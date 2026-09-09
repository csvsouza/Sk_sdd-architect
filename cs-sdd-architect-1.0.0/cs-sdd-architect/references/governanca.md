# Herança corporativa

As fontes corporativas canônicas desta skill são `assets/templates/empresa-processos.md` e `assets/templates/empresa-desenvolvimento.md`. Leia-as diretamente em toda execução e não gere, copie nem mantenha duplicatas delas dentro dos projetos. O projeto registra versão, origem e hash em `baseline.json`, `projeto-regras.md` e na visão geral. `corporate_root: null` usa automaticamente essas fontes incorporadas.

`corporate_root` só deve apontar para outra pasta quando o usuário fornecer explicitamente uma revisão corporativa substituta, completa e versionada. Caminhos relativos resolvem a partir de `sdd-config.yaml`. O utilitário não acessa rede nem faz checkout. Uma substituição não altera silenciosamente a baseline incorporada; compare hashes, registre a adoção e preserve a revisão anterior.

Leia integralmente as duas baselines, inclusive metadados, histórico e regras aplicáveis, antes de filtrar contexto para tarefas. Confirme com fonte de aprovação a revisão vigente quando o projeto precisar declarar conformidade. Leia `projeto-regras.md` existente; só pergunte o que falta. Não replique o texto normativo: registre a adoção por referência, versão e hash. Snapshot externo só é aceitável quando um consumidor não puder acessar a skill e deve preservar a origem.

Base normativa: obrigações corporativas; depois detalhes locais compatíveis/mais rigorosos; recomendações adaptáveis com justificativa; por fim sugestões explicitamente propostas. Os dois documentos corporativos são complementares, sem desempate automático. Inspecione também conflitos entre eles e entre recomendações e obrigações. Não transforme campos nulos ou texto de orientação em regra aprovada.

Para cada regra aplicável registre ID e revisão, aplicabilidade, requisito, componente/decisão, tarefa, teste, evidência e status. Não reproduza a descrição completa se o ID e a versão apontarem inequivocamente para a baseline. Use os sete estados do template de rastreabilidade. N/A exige justificativa; verificado exige evidência real ligada à revisão.

## Conflitos e exceções

Registre IDs e origens conflitantes, cláusulas, impacto e tarefas dependentes. Proponha compatibilidade (manter obrigação ou tornar regra local mais rigorosa). Bloqueie só decisões dependentes; avance no restante. Solicitação do usuário conflitante não comprova aprovação de exceção e não altera o padrão corporativo.

Exceção exige ID, regra/revisão, justificativa, escopo, aprovador autorizado, evidência acessível, validade, controles compensatórios e status. Examine validade e condições no momento de uso; evidência existente em disco não prova identidade/autoridade do aprovador. Exceção pendente ou expirada não autoriza enfraquecimento. Proponha melhorias corporativas em registro separado; adoção exige ação explícita versionada.

## Atualização e indisponibilidade

Projeto existente mantém sua base. Compare hashes/revisões atuais com os adotados e registre impacto antes de adotar. Não use atualização de hash para encobrir divergência. Registre decisão de adoção, responsável, evidência, data e revisões anterior/nova; reavalie só requisitos e aprovações afetados. Preserve a base anterior no histórico.

Se uma fonte externa configurada falhar, mantenha a revisão previamente adotada quando seu hash estiver acessível ou retorne explicitamente à baseline incorporada mediante decisão registrada. Sem arquivo completo/versionado não declare conformidade, mas produza rascunho. Não reclassifique cópia desatualizada como vigente.
