# EXEMPLO FICTÍCIO

REQ-01: enviar somente solicitação aprovada por gestor autorizado. Aceite: solicitante não aprova a si sem regra explícita; rejeição não envia; timeout com resultado incerto entra em reconciliação, sem repetir POST automaticamente. Verificação proposta: acesso direto indevido, rejeição e falha após efeito remoto. Testes de negócio não executados. Evidência esperada: logs redigidos, resultados por revisão e perfil, sem dados reais nesta avaliação.

Origem: [REQ-01](spec.md). Estado previsto.

## CHG-01 — revisão 1.1
REQ-02: testar aprovação sem revisão (não envia), revisão negada (retorna ao gestor), revisão positiva autorizada (habilita envio). Testes propostos, não executados.
