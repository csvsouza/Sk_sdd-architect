"""Local, read-only SDD checks and initial draft rendering. No network/LLM calls."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import re
import sys
from datetime import date
from pathlib import Path
import yaml

CORPORATE = ('empresa-processos.md', 'empresa-desenvolvimento.md')
STATES = {'previsto', 'implementado_nao_verificado', 'verificado_conforme',
          'nao_conforme', 'nao_aplicavel', 'excecao_aprovada', 'pendente'}
SECTIONS = ['Identificação e controle', 'Resumo executivo', 'Visão de produto',
            'Mapa funcional', 'Visão de engenharia', 'Dados e conceitos', 'Fluxos',
            'Orientações para uso', 'Falhas e suporte', 'Operação', 'Governança',
            'Estado do projeto', 'Índice documental', 'Pendências documentais']
WEIGHTS = {'produto': 15, 'escopo': 20, 'governanca': 20,
           'engenharia': 15, 'verificacao': 20, 'seguranca_operacao': 10}


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    result = {}
    for k, v in node.value:
        key = loader.construct_object(k, deep=deep)
        if key in result:
            raise ValueError(f'chave YAML duplicada: {key}')
        result[key] = loader.construct_object(v, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def read(path):
    return yaml.load(Path(path).read_text(encoding='utf-8-sig'), Loader=UniqueLoader)


def frontmatter(path):
    text = Path(path).read_text(encoding='utf-8-sig')
    match = re.match(r'^---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
    if not match:
        raise ValueError(f'{Path(path).name}: metadados YAML ausentes')
    data = yaml.load(match[1], Loader=UniqueLoader)
    if not isinstance(data, dict):
        raise ValueError('frontmatter deve ser objeto')
    return data, text[match.end():]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def portable(root, value):
    if not isinstance(value, str) or not value or '\\' in value or ':' in value:
        raise ValueError(f'caminho não portátil: {value}')
    base = Path(root).resolve()
    p = (base / value).resolve()
    if not p.is_relative_to(base):
        raise ValueError(f'caminho fora da raiz: {value}')
    return p


def ipc(data):
    if data.get('rubric_version') != 'ipc-1.0':
        raise ValueError('rubrica não suportada; registre nova implementação para nova rubrica')
    dims = data.get('dimensions', [])
    if {d['id'] for d in dims} != set(WEIGHTS) or len(dims) != 6:
        raise ValueError('dimensões ausentes ou duplicadas')
    seen, total, earned, scores = set(), 0.0, 0.0, {}
    for d in dims:
        if d['weight'] != WEIGHTS[d['id']] or len(d['items']) != 2:
            raise ValueError('pesos/itens divergem da rubrica ipc-1.0')
        den = num = 0.0
        for n, item in enumerate(d['items'], 1):
            if item['id'] != f"{d['id']}-{n}" or item['id'] in seen:
                raise ValueError('ID de item duplicado ou divergente da rubrica')
            seen.add(item['id'])
            score = item.get('score')
            if isinstance(score, bool) or score not in (0, 0.5, 1):
                raise ValueError('nota deve ser 0, 0.5 ou 1')
            if not isinstance(item.get('applicable'), bool):
                raise ValueError('applicable deve ser booleano')
            if not item['applicable']:
                if not item.get('justification'):
                    raise ValueError('N/A sem justificativa')
                continue
            if score > 0 and not item.get('source'):
                raise ValueError('nota positiva sem fonte')
            weight = d['weight'] / len(d['items'])
            den += weight
            num += weight * score
        scores[d['id']] = None if den == 0 else 100 * num / den
        total += den
        earned += num
    raw = None if not total else 100 * earned / total
    band = ('nao_calculavel' if raw is None else 'contexto_insuficiente' if raw < 60
            else 'especificacao_parcial' if raw < 80 else 'candidata_revisao' if raw < 90
            else 'candidata_aprovacao')
    return {'rubric_version': data['rubric_version'], 'ipc_raw': raw,
            'ipc_display': None if raw is None else math.floor(raw + 0.5),
            'dimensions': scores, 'applicable_weight': total, 'band': band,
            'critical_blockers': data.get('critical_blockers', []),
            'approval_blocked': bool(data.get('critical_blockers')) or raw is None,
            'approval': 'nao_concedida',
            'meaning': 'Completude contextual; não é probabilidade de acerto.'}


def select(context):
    docs = {'spec.md': 'requisitos, abordagem, validações e registros compactos',
            'projeto-regras.md': 'base adotada e regras locais',
            'visao-geral-projeto.md': 'entrada documental obrigatória'}
    if context.get('components', 1) > 1:
        docs.update({'architecture.md': 'fronteiras entre componentes', 'tasks.md': 'dependências entre componentes',
                     'testing.md': 'verificação entre componentes'})
    if context.get('data_change'):
        docs['database.md'] = 'persistência/transações afetadas'
    if context.get('integration'):
        docs['integrations.md'] = 'contratos entre sistemas'
    if context.get('operation'):
        docs['operations.md'] = 'execução recorrente e recuperação'
    if context.get('risk') == 'alto':
        docs['security.md'] = 'risco alto exige revisão dedicada'
    return docs


def load_rules(config_path, baseline=None):
    config_path = Path(config_path)
    cfg = read(config_path)
    root = cfg.get('corporate_root')
    root = (config_path.parent / root).resolve() if root else None
    report = {'sources': [], 'gaps': [], 'changes': [], 'conformity': 'nao_declarada'}
    adopted = {s['name']: s for s in (baseline or {}).get('sources', [])}
    for name in CORPORATE:
        path = root / name if root else None
        fallback = False
        if path is None or not path.is_file():
            cache = cfg.get('corporate_cache')
            path = config_path.parent / cache / name if cache else None
            fallback = True
            report['gaps'].append(f'{name}: fonte central indisponível')
        try:
            if path is None:
                raise ValueError('sem fonte')
            digest = sha(path)
            if fallback and (name not in adopted or adopted[name]['sha256'] != digest):
                raise ValueError('cópia sem hash correspondente à base adotada')
            meta, body = frontmatter(path)
            for key in ('version', 'status', 'responsible', 'history', 'origin'):
                if not meta.get(key):
                    report['gaps'].append(f'{name}: {key} ausente/incompleto')
            if meta.get('status') != 'aprovado':
                report['gaps'].append(f'{name}: status não aprovado')
            if not meta.get('approval_evidence'):
                report['gaps'].append(f'{name}: aprovação não documentada')
            if not body.strip():
                report['gaps'].append(f'{name}: conteúdo ausente')
            entry = {'name': name, 'origin': meta.get('origin'), 'version': meta.get('version'),
                     'sha256': digest, 'fallback': fallback, 'status': meta.get('status')}
            report['sources'].append(entry)
            if name in adopted and adopted[name]['sha256'] != digest:
                report['changes'].append({'name': name, 'adopted': adopted[name], 'available': entry,
                                          'action': 'avaliar impacto; base mantida até adoção explícita'})
        except (OSError, ValueError, yaml.YAMLError) as exc:
            report['gaps'].append(f'{name}: {exc}')
    return report


def check_overview(path):
    path = Path(path)
    errors = []
    meta, body = frontmatter(path)
    required = {'schema_version', 'project_id', 'project_name', 'document_version', 'updated_at',
                'responsible', 'project_phase', 'intended_audiences', 'source_baseline',
                'corporate_rules_baseline', 'documentation_readiness', 'known_gaps', 'outputs'}
    errors += [f'metadado ausente: {key}' for key in sorted(required - meta.keys())]
    if meta.get('schema_version') != '1.0':
        errors.append('schema_version não suportado')
    for key in ('project_id', 'project_name', 'document_version', 'updated_at', 'responsible', 'project_phase'):
        if meta.get(key) is not None and not isinstance(meta[key], str):
            errors.append(f'{key}: string ou null exigido (datas entre aspas)')
    if isinstance(meta.get('updated_at'), str):
        try:
            date.fromisoformat(meta['updated_at'])
        except ValueError:
            errors.append('updated_at: data ISO inválida')
    ready = {'pendente', 'parcial', 'pronto_para_revisao'}
    if meta.get('documentation_readiness') not in ready:
        errors.append('documentation_readiness inválido')
    for key in ('intended_audiences', 'source_baseline', 'corporate_rules_baseline', 'known_gaps', 'outputs'):
        if not isinstance(meta.get(key), list):
            errors.append(f'{key}: lista exigida')
    for key in ('intended_audiences', 'known_gaps'):
        if isinstance(meta.get(key), list) and any(not isinstance(x, str) for x in meta[key]):
            errors.append(f'{key}: itens devem ser strings')
    for section in SECTIONS:
        if f'## {section}\n' not in body.replace('\r\n', '\n'):
            errors.append(f'seção ausente: {section}')
    sources = meta.get('source_baseline', [])
    if not isinstance(sources, list):
        sources = []
    seen_paths = set()
    for s in sources:
        if not isinstance(s, dict) or not {'path', 'revision', 'sha256'} <= s.keys():
            errors.append('source_baseline: registro incompleto')
            continue
        try:
            p = portable(path.parent, s['path'])
            if s['path'] in seen_paths:
                errors.append('source_baseline: caminho duplicado')
            seen_paths.add(s['path'])
            if not p.is_file():
                errors.append(f"fonte inacessível: {s['path']}")
            elif s['sha256'] and sha(p) != s['sha256']:
                errors.append(f"fonte desatualizada: {s['path']}")
            if s['sha256'] is not None and not re.fullmatch('[0-9a-f]{64}', str(s['sha256'])):
                errors.append('sha256 inválido')
            if s['revision'] is not None and not isinstance(s['revision'], str):
                errors.append('revision deve ser string ou null')
        except ValueError as exc:
            errors.append(str(exc))
    corp = meta.get('corporate_rules_baseline', [])
    if not isinstance(corp, list) or len(corp) != 2 or {x.get('name') for x in corp if isinstance(x, dict)} != set(CORPORATE):
        errors.append('duas fontes corporativas devem estar explicitadas')
    else:
        for s in corp:
            if not {'name', 'origin', 'revision', 'sha256', 'path'} <= s.keys():
                errors.append('base corporativa incompleta')
            elif s['path'] is not None and s['path'] not in seen_paths:
                errors.append('snapshot corporativo não consta nas fontes')
            for key in ('origin', 'revision', 'sha256', 'path'):
                if s.get(key) is not None and not isinstance(s[key], str):
                    errors.append(f'base corporativa: {key} deve ser string ou null')
            if s.get('sha256') is not None and not re.fullmatch('[0-9a-f]{64}', str(s['sha256'])):
                errors.append('base corporativa: sha256 inválido')
    for o in meta.get('outputs', []) if isinstance(meta.get('outputs'), list) else []:
        if not isinstance(o, dict) or not {'type', 'audience', 'status', 'sources', 'evidence', 'gaps'} <= o.keys():
            errors.append('prontidão por saída incompleta')
        elif o['status'] not in ready:
            errors.append('status de saída inválido')
        elif o['type'] == 'manual_validado' and o['status'] == 'pronto_para_revisao' and not o['evidence']:
            errors.append('manual validado sem evidência')
        if isinstance(o, dict):
            for key in ('sources', 'evidence', 'gaps'):
                if not isinstance(o.get(key), list) or any(not isinstance(x, str) for x in o.get(key, [])):
                    errors.append(f'saída: {key} exige lista de strings')
            if o.get('audience') is not None and not isinstance(o['audience'], str):
                errors.append('saída: audience deve ser string ou null')
    if meta.get('documentation_readiness') == 'pronto_para_revisao':
        if not sources or not meta.get('project_id') or not meta.get('document_version'):
            errors.append('prontidão sem identificação/base suficiente')
        if any(not s.get('sha256') or not s.get('revision') for s in sources if isinstance(s, dict)):
            errors.append('prontidão com revisão de fonte pendente')
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', body):
        if target.startswith(('https://', 'http://', '#')):
            continue
        try:
            if not portable(path.parent, target.split('#')[0]).exists():
                errors.append(f'link quebrado: {target}')
        except ValueError as exc:
            errors.append(str(exc))
    diagrams = re.findall(r'```mermaid\s*\n(.*?)```', body, re.S)
    if not any(d.lstrip().startswith('flowchart ') for d in diagrams):
        errors.append('fluxograma ausente')
    if not any(d.lstrip().startswith('mindmap') for d in diagrams):
        errors.append('mapa mental ausente')
    return {'errors': errors, 'sync': 'pendente' if errors else 'bases_conferidas_revisao_semantica_necessaria' if sources else 'sem_fontes_registradas',
            'mermaid': 'presença verificada; sintaxe/renderização dependem de ferramenta externa'}


def check_records(data, root):
    errors, ids = [], set()
    for r in data.get('records', []):
        rid = r.get('id')
        if not rid or rid in ids:
            errors.append(f'ID ausente/duplicado: {rid}')
        ids.add(rid)
        state = r.get('status')
        if state not in STATES:
            errors.append(f'{rid}: estado inválido')
        for key in ('origin', 'revision', 'requirement', 'component', 'task', 'verification'):
            if not r.get(key):
                errors.append(f'{rid}: {key} ausente')
        if state == 'nao_aplicavel' and not r.get('justification'):
            errors.append(f'{rid}: N/A sem justificativa')
        if state in ('implementado_nao_verificado', 'verificado_conforme', 'excecao_aprovada') and not r.get('evidence'):
            errors.append(f'{rid}: evidência ausente')
        if state == 'excecao_aprovada' and not any(
                e.get('id') == r.get('exception_id') and e.get('status') == 'aprovado'
                for e in data.get('exceptions', [])):
            errors.append(f'{rid}: exceção aprovada não vinculada')
        if r.get('evidence'):
            try:
                if not portable(root, r['evidence']).is_file():
                    errors.append(f'{rid}: evidência inacessível')
            except ValueError as exc:
                errors.append(str(exc))
    for e in data.get('exceptions', []):
        for key in ('id', 'rule', 'revision', 'justification', 'scope', 'approver', 'evidence', 'valid_until', 'controls', 'status'):
            if not e.get(key):
                errors.append(f'exceção: {key} ausente')
        if e.get('status') == 'aprovado':
            try:
                if date.fromisoformat(e['valid_until']) < date.today():
                    errors.append('exceção expirada')
                if not portable(root, e['evidence']).is_file():
                    errors.append('exceção: evidência inacessível')
            except (KeyError, ValueError, TypeError):
                errors.append('exceção aprovada inválida')
    for a in data.get('approvals', []):
        allowed = {'nao_submetido', 'aguardando_aprovacao', 'aprovado', 'aprovado_com_condicoes', 'reprovado', 'invalidado_por_mudanca'}
        if a.get('status') not in allowed:
            errors.append('aprovação: estado inválido')
        if a.get('status') in ('aprovado', 'aprovado_com_condicoes'):
            for key in ('id', 'stage', 'versions', 'criteria', 'responsible', 'date', 'evidence'):
                if not a.get(key):
                    errors.append(f'aprovação: {key} ausente')
            try:
                date.fromisoformat(a['date'])
                if not portable(root, a['evidence']).is_file():
                    errors.append('aprovação: evidência inacessível')
            except (KeyError, ValueError, TypeError):
                errors.append('aprovação: data/evidência inválida')
            if a.get('status') == 'aprovado_com_condicoes' and not a.get('conditions'):
                errors.append('aprovação condicional sem condições')
    return {'errors': errors, 'semantic_review': 'necessaria; existência não autentica evidência'}


def render(input_path, output):
    """Render agent-authored sections without inventing business behavior. Never overwrite."""
    data = read(input_path)
    output = Path(output)
    meta = data['metadata']
    sections = data.get('sections', {})
    text = '---\n' + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False) + '---\n\n'
    for name in SECTIONS:
        text += f'## {name}\n\n{sections.get(name) or "Pendente: conteúdo não fornecido; não presumir comportamento."}\n\n'
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('x', encoding='utf-8', newline='\n') as f:
        f.write(text)
    return {'created': str(output), 'status': 'rascunho; executar check e revisão semântica'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('ipc', 'select', 'records', 'check'):
        p = sub.add_parser(name)
        p.add_argument('input', type=Path)
    p = sub.add_parser('rules')
    p.add_argument('input', type=Path)
    p.add_argument('--baseline', type=Path)
    p = sub.add_parser('render')
    p.add_argument('input', type=Path)
    p.add_argument('output', type=Path)
    args = parser.parse_args()
    try:
        if args.command == 'ipc':
            result = ipc(read(args.input))
        elif args.command == 'select':
            result = select(read(args.input))
        elif args.command == 'rules':
            result = load_rules(args.input, read(args.baseline) if args.baseline else None)
        elif args.command == 'records':
            result = check_records(read(args.input), args.input.parent)
        elif args.command == 'render':
            result = render(args.input, args.output)
        else:
            result = check_overview(args.input)
        print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
        return 1 if result.get('errors') or result.get('gaps') or result.get('changes') else 0
    except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as exc:
        print(json.dumps({'error': str(exc)}, ensure_ascii=False))
        return 2


if __name__ == '__main__':
    sys.exit(main())
