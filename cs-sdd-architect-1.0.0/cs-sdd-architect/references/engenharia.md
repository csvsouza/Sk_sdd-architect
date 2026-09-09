# Engenharia de software

Vincule cada componente a um requisito e ao resultado de negócio. Compare solução mínima, adaptação do legado e alternativa relevante por testabilidade, manutenção, evolução, dependências, custo operacional e risco. Registre decisão e consequências; não prescreva arquitetura distribuída sem necessidade demonstrada.

Requisito: ID estável, origem/revisão, descrição, limites, dados, fluxo principal, exceções, aceite mensurável e verificação proposta. Use Given/When/Then quando esclarecer. Descreva unidade/condições de medidas não funcionais; não crie metas ausentes.

Defina fronteiras de responsabilidade, contrato de dados e erros, compatibilidade, transações, concorrência e recuperação. Identifique dependências não confirmadas e evidências necessárias antes de execução. Separe validação do valor (o resultado atende ao negócio?) da verificação técnica (o contrato é cumprido?).

Na revisão, percorra requisito → decisão ou componente → tarefa → teste; depois percorra inversamente para encontrar trabalho sem propósito e regra sem cobertura. Mudança não deve remover sem análise critérios, testes ou evidências antigas; marque obsoletos com motivo/revisão.
