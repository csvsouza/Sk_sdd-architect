---
version: "0.1.0-proposta"
status: rascunho
responsible: null
origin: "Proposta derivada do processo SDD e PMO do CS_Genesis v9.4.0, por solicitação do usuário em 2026-09-09"
approval_evidence: null
history:
  - "0.1.0-proposta - 2026-09-09 - consolidação inicial do processo geral de SDD, documentação, rastreabilidade, mudança e release; aprovação corporativa pendente"
---
# Regras corporativas de processo

Este documento reúne regras gerais candidatas para descoberta, especificação, desenvolvimento, validação, mudança e entrega de projetos conduzidos por SDD. As regras do domínio, do produto e da solução permanecem em `projeto-regras.md` e nos documentos específicos de cada projeto.

Enquanto `status` não for `aprovado` e `approval_evidence` permanecer nulo, o conteúdo deve ser tratado como proposta de baseline, não como comprovação de conformidade corporativa.

## Princípio de herança

Cada projeto deve adotar uma versão identificada de `empresa-processos.md` e `empresa-desenvolvimento.md` e então complementar essa base com suas regras locais. Regra local pode detalhar ou tornar a baseline mais rigorosa; conflito, flexibilização ou exceção não substitui a regra geral sem decisão e aprovação registradas.

## Entregáveis mínimos do SDD

Os nomes físicos podem variar conforme o template do projeto, mas a responsabilidade documental deve existir e ser rastreável:

- entrada PMO ou registro de descoberta preservado como fonte;
- visão geral do projeto;
- catálogo de requisitos e critérios de aceite;
- regras de negócio (`BUSINESS_RULES.md` ou documento equivalente);
- arquitetura e decisões/ADRs aplicáveis;
- tarefas, estratégia e evidências de teste;
- regras locais do projeto e baseline corporativa adotada;
- histórico canônico de mudanças (`CHANGELOG.md`, `HISTORICO_ALTERACOES.md` ou equivalente definido pelo projeto);
- plano e evidências de release quando houver implantação.

Artefatos adicionais devem ser selecionados de forma proporcional ao risco, à stack e ao tipo de mudança; esta lista não obriga a criação de documentos vazios ou duplicados.

## Regras

| ID estável | Descrição | Escopo | Classificação obrigatoria/recomendacao | Critério de conformidade | Evidência exigida | Política de exceção | Aprovador |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PROC-001 | Iniciar o SDD a partir de uma entrada PMO ou descoberta estruturada, versionada e preservada como fonte, com IDs estáveis para cada campo relevante. | Todos os projetos | obrigatoria | A fonte de entrada identifica projeto, solicitante, responsáveis, data, prioridade e respostas por ID; alterações posteriores não apagam a versão recebida. | Documento PMO/descoberta, hash ou commit e histórico de revisões. | Projeto sem PMO formal deve produzir registro equivalente e obter aceite do responsável de negócio. | Product Owner ou solicitante autorizado |
| PROC-002 | Separar informação de negócio de validação técnica, preservando a autoria e a responsabilidade de cada decisão. Informação encontrada em outra seção pode evitar pergunta repetida, mas não transfere aprovação entre responsáveis. | Descoberta, requisitos e arquitetura | obrigatoria | Requisitos funcionais têm fonte de negócio; contratos, versões e assinaturas têm fonte técnica; reconciliações indicam origem e limite. | Matriz de fontes, decisões e aprovações por papel. | Acúmulo de papéis deve ser declarado e aprovado na governança do projeto. | Product Owner e responsável técnico |
| PROC-003 | Registrar problema, objetivo, valor, escopo incluído/excluído, gatilho, entradas, saídas, consumidor, restrições, riscos e sucesso observável antes do plano de implementação. | Descoberta e produto | obrigatoria | Os campos aplicáveis estão respondidos; desconhecidos permanecem como pendências e não são completados por inferência. | PMO, visão geral e critérios de aceite. | Item não aplicável deve usar `N/A` com motivo e responsável pela confirmação. | Product Owner |
| PROC-004 | Manter documento de regras de negócio com gatilho, entradas, elegibilidade, fluxo etapa a etapa, transformações, validações, comportamento sem dados, tratamento de erro, saída e consumidor. | Requisitos e desenvolvimento | obrigatoria | As regras têm IDs estáveis e correspondem ao comportamento especificado e implementado, sem substituir a fonte original. | `BUSINESS_RULES.md` ou equivalente, revisão funcional e rastreabilidade. | Formato alternativo é permitido se cobrir integralmente o conteúdo e estiver indicado no índice documental. | Responsável funcional |
| PROC-005 | Catalogar requisitos funcionais, regras de negócio e requisitos não funcionais com IDs estáveis e preservá-los em arquitetura, tarefas, testes e mudanças. | Todo o ciclo SDD | obrigatoria | Nenhum requisito aprovado perde ou troca de ID silenciosamente; obsolescência é registrada com motivo e revisão. | Catálogo de requisitos, matriz de rastreabilidade e histórico. | Renumeração excepcional exige mapa de equivalência e aprovação dos consumidores do documento. | Product Owner e responsável técnico |
| PROC-006 | Definir critérios de aceite observáveis e verificáveis, com cenário, resultado esperado, fonte e responsável pela confirmação. | Requisitos e QA | obrigatoria | Cada entrega funcional possui ao menos um critério de aceite ligado a requisito e teste/evidência. | Catálogo de critérios, testes e aceite registrado. | Critério inicialmente não automatizável deve ter procedimento manual, responsável e evidência esperada. | Responsável funcional e QA |
| PROC-007 | Registrar decisões arquiteturais, alternativas, consequências, dependências, limites e exceções antes de implementar pontos que delas dependam. | Arquitetura e governança | obrigatoria | Toda decisão relevante tem ID, status, origem, motivo, impacto e aprovador; pendência bloqueia somente o trabalho dependente. | ADR/registro de decisão e análise de impacto. | Decisão emergencial deve ter autorização, validade, controles compensatórios e prazo de regularização. | Responsável técnico e demais donos do risco |
| PROC-008 | Manter rastreabilidade bidirecional entre regra corporativa/local, requisito, decisão ou componente, tarefa, teste, evidência e status. | Todo o ciclo SDD | obrigatoria | É possível percorrer a cadeia nos dois sentidos sem requisito órfão nem trabalho sem finalidade registrada. | Matriz de rastreabilidade validada. | Relação não aplicável exige justificativa explícita; campo vazio não equivale a `N/A`. | Responsável técnico e QA |
| PROC-009 | Avaliar prontidão antes de liberar implementação e novamente nos marcos relevantes; separar pontuação, bloqueios e decisões humanas pendentes. | Planejamento e gates | obrigatoria | O índice ou matriz usado é reproduzível, desconhecidos não recebem pontuação, bloqueios são listados à parte e não são mascarados pelo total. | Relatório de prontidão, entradas do cálculo e decisão do gate. | O projeto pode adotar método diferente, desde que critérios, pesos, limiares e aprovador sejam definidos e versionados. | Governança do projeto |
| PROC-010 | Não gerar solução final quando faltarem regra de negócio, fonte de dados, contrato, destino, responsável, aprovação protegida ou teste mínimo necessário; não declarar template, skeleton ou TODO como entrega completa. | Planejamento, desenvolvimento e entrega | obrigatoria | Lacunas aparecem como pendências/bloqueios e o status da entrega corresponde ao que foi realmente produzido e verificado. | Checklist de gate, relatório de pendências e revisão do artefato. | Aceite de risco deve ser explícito, limitado, versionado e emitido por quem possui autoridade sobre a lacuna. | Product Owner e responsável técnico |
| PROC-011 | Preservar literalmente fontes fornecidas como vinculantes — inclusive código legado, SQL, contratos e evidências — e distinguir transcrição, síntese e interpretação. | Descoberta e manutenção | obrigatoria | A fonte original permanece acessível e íntegra; derivados apontam para ela e registram qualquer interpretação. | Hash/commit da fonte, diff e referências documentais. | Redação ou migração da fonte exige autorização explícita e preservação da revisão anterior. | Proprietário da fonte |
| PROC-012 | Executar o trabalho por gates: descoberta/requisitos, requisitos técnicos, arquitetura, desenvolvimento, QA e release; uma etapa só aprova a seguinte quando seu contrato estiver completo e suas pendências bloqueantes resolvidas ou formalmente aceitas. | Ciclo SDD | obrigatoria | Cada etapa registra entrada, saída, status, evidência, perguntas pendentes e aprovação aplicável. | Contratos/artefatos versionados e registro dos gates. | Projetos pequenos podem combinar etapas, sem eliminar responsabilidades, critérios ou evidências. | Governança do projeto |
| PROC-013 | Diferenciar validação estrutural, revisão semântica, teste técnico, homologação e validação em produção; nenhuma delas comprova automaticamente as demais. | Qualidade e comunicação de status | obrigatoria | Relatórios declaram o que foi executado, ambiente, resultado, limitações e o que permanece não verificado. | Logs, checklist, revisão humana e evidências por ambiente. | Etapa omitida deve ter motivo, impacto e aceite do dono do risco. | QA e responsável técnico |
| PROC-014 | Toda mudança deve atualizar, na mesma execução, as fontes e os artefatos afetados: requisitos, regras, arquitetura, diagramas, tarefas, testes, prontidão, aprovações e histórico. | Gestão de mudanças | obrigatoria | A análise de impacto identifica documentos afetados e o diff não deixa sínteses ou rastreabilidade divergentes. | Registro da mudança, diff, matriz atualizada e validações repetidas. | Se um artefato estiver inacessível, registrar sincronização pendente e não declarar a mudança concluída. | Responsável pela mudança |
| PROC-015 | Manter um único histórico canônico de mudanças do projeto, com entradas mais novas primeiro e versão, data/hora, solicitante quando informado, motivo, arquivos afetados, validações e pendências. | Governança documental | obrigatoria | O índice documental aponta para um único `CHANGELOG.md`, `HISTORICO_ALTERACOES.md` ou equivalente; não existem históricos concorrentes sem função distinta. | Histórico versionado e commits/diffs correspondentes. | Histórico regulatório ou de release separado é permitido quando sua responsabilidade for distinta e houver referência cruzada. | Responsável pelo projeto |
| PROC-016 | Registrar aprovação vinculada à revisão exata do artefato e preservar aprovações anteriores; mudança invalida apenas os itens afetados. | Aprovações e auditoria | obrigatoria | A evidência contém aprovador, papel/autoridade, data, decisão, versão/hash e escopo; revisões novas indicam aprovações preservadas ou invalidadas. | Ata, ticket, assinatura eletrônica ou registro corporativo acessível. | Aprovação verbal deve ser formalizada antes do gate que depende dela. | Governança do projeto |
| PROC-017 | Não incluir senha, token, credencial, chave privada ou dado pessoal real em PMO, SDD, código de exemplo, log ou evidência. | Segurança documental | obrigatoria | Revisão e varredura não encontram conteúdo proibido; exemplos usam valores fictícios identificados. | Resultado de varredura/revisão e política de acesso. | Não prevista para credenciais. Dado pessoal necessário à evidência deve ser minimizado, mascarado e armazenado em repositório autorizado. | Responsável por segurança e responsável pelos dados |
| PROC-018 | Preparar release somente após validação aplicável, com ambiente-alvo explícito, inventário de artefatos, dependências, ordem de execução, rollback/reversão, smoke test, responsáveis e evidências. | Release e implantação | obrigatoria | O plano de release está completo antes da execução e o resultado registra estado anterior/posterior e limitações. | Plano, aprovação, scripts, logs, smoke test e evidências. | Processo emergencial deve seguir a política corporativa própria e gerar regularização rastreável. | Responsável por release e Product Owner |
| PROC-019 | Tratar defeito, desvio e falha de validação conforme sua causa: correção formal segura pode ser refeita com limite; lacuna semântica, autorização, risco protegido ou falha externa deve voltar ao responsável adequado. | QA e recuperação do processo | obrigatoria | O registro distingue defeito do artefato, falta de informação, falha de ferramenta e decisão humana; repetição possui limite e condição de parada. | Log de tentativas, diagnóstico e encaminhamento. | Política de retry diferente deve documentar idempotência, custo, risco e limite. | QA e responsável pelo processo |
| PROC-020 | Selecionar documentos e profundidade de análise proporcionalmente ao risco e ao contexto, sem criar artefatos vazios apenas para cumprir lista. | Planejamento documental | recomendacao | Cada artefato existe por finalidade concreta; conteúdo obrigatório está coberto e documentos omitidos têm motivo. | Índice documental e justificativa de seleção. | O projeto pode exigir conjunto fixo por contrato, auditoria ou regulação. | Responsável pelo projeto |

## Base adotada

Esta proposta foi extraída de fontes do CS_Genesis `v9.4.0`. Os hashes identificam os bytes consultados, mas não substituem aprovação nem comprovam vigência para toda a empresa.

| Fonte | Uso nesta proposta | SHA-256 |
| --- | --- | --- |
| `CS_Genesis/CS_Genesis_Agents_Official/templates/FORMULARIO_PMO_CS_GENESIS.md` | Estrutura de intake PMO, IDs estáveis, regras de preenchimento, critérios, riscos e evidências. | `539CC61D48F69FC8F6F99F17837478A8FD1C1FC5837D09A4532A47BFAA92D8D7` |
| `CS_Genesis/referencias/decisions.md` | Gates, preservação de legado, governança de mudanças estruturais e documentação funcional. | `1D60E6BAA0D8440FED713105BC2FFB6A1AC526E854D84FAB65335FA70FAD36D8` |
| `CS_Genesis/referencias/task.md` | Critérios de revisão, rastreabilidade, QA e limites da evidência. | `EA5831F63AA1B0E15378DFCC32FF31ED9238A82F3A978F267DB19318B911BC05` |
| `CS_Genesis/referencias/deployment.md` | Processo de release, rollback, smoke test e evidências. | `ECDA8DF11E046293F1388C9791FBAB16DFFDE055C98790E53518D5D78E7B2982` |
| `CS_Genesis/HISTORICO_ALTERACOES_GENESIS.md` | Modelo de histórico canônico e versionamento de mudanças. | `D97032D15987F18754B445FB6C01E1619551BF63317B6CD22EDAD51176345058` |

Antes de publicar esta baseline, preencher `responsible`, `approval_evidence`, mudar `status` somente após aprovação real e registrar a revisão publicada. Projetos devem adotar a versão e o hash publicados em sua própria baseline; não devem copiar silenciosamente uma revisão mais nova.

## Conflitos e exceções

| ID | Regra/revisão | Impacto/escopo | Justificativa | Resolução proposta | Aprovador | Evidência | Validade | Controles compensatórios | Estado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EXC-PROC-001 | PROC-001 a PROC-020 / `0.1.0-proposta` | Publicação corporativa | Responsável e evidência de aprovação ainda não foram informados. | Submeter a proposta aos responsáveis de negócio, técnico, QA e governança; publicar nova versão após decisão. | Pendente | Pendente | Até a publicação aprovada | Tratar todas as regras como proposta e declarar conformidade corporativa como não confirmada. | pendente |

## Histórico

| Data | Versão | Origem e motivo | Alterações | Responsável | Aprovação |
| --- | --- | --- | --- | --- | --- |
| 2026-09-09 | `0.1.0-proposta` | Solicitação do usuário para criar regras gerais de processo aplicáveis aos SDDs, aproveitando práticas do CS_Genesis. | Consolidação inicial de 20 regras; inclusão explícita de entrada PMO, regras de negócio, rastreabilidade, changelog/histórico, QA e release; exclusão de contratos próprios de agentes autônomos. | Não informado | Pendente |
