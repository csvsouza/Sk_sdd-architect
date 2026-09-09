# Instalação, configuração e uso

A entrega é uma skill local para Codex com acesso a arquivos. A pasta completa `cs-sdd-architect` é a unidade de instalação; a pasta validation do projeto contém avaliação reproduzível e não é necessária em produção. O agente faz entrevista e redação; Python/PyYAML são usados somente pelos utilitários determinísticos. Não depende de Oracle, APEX, chaves API ou plugin para especificar.

## Instalar

No ambiente fornecido, as instruções locais de criação usam `$CODEX_HOME/skills` ou `$USERPROFILE/.codex/skills` quando CODEX_HOME não estiver definido. Copie a pasta completa para esse local, sem sobrescrever outra versão silenciosamente:

```powershell
$sddRoot = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $env:USERPROFILE '.codex\skills' }
$sddTarget = Join-Path $sddRoot 'cs-sdd-architect'
if (Test-Path -LiteralPath $sddTarget) { throw 'Já existe uma instalação; compare e preserve a versão anterior antes de atualizar.' }
New-Item -ItemType Directory -Force -Path $sddRoot | Out-Null
Copy-Item -LiteralPath '.\cs-sdd-architect' -Destination $sddTarget -Recurse
```

Abra uma nova sessão e invoque `$cs-sdd-architect`; se ainda não aparecer, informe o caminho do SKILL.md explicitamente e confira o mecanismo de descoberta da sua instalação. A descoberta automática está habilitada por padrão. O pacote foi validado estruturalmente nesta entrega; ativação em nova sessão não foi testada. Nenhuma instalação global foi feita nesta implementação.

O formato de skill com SKILL.md e recursos progressivos também está descrito na [documentação oficial de skills](https://learn.chatgpt.com/docs/build-skills), consultada em 08/09/2026. O destino acima segue as instruções locais deste ambiente, não pressupõe que todo host use o mesmo diretório.

Para os utilitários, crie ambiente virtual local e instale a dependência:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r .\cs-sdd-architect\requirements.txt
.\.venv\Scripts\python.exe .\cs-sdd-architect\scripts\sdd.py --help
```

Validado aqui com Python 3.14.6/PyYAML 6.0.3 em Windows. Outras versões/plataformas não foram executadas nesta avaliação. Não copie a .venv para a instalação da skill.

## Configurar padrões e compartilhar

1. O mantenedor copia `assets/templates/empresa-processos.md` e `empresa-desenvolvimento.md` para uma fonte central versionada escolhida pela empresa. Preenche conteúdo real, versão, responsável, status, histórico e evidência de aprovação; IDs estáveis para regras, escopo/classificação, aceite/evidência e política de exceção.
2. Registre aprovação e publicação de uma revisão identificável. O mecanismo pode ser repositório, pasta versionada ou exportação controlada; não há serviço de sincronização implementado. Disponibilize somente a quem pode ler o conteúdo e não grave segredos nos arquivos.
3. Em cada projeto, copie `sdd-config.yaml`, configure corporate_root para essa fonte acessível e peça à skill que leia os dois arquivos. Configuração e baselines são do projeto, não da memória de conversa. Preencha projeto-regras.md com regras locais ou declaração explícita de ausência.
4. Registre origem/revisão/hash em baseline.json e nas fontes da visão geral. Para consumo portátil, mantenha snapshots autorizados em regras/ com origem preservada. Os exemplos mostram dois projetos usando a mesma fonte central fictícia.
5. Nova versão corporativa: compare impacto antes de adotar explicitamente em projeto existente. Preserve base/histórico e revisão anterior; atualize aprovações afetadas. Fonte indisponível: fallback apenas com hash adotado correspondente e limitação registrada. Ausência/incompletude impede conformidade, mas permite rascunho.

O catálogo de modelos começa vazio. Para cada entrada, registrar id exato, supported_efforts (lista), required_capabilities (lista), context_limit (número/null), tools (lista), latency_evidence (string/null), source (URL), verified_at (data), environment_availability (confirmada/pendente), billing_regime (API/assinatura), prices (objeto por categoria/moeda/unidade ou null) e restrictions (lista). Confirmar fontes oficiais no momento da recomendação; não copiar hipóteses de modelos como capacidades verificadas.

## Exemplo de uso

```text
Use $cs-sdd-architect. Especifique uma automação Python que recebe lotes e persiste no Oracle.
Leia sdd-config.yaml e os documentos existentes. O operador precisa retomar lotes interrompidos
sem duplicar registros. Ainda não temos confirmação da chave de idempotência nem das versões.
Gere os documentos proporcionais, o IPC e a visão geral, mantendo essas decisões pendentes.
```

Resultado esperado: descoberta das lacunas críticas sem repetir informações; spec e regras locais, contratos/transações/retomada, tarefas e testes propostos; visão geral planejada com Mermaid, fontes e lacunas para manual. Veja [exemplo materializado](examples/python-oracle/visao-geral-projeto.md) e sua [entrada](examples/python-oracle/entrada.md). Todos os dados dos exemplos são fictícios.

Para mudança: `A solicitação agora exige revisão do operador antes de envio; atualize a especificação.` A skill deve atualizar fontes, visão geral e diagramas afetados na mesma execução, reavaliando IPC/modelos/aprovações, sem um pedido adicional para documentação. Veja [avaliação de mudança](examples/mudancas/registro.md).

## Validar e entregar ao próximo consumidor

Comandos detalhados em [utilitários](references/utilitarios.md). Na raiz desta entrega: `.\.venv\Scripts\python.exe validation/evaluate.py` executa as fixtures e salva `validation/results.json`. Leia o relatório da entrega para diferenciar cobertura estrutural e semântica.

Entregue ao consumidor a visão geral e fontes relativas acessíveis, contrato 1.0, estados, evidências e pendências por público/tipo de saída. Não entregue credenciais. Não declare manual validado com base somente em especificação aprovada.

## Pendências da empresa

Conteúdo e vigência dos dois padrões; fonte central e acesso; responsáveis/processo de aprovação e exceção; versões/restrições da stack; exemplos reais de package/APEX/automação; catálogo/orçamento e distribuição na equipe. Sem essas informações, nenhuma conformidade corporativa, validação de negócio ou economia monetária foi demonstrada.
