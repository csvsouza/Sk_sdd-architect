---
schema_version: '1.0'
project_id: apex-pequeno
project_name: EXEMPLO FICTÍCIO apex-pequeno
document_version: '1.0'
updated_at: '2026-09-08'
responsible: null
project_phase: rascunho
intended_audiences:
- negócio
- engenharia
- suporte
source_baseline:
- path: regras/empresa-processos.md
  revision: 1.0-ficticia
  sha256: 5e542b56fc4c7a305dc129737bbe17a724bf8ab16e4f696a0b41b1467a575366
- path: regras/empresa-desenvolvimento.md
  revision: 1.0-ficticia
  sha256: bc1c7752b9f3a8cf59c41de4fd49bf21f54b0a1c14db0a85a23d134a75157bf7
- path: entrada.md
  revision: '1.0'
  sha256: e2c491eaf840385a35a47fab27ada2a0f237d11c78181c2c41a1d5e6a0a16673
- path: projeto-regras.md
  revision: '1.0'
  sha256: 3812f77dd5d12df09519d6dc4e3ff04b9f1709c469e6e8b1f0dbb349408cba93
- path: spec.md
  revision: '1.0'
  sha256: 2d9637ed355e434dade53ae5fadf336a2850d9dc386d66fc4421ef8e461dd090
corporate_rules_baseline:
- name: empresa-processos.md
  origin: fixture://empresa-ficticia/empresa-processos.md
  revision: 1.0-ficticia
  sha256: 5e542b56fc4c7a305dc129737bbe17a724bf8ab16e4f696a0b41b1467a575366
  path: regras/empresa-processos.md
- name: empresa-desenvolvimento.md
  origin: fixture://empresa-ficticia/empresa-desenvolvimento.md
  revision: 1.0-ficticia
  sha256: bc1c7752b9f3a8cf59c41de4fd49bf21f54b0a1c14db0a85a23d134a75157bf7
  path: regras/empresa-desenvolvimento.md
documentation_readiness: parcial
known_gaps:
- Versões da stack e ambiente real não fornecidos
- Implementação não executada
outputs:
- type: apresentacao_conceitual
  audience: negócio
  status: pronto_para_revisao
  sources:
  - spec.md
  evidence: []
  gaps:
  - Revisão humana pendente
- type: manual_validado
  audience: usuários
  status: pendente
  sources:
  - spec.md
  evidence: []
  gaps:
  - Sistema e interface não implementados
---

## Identificação e controle

Projeto apex-pequeno, fictício. Documento 1.0, formato 1.0, responsável pendente. Fontes/revisões no YAML.

## Resumo executivo

Problema: atendentes têm dificuldade de localizar pedidos por situação. MVP: filtrar a consulta existente; excluir alterações de cadastro. Prioridade alta pelo valor de localização, esforço relativo pequeno e dependência da consulta atual. Indicador: tempo de localização por tarefa; baseline e meta pendentes. Alternativa de nova página descartada como proposta por duplicar manutenção.

## Visão de produto

Síntese do MVP e valor acima; prioridades, métrica e alternativas em [spec](spec.md).

## Mapa funcional

FUN-01 — Consultar pedidos por situação. Origem: [REQ-01](spec.md); entradas/saídas e dependências ali descritas. Estado planejado.

## Visão de engenharia

APEX confirmado, versão pendente. Reutilizar consulta e convenções existentes após inspecionar exportação. Nenhuma migração ou integração nova. Autorização existente preservada e testada no servidor, sem inventar IDs de página. Fonte: [spec](spec.md).

## Dados e conceitos

Pedido e situação; somente leitura; ciclo de vida do cadastro preservado.

## Fluxos

**Fluxo de negócio proposto**, fonte [REQ-01](spec.md); não é fluxo de desenvolvimento.

```mermaid
flowchart TD
  A([Inicio]) --> B["Aplicar filtro"]
  B --> C{"Permissao e dados validos?"}
  C -->|Nao| E["Interromper e registrar pendencia"]
  C -->|Sim| D["Exibir pedidos correspondentes"]
  D --> F([Fim])
```

Descrição textual: iniciar, aplicar filtro, verificar permissão e dados; inválidos interrompem com pendência, válidos seguem para exibir pedidos correspondentes e fim.

**Mapa mental**, fonte [produto/engenharia](spec.md).

```mermaid
mindmap
  root((apex-pequeno))
    Produto
      Consultar pedidos por situação
    Usuarios
      Perfis da entrada
    Modulos
      Componentes do spec
    Dados
      Entidades do spec
    Integracoes
      Sem integracao nova
    Regras
      Base ficticia
    Operacao
      Consulta existente
```

Descrição textual: projeto organizado em produto, usuários, módulos, dados, integrações, regras e operação; os nós remetem aos conceitos do spec. Sintaxe/renderização: consultar relatório de avaliação, não presumir.

## Orientações para uso

PROC-01: objetivo e público conhecidos na entrada; pré-condição: acesso autorizado ao ambiente. Passos operacionais: pendentes de interface/exportação. Resultado esperado: REQ-01; exceções: permissões e dados inválidos. Estado: planejado, não validado; coletar evidência do sistema. Nenhum botão ou comando foi presumido.

## Falhas e suporte

Falhas relevantes e recuperação em [spec](spec.md). Mensagens e encaminhamento real pendentes; não inventar códigos.

## Operação

Consulta existente somente leitura; implantação segue processo ainda não fornecido. Recuperação de gravação N/A porque não há escrita nova.

## Governança

Base fictícia 1.0-ficticia, não é padrão real; [regras locais](projeto-regras.md). Gates não submetidos; nenhum aceite humano real.

## Estado do projeto

FUN-01 planejada. Implementação e verificação de negócio não executadas. Documentação conceitual candidata à revisão; manual validado pendente de execução e evidências.

## Índice documental

- [regras/empresa-processos.md](regras/empresa-processos.md) — revisão 1.0-ficticia.
- [regras/empresa-desenvolvimento.md](regras/empresa-desenvolvimento.md) — revisão 1.0-ficticia.
- [entrada.md](entrada.md) — revisão 1.0.
- [projeto-regras.md](projeto-regras.md) — revisão 1.0.
- [spec.md](spec.md) — revisão 1.0.

## Pendências documentais

Confirmar versões, padrões reais, aprovadores e interface. Sem material para manual validado. Histórico: 1.0 consolidação inicial fictícia, nenhuma aprovação atribuída.

