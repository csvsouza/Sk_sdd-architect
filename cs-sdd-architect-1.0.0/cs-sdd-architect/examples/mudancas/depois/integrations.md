# EXEMPLO FICTÍCIO

APEX/PLSQL → fila lógica a especificar → Python → serviço. Contrato remoto, autenticação, chave idempotente, timeout e limites pendentes. Resultado incerto bloqueia retry até reconciliação.

Origem: [REQ-01](spec.md). Estado previsto.

## CHG-01 — revisão 1.1
REQ-02: Python só recebe solicitação com revisão positiva registrada; aprovação isolada não permite envio.
