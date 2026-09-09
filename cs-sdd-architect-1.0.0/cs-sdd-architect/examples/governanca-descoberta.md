# Exercícios semânticos — dados inteiramente fictícios

Método: leitura das entradas e aplicação das referências da skill pelo autor nesta execução, com decisões abaixo registradas. Não houve entrevista com usuários reais nem teste cego por outro agente. Os testes automatizados verificam invariantes, não a capacidade geral de detectar conflitos em linguagem natural.

## Descoberta nos três cenários

| Entrada inspecionada | Informação reutilizada, sem perguntar de novo | Pergunta produzida / estado |
| --- | --- | --- |
| apex-pequeno/entrada.md | APEX existente, atendentes, filtro, nenhuma regra adicional | Qual exportação/convenção e versão estão disponíveis para confirmar a alteração? Pendente; não inventar página. |
| python-oracle/entrada.md e projeto-regras.md | Python, Oracle, lote e L-FIC01 já existente | Qual chave identifica o lote e quem coordena a transação? Bloqueia contrato de persistência. |
| sistema-integrado/entrada.md | APEX, PL/SQL, Python, serviço, gestor e operador | Há regras locais, referências ou exceções aprovadas? Qual contrato remoto e autorização por perfil? Pendente; silêncio não vira ausência. |
| Escopo ambíguo: “quero um dashboard melhor” | Pedido de solução, sem problema/público | Qual decisão o público precisa tomar e qual resultado atual está insuficiente? Não presumir gráficos, MVP ou metas. |

Histórico: material existente lido → fatos acima registrados → perguntas limitadas ao que altera decisão → exemplos gerados como rascunho. Não simular resposta às perguntas pendentes. Versões permanecem ausentes nos três exemplos; não recomendar recurso dependente de versão.

## Oito cenários de governança

| Caso e entrada fictícia | Aplicação da skill nesta avaliação | Evidência / limite |
| --- | --- | --- |
| 1. Não há regras locais adicionais | Registrar declaração e herdar ambas as fontes | apex-pequeno/projeto-regras.md e baseline.json; hashes reais de fixtures |
| 2. L-FIC01 exige checkpoint por lote | Mais rigorosa e compatível com base; incluir verificação de retomada | python-oracle/projeto-regras.md e spec.md |
| 3. L-FIC02 pede “autorizar só ocultando botão” contra FIC-D01 | Conflito: origem local versus empresa-desenvolvimento@1.0-ficticia; risco acesso direto. Propor autorização no servidor. Bloquear somente tarefa de autorização, avançar restante. Exceção sem evidência não aplicada | Decisão registrada aqui; inspeção semântica, não detector automático |
| 4. EX-FIC01 com regra/revisão, justificativa, escopo, aprovador, evidência, validade e controles | Aceitar apenas estrutura completa e vigência; verificar autoridade/conteúdo antes de aceitar exceção real | EX-01/02/03 em validation/results.json; evidência simulada só nas fixtures, não aprovação real |
| 5. Processo FIC-P02 exige log integral; desenvolvimento FIC-D02 proíbe dado sensível em log | Fontes complementares conflitam; nenhum desempate automático. Propor log redigido com correlação e pedir decisão sobre interpretação. Bloquear apenas desenho de log dependente | Revisão semântica registrada; não alterar nenhuma fonte central |
| 6. Central passa de 1.0 para conteúdo novo | Hash divergente sinaliza impacto; base anterior mantida. Adoção exige decisão documentada, análise de tarefas e aprovações | GOV-05 verifica detecção sem mutação. Adoção humana real não executada |
| 7. Central indisponível com cópia versionada | Usar somente cópia que coincide com base adotada; registrar vigência central não confirmada | GOV-03/04 verificam fallback e rejeitam cópia não adotada |
| 8. Ausente/incompleto | Rascunho, conformidade não declarada; preencher fontes/responsáveis/versão é pendência | GOV-02/06 executados |

## Adoção explícita simulada, sem alteração corporativa real

Entrada adicional fictícia: “O responsável fictício aprovou adoção da revisão 1.1 do padrão após avaliação de impacto”. AD-FIC01 foi materializada em [decisão](governanca-adocao/decisao.json), com aprovador fictício, data da avaliação, impacto em REQ-01, evidência simulada e base anterior/nova. Os bytes da revisão 1.1 e os hashes são reais das fixtures. GOV-07 confere que a base adotada corresponde à revisão disponível e que a anterior foi preservada. Isso é adoção executada no exercício, não aprovação ou alteração de norma corporativa real.

## Aprovações

Pendente: G1–G3 dos projetos ficam não submetidos; responsável real ausente. Aprovado: fixtures estruturais APR-02/EX-01 usam evidência fictícia acessível e todos os campos; o validador não autentica pessoa. Após mudança: snapshots em mudancas/ preservam G1 e invalidam G2 apenas no exercício. Critérios da especificação não são evidência de execução ou liberação G4/G5.
