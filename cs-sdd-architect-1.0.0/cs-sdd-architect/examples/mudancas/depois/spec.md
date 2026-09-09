# ESPECIFICAÇÃO FICTÍCIA — comportamento planejado

## Produto
Problema: envio sem controle de aprovação. MVP: solicitação, decisão de gestor e envio rastreável; excluir reprocessamento automático irrestrito e manual final. Priorizar autorização/estado antes de envio. Métrica: envios vinculados a aprovação, fonte futura do registro; meta pendente. Alternativa de envio direto rejeitada como proposta por contrariar necessidade de controle.

## Engenharia
APEX: interface e autorização; PL/SQL: transição de estado; Python: integração; serviço externo: destino. Versões, contrato e ferramentas pendentes. Nenhuma implementação executada. Autorização de gestor deve ocorrer no servidor.

## REQ-01
REQ-01: enviar somente solicitação aprovada por gestor autorizado. Aceite: solicitante não aprova a si sem regra explícita; rejeição não envia; timeout com resultado incerto entra em reconciliação, sem repetir POST automaticamente. Verificação proposta: acesso direto indevido, rejeição e falha após efeito remoto.
Origem: [entrada](entrada.md), FIC-P01/FIC-D01 revisão 1.0-ficticia e regras locais. Estado: previsto; evidência de negócio inexistente.

## Seleção proporcional
- spec.md: requisitos, abordagem, validações e registros compactos.
- projeto-regras.md: base adotada e regras locais.
- visao-geral-projeto.md: entrada documental obrigatória.
- architecture.md: fronteiras entre componentes.
- tasks.md: dependências entre componentes.
- testing.md: verificação entre componentes.
- database.md: persistência/transações afetadas.
- integrations.md: contratos entre sistemas.
- operations.md: execução recorrente e recuperação.
- security.md: risco alto exige revisão dedicada.
Demais registros permanecem em seções deste spec para evitar documentos vazios.

## T-01
Contexto: REQ-01, entrada.md, projeto-regras.md, base corporativa 1.0-ficticia. Dependência: confirmar ambiente/contratos pendentes. Limites: somente componentes descritos; preservar legado e proibir alterações corporativas. Conclusão: critérios de REQ-01 demonstrados. Validação proposta conforme REQ-01; comandos ainda não confirmados. Evidência esperada: registro de teste por revisão. Interromper parte dependente se contrato/autorização ausente ou efeito remoto incerto. Nenhum comando de negócio executado.

## Rastreabilidade
FIC-P01/FIC-D01@1.0-ficticia → REQ-01 → componente descrito em Engenharia → T-01 → teste de REQ-01. Estado previsto; não confundir evidência prevista com teste executado.

## Aprovações
G1/G2/G3 propostos; responsáveis a identificar; não submetido. G4/G5 especificados pelo ciclo da skill, sem liberação.

## Estratégia
Decisões transacionais/integração: avaliar candidato de capacidade compatível, separando rotina e revisão crítica. Catálogo ausente; identificador e esforço exatos não confirmados, custo não estimável. Teste representativo proposto com limite a acordar antes de consumo pago. Não remover teste negativo, regras ou aprovação. Troca não executada.

## IPC
Rubrica e notas em readiness.json, cálculo em ipc-result.json. Notas sustentam apenas contexto fictício; não são probabilidade de acerto nem aprovação.

## Erros e recuperação
Operador trata envio incerto com consulta autorizada ao destino; não reenvia até conclusão. Implantação e suporte pendentes; recuperação precisa respeitar estado remoto e local.

## CHG-01 — revisão 1.1
Solicitação fictícia confirmada nesta avaliação: após aprovação do gestor, operador deve revisar a solicitação antes do envio. REQ-02: revisão registrada é pré-condição para Python enviar. Aceite proposto: aprovação sem revisão não envia; revisão negativa retorna ao gestor. T-02 depende de T-01 e altera somente transição de envio e evidências correspondentes. Teste negativo adicional obrigatório; nenhum código foi implementado.
