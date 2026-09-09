# Exercício de consumo e estados — dados fictícios

Fonte bruta fictícia fornecida ao exercício: “FUN-F01 está planejada. FUN-F02 possui alteração de código no arquivo fictício commit-F02, mas nenhum teste. FUN-F03 tem implementação e relatório fictício TEST-F03. Procedimento confirmado pelo material fictício: operador recebe lote, confere a identificação e encaminha ao responsável se identificação ausente. A interface de submissão ainda não foi fornecida.” Nenhum desses sistemas foi implementado ou testado nesta entrega.

| Funcionalidade | Estado a representar | Sustentação da fixture |
| --- | --- | --- |
| FUN-F01 | planejado | requisito fornecido; nenhuma implementação |
| FUN-F02 | implementado, não verificado | declaração de commit fictício; teste ausente |
| FUN-F03 | verificado segundo evidência fornecida na fixture | relatório fictício; não alegar teste executado pelo agente |

PROC-F01: objetivo conferir identificação de lote; público operador; pré-condição lote recebido e acesso permitido; passos conhecidos receber/conferir; resultado identificação conferida; exceção identificação ausente encaminha ao responsável; fonte texto fictício acima; validação documental confirmada na fixture, execução real não verificada.

PROC-F02: objetivo submeter lote; público operador; pré-condição e interface pendentes; passos não fornecidos; resultado esperado na especificação; exceções técnicas pendentes; estado não validado. Coletar interface, permissões e evidência de execução antes de manual.

Prontidão: apresentação conceitual pode seguir para revisão com requisito e arquitetura; manual validado permanece pendente de execução por perfil. Guia administrativo depende de configuração e suporte; guia técnico depende de contratos; treinamento pode usar conceitos identificados como planejados. Nenhuma dessas saídas foi implementada pela futura skill nesta entrega.

Consumo portátil executado nesta avaliação: partir somente de examples/python-oracle/visao-geral-projeto.md, ler o YAML e seguir source_baseline até spec.md, entrada.md, regras locais e snapshots corporativos, conferindo os hashes pelo comando check. Os arquivos e índice permitiram localizar o contexto sem recorrer à conversa. Isso demonstra a navegação do contrato; execução de uma futura skill independente não foi realizada.
