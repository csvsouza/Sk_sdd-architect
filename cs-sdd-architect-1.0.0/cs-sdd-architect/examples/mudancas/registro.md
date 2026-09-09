# Mudança documental na mesma execução — exercício fictício

Entrada de CHG-01: após aprovação do gestor, acrescentar revisão do operador antes do envio. Natureza: solicitação confirmada do exercício, sem aprovação humana ou implementação do negócio.

Execução: alterar REQ-02/T-02 e fontes técnicas afetadas; atualizar mapa funcional, engenharia, fluxograma, mapa mental, procedimento, estado, índice e histórico da visão geral; registrar versões/hashes reais das fixtures. IPC cai de 50 para 45 porque um item de peso 10 passou de parcial (0,5) para ausente (0). G1 preservada; G2 anterior invalidada no exercício. Recomendar revisão de autorização pelo risco da nova transição; modelo e custo continuam pendentes.

- [Antes](antes/visao-geral-projeto.md) e [depois](depois/visao-geral-projeto.md).
- [Diff da visão geral](visao-geral-projeto.md.diff) e [diff da fonte](spec.md.diff).
- [Resultado executado](resultado.json) e [impacto de aprovação fictício](approval-impact.json).

Proposta conflitante CHG-02: “dispensar autorização do operador” contraria a base fictícia; registrar proposta e impacto, manter versão aprovada e bloquear somente tarefa dependente. Nenhum enfraquecimento foi aplicado.

Sem impacto CHG-03: alteração apenas na forma de comunicação do exercício, sem modificar requisito/procedimento; registrar essa conclusão, sem reescrever fontes.

Falha de acesso executada nos testes CHANGE-02/03: fonte removida apenas em diretório temporário → sync pendente; acesso/base restaurados → hashes conferidos novamente. Em projeto real, falta de acesso exige registro local da pendência, não declaração de conclusão. O utilitário não faz recuperação semântica automaticamente.

Limite: exercício documental conduzido pelo autor e scripts de fixtures, não teste cego de comportamento de outro agente. Sem monitoramento em segundo plano ou implementação de negócio.
