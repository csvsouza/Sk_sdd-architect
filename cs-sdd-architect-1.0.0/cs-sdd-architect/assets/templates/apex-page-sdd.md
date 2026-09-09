---
version: null
status: rascunho
responsible: null
application_id: null
page_id: null
page_alias: null
module: null
legacy_screens: []
source_baseline: []
known_gaps: []
---
# SDD da página APEX

Remova estas orientações ao preencher. Não invente aplicação, página, owner, objetos, versões ou componentes disponíveis.

## Objetivo e valor

Problema, público, resultado observável, escopo, exclusões e critérios de sucesso.

## Identidade e herança CS

- Gestão, módulo, aplicação e página:
- Página principal, modal ou dependente:
- Origem Delphi e `cod_telas`:
- `page_tree` ou justificativa N/A:
- Alias:
- Scaffold, CS-Template, subscriptions e componentes compartilhados avaliados:
- Fonte/hash do guideline CS APEX:

## Jornada e estados

Fluxo principal, alternativas, cancelamento, retorno de modal, erros, sessão expirada, retomada e estados persistidos.

## Segurança e alçada

Alçada, `Solicitar Senha`, `contexto_alcada`, página pública, atores, permissões, acesso direto, submissão manipulada e validação no servidor.

## Componentes da página

| ID | Tipo | Nome/Static ID | Origem dos dados | Evento/ação | Condição | Regra relacionada |
| --- | --- | --- | --- | --- | --- | --- |

Detalhar itens, regiões, botões, grids, LOVs, Dynamic Actions, processos, validações e branches realmente aplicáveis.

## Dados e PL/SQL

Tabelas, chaves, nulabilidade, owner, Parsing Schema, packages, procedures/functions, triggers, views, grants existentes, logging, transação e tratamento de erro. Separar existente, planejado e pendente.

## Estado, arquivos e integrações

Application Items, CS Collections, uploads, importações, APIs e filas aplicáveis; incluir ciclo de vida, isolamento, volume, idempotência e recuperação.

## Padrões visuais e navegação

Filtros, drawer, grids, cards, tabs, modais, código/descrição, TAB por ENTER, mensagens traduzíveis, responsividade e dependências do guideline UI/UX.

## Critérios de aceite

| ID | Cenário | Pré-condição | Ação | Resultado verificável | Camada | Evidência esperada |
| --- | --- | --- | --- | --- | --- | --- |

Incluir cenários válido, inválido, não autorizado, acesso direto, manipulação de request, sessão expirada, erro parcial e retomada quando aplicáveis.

## Release e operação

Check-in/autosave, páginas bloqueadas, APP por time, página por cliente, Menu Apex, promoção entre ambientes, rollback/recuperação, suporte e evidências.

## Rastreabilidade

| Regra/fonte | Requisito | Componente/decisão | Tarefa | Teste | Evidência | Estado |
| --- | --- | --- | --- | --- | --- | --- |

## Pendências e aprovações

Decisões ainda necessárias, impacto, responsável real a confirmar, evidência exigida e trabalho que pode continuar sem a decisão.

