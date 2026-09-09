# Índice de Prontidão Contextual (IPC)

Completude e sustentação da especificação, não probabilidade de acerto, garantia de sucesso nem taxa de qualidade do modelo. Rubrica `ipc-1.0` proposta, não calibrada pela empresa. Itens observáveis em [rubrica](../assets/templates/readiness.json); fixe-os antes de pontuar e preserve versão entre comparações.

Dimensões/pesos: produto 15; escopo 20; governança 20; engenharia 15; verificação 20; segurança/operação 10. Cada dimensão tem dois itens de igual peso. Alteração de itens/pesos exige nova versão e base comparável explicitada.

Nota 0 = ausente/contraditório; 0,5 = parcial/hipótese não confirmada; 1 = suficiente/consistente com fonte identificada. Desconhecido fica 0 no denominador; N/A exige justificativa e sai do numerador/denominador. Nota positiva exige fonte; fonte não garante semântica. `IPC = 100 * soma(peso_item * nota) / soma(pesos aplicáveis)`. Sem itens aplicáveis: não calculável. Não redistribua peso N/A dentro da dimensão. Arredonde só exibição final (meio para cima).

Faixas propostas usando valor antes do arredondamento: <60 insuficiente; <80 parcial; <90 candidata à revisão; >=90 candidata à aprovação, sempre condicionada ao gate e bloqueios. O script não concede aprovação.

Em cada marco/mudança mostre itens, fontes, versão, IPC global e por dimensão, hipóteses/contradições, bloqueios, ações/perguntas prioritárias, etapa/status e delta/causa. Mudou rubrica? Não apresente delta direto como melhora. Prontidão para implementação também depende de escopo/exclusões, regras claras, aceites, contratos, controles, falhas, operação aplicável e consistência.

Assertividade observada, se disponível, é outra métrica: critérios aprovados na primeira revisão / avaliados, numerador, denominador, período, amostra e método. Sem histórico: não mensurada. Não converta IPC em taxa histórica.
