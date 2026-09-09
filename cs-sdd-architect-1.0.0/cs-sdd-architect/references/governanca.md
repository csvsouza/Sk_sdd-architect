# Herança corporativa

Configure `sdd-config.yaml` a partir do template. `corporate_root` aponta para uma pasta central versionada acessível (checkout, compartilhamento ou exportação autorizada). Caminhos relativos resolvem a partir da configuração. O utilitário não acessa rede nem faz checkout. O mantenedor publica revisões aprovadas; hash identifica bytes, não comprova aprovação ou vigência.

Leia integralmente `empresa-processos.md` e `empresa-desenvolvimento.md`, inclusive metadados, histórico e regras aplicáveis, antes de filtrar contexto para tarefas. Confirme com fonte de aprovação a revisão vigente em projetos novos. Leia `projeto-regras.md` existente; só pergunte o que falta. Registre adoção em `baseline.json` e em regras locais; snapshot em `regras/` é opcional. Mantenha links portáveis para snapshots autorizados quando houver consumidor externo à pasta central.

Base normativa: obrigações corporativas; depois detalhes locais compatíveis/mais rigorosos; recomendações adaptáveis com justificativa; por fim sugestões explicitamente propostas. Os dois documentos corporativos são complementares, sem desempate automático. Inspecione também conflitos entre eles e entre recomendações e obrigações. Não transforme campos nulos ou texto de orientação em regra aprovada.

Para cada regra registre ID, texto, escopo, classificação (`obrigatoria` ou `recomendacao`), conformidade, evidência, política de exceção e aprovador. Os templates não contêm regras fictícias. A matriz registra origem/revisão, aplicabilidade, requisito, componente/decisão, tarefa, teste, evidência e status. Use os sete estados do template de rastreabilidade. N/A exige justificativa; verificado exige evidência real ligada à revisão.

## Conflitos e exceções

Registre IDs e origens conflitantes, cláusulas, impacto e tarefas dependentes. Proponha compatibilidade (manter obrigação ou tornar regra local mais rigorosa). Bloqueie só decisões dependentes; avance no restante. Solicitação do usuário conflitante não comprova aprovação de exceção e não altera o padrão corporativo.

Exceção exige ID, regra/revisão, justificativa, escopo, aprovador autorizado, evidência acessível, validade, controles compensatórios e status. Examine validade e condições no momento de uso; evidência existente em disco não prova identidade/autoridade do aprovador. Exceção pendente ou expirada não autoriza enfraquecimento. Proponha melhorias corporativas em registro separado; adoção exige ação explícita versionada.

## Atualização e indisponibilidade

Projeto existente mantém sua base. Compare hashes/revisões atuais com os adotados e registre impacto antes de adotar. Não use atualização de hash para encobrir divergência. Registre decisão de adoção, responsável, evidência, data e revisões anterior/nova; reavalie só requisitos e aprovações afetados. Preserve a base anterior no histórico.

Se a central falhar, use apenas cópia correspondente ao hash e à revisão previamente registrada; exponha que vigência central não foi confirmada. Sem arquivo completo/versionado não declare conformidade, mas produza rascunho. Não reclassifique cópia desatualizada como vigente.
