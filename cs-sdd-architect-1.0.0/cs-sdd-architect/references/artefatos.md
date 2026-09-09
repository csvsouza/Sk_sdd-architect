# Seleção proporcional

Sempre produza `spec.md`, `projeto-regras.md` e `visao-geral-projeto.md`. Em projeto pequeno, `spec.md` pode conter produto, desenvolvimento, tarefas, testes, rastreabilidade, aprovações, IPC e estratégia. Os dois documentos corporativos continuam na fonte central ou em snapshots identificados, sem duplicação normativa.

Selecione por conteúdo real; registre no spec arquivos escolhidos/dispensados e justificativa. `select` oferece sugestão determinística, ajustável pelo agente com justificativa.

| Template | Quando separar |
| --- | --- |
| product.md | Jornadas, stakeholders ou backlog extensos |
| development.md | Organização do código e convenções próprias extensas |
| architecture.md | Múltiplos componentes ou trade-offs relevantes |
| database.md | Modelagem, transações ou migração substanciais |
| integrations.md | Contratos externos ou fronteiras de sistemas |
| security.md | Autorização, dados sensíveis ou ameaças que precisam revisão própria |
| testing.md | Múltiplas camadas, contratos ou cenários negativos |
| operations.md | Agendamento, implantação, suporte e retomada |
| tasks.md | Dependências suficientes para execução separada |
| decision.md → decisions/ADR-NNN.md | Decisão relevante com alternativas/consequências |
| approvals.md, readiness.md, execution-strategy.md | Registros extensos; caso contrário seções do spec |

Copie apenas templates aplicáveis, substitua orientações por conteúdo sustentado ou pendência explícita. Nunca crie documento opcional vazio. A fonte principal de uma informação deve ser única e referenciada na síntese. A visão geral tem todas as seções, podendo explicitar N/A justificado ou desconhecido.
