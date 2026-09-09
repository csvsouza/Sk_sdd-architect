# ESPECIFICAÇÃO FICTÍCIA — comportamento planejado

## Produto
Problema: atendentes têm dificuldade de localizar pedidos por situação. MVP: filtrar a consulta existente; excluir alterações de cadastro. Prioridade alta pelo valor de localização, esforço relativo pequeno e dependência da consulta atual. Indicador: tempo de localização por tarefa; baseline e meta pendentes. Alternativa de nova página descartada como proposta por duplicar manutenção.

## Engenharia
APEX confirmado, versão pendente. Reutilizar consulta e convenções existentes após inspecionar exportação. Nenhuma migração ou integração nova. Autorização existente preservada e testada no servidor, sem inventar IDs de página.

## REQ-01
REQ-01: permitir consultar pedidos por situação autorizada. Aceite: situação selecionada restringe resultados; seleção sem correspondência retorna lista vazia; acesso sem permissão continua negado no servidor. Verificação proposta: comparar resultados e testar acesso direto por perfil em ambiente de teste.
Origem: [entrada](entrada.md), FIC-P01/FIC-D01 revisão 1.0-ficticia e regras locais. Estado: previsto; evidência de negócio inexistente.

## Seleção proporcional
- spec.md: requisitos, abordagem, validações e registros compactos.
- projeto-regras.md: base adotada e regras locais.
- visao-geral-projeto.md: entrada documental obrigatória.
Demais registros permanecem em seções deste spec para evitar documentos vazios.

## T-01
Contexto: REQ-01, entrada.md, projeto-regras.md, base corporativa 1.0-ficticia. Dependência: confirmar ambiente/contratos pendentes. Limites: somente componentes descritos; preservar legado e proibir alterações corporativas. Conclusão: critérios de REQ-01 demonstrados. Validação proposta conforme REQ-01; comandos ainda não confirmados. Evidência esperada: registro de teste por revisão. Interromper parte dependente se contrato/autorização ausente ou efeito remoto incerto. Nenhum comando de negócio executado.

## Rastreabilidade
FIC-P01/FIC-D01@1.0-ficticia → REQ-01 → componente descrito em Engenharia → T-01 → teste de REQ-01. Estado previsto; não confundir evidência prevista com teste executado.

## Aprovações
G1/G2/G3 propostos; responsáveis a identificar; não submetido. G4/G5 especificados pelo ciclo da skill, sem liberação.

## Estratégia
Tarefa simples/baixo risco: avaliar candidato econômico e esforço baixo/médio suportado. Catálogo ausente; identificador e esforço exatos não confirmados, custo não estimável. Teste representativo proposto com limite a acordar antes de consumo pago. Não remover teste negativo, regras ou aprovação. Troca não executada.

## IPC
Rubrica e notas em readiness.json, cálculo em ipc-result.json. Notas sustentam apenas contexto fictício; não são probabilidade de acerto nem aprovação.

## Erros e recuperação
Falha de consulta: não apresentar dados de outro perfil; diagnóstico permitido e mensagem final pendentes do padrão real; testar ausência de permissão e entrada inválida. Consulta somente leitura não exige desfazer gravação.
