# Python

Confirme versão, entrada executável, dependências, configuração, sistema operacional e agendador. Descreva estrutura proporcional, conexão Oracle e fechamento de recursos, sem presumir bibliotecas instaladas.

Defina contratos de entrada/saída e erros; segredos fora de exemplos/logs, fonte de configuração aprovada, fronteira transacional e efeito de exceções. Em lote, descreva unidade de checkpoint, retomada, chave de idempotência e prevenção de concorrência/duplicação.

Integrações: timeouts, falhas permanentes/transitórias, orçamento de retries e parada. Resultado remoto incerto não autoriza repetir POST; exigir reconciliação ou chave idempotente comprovada. Sucesso HTTP não substitui verificação do corpo quando o contrato admite erro lógico.

Observabilidade: logs redigidos, correlação, métricas e alertas com destinatário a confirmar. Defina agendamento, empacotamento, implantação e recuperação conforme ambiente. Testes: conexão indisponível, timeout após efeito remoto, duplicação, queda após checkpoint, falha parcial e recurso fechado. Distinguir mocks de integração real. Consulte documentação oficial da versão para recursos usados.
