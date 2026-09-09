# ESPECIFICAÇÃO FICTÍCIA — comportamento planejado

## Produto
Problema: redigitação de lotes. MVP: validar lote e persistir dados, excluindo interface web e postagem externa. Priorizar integridade antes de agendamento, pois duplicação compromete valor. Métrica: lotes sem redigitação por período, fonte futura de execução; meta pendente. Alternativa de macro descartada como proposta por dificultar retomada auditável.

## Engenharia
Python e Oracle/PLSQL confirmados sem versões. Dois componentes: leitor/validador Python e persistência Oracle. Contrato e chave de unicidade precisam confirmação antes de implementação. Transação proposta por lote; COMMIT sob responsabilidade do coordenador a confirmar, sem criar package real.

## REQ-01
REQ-01: importar lote validado uma única vez. Aceite proposto: lote inválido não persiste; reapresentação da mesma chave não duplica; queda após commit é reconciliada antes de nova gravação. Verificação proposta: injetar falha antes/depois do commit e consultar o estado durável.
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
Agendador e credenciais pendentes. Retomada lê checkpoint; lote incerto requer reconciliação. Logs não contêm conteúdo sensível do arquivo; métricas de conclusão/falha e responsável por alerta a confirmar.
