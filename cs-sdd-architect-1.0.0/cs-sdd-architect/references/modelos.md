# Modelo e esforço por tarefa

Use [catálogo editável](../assets/templates/model-catalog.json), inicialmente vazio. Consulte documentação oficial vigente e disponibilidade do ambiente ao fazer recomendação concreta. Registre identificador exato, esforços suportados, capacidades necessárias, contexto, ferramentas, latência, fonte/data e restrições. Não preencha catálogo com nomes inferidos de exemplos.

Avalie complexidade (escopo, novidade, ambiguidade, componentes) separada de risco (dados, autorização, concorrência, reversibilidade, testes). Simples/baixo risco: avaliar primeiro candidato econômico e esforço baixo/médio suportado. Moderada: candidato intermediário com dependências claras. Crítica/ambígua: resolver lacunas e avaliar candidato mais capaz/esforço maior nos trechos necessários. Rotina em projeto complexo pode reutilizar candidato econômico já validado.

O exemplo GPT-5.6 Terra médio versus GPT-6 muito alto é hipótese do solicitante, não ranking, confirmação de identificadores, disponibilidade ou economia. Sem catálogo confirmado: modelo/esforço exatos nulos, recomendação condicional por perfil. Sem tarifa/medição: custo não estimável. Não alegue troca executada; ela exige ferramenta e autorização disponíveis.

Registre por tarefa: complexidade e fatos, risco e fatos, modelo/esforço candidatos, qualidade mínima, justificativa, evidência, limitações, faixa de tokens/custo e premissas, alternativa, gatilho de escalonamento e aprovação. Compare custo por entrega aceita incluindo revisão e retrabalho, não só token.

Sem histórico comparável, proponha avaliação representativa limitada: critérios, casos adversos se risco alto, limite de tentativas e consumo definidos antes de executar. Na ausência de orçamento autorizado, avaliação paga fica pendente; ainda elabore plano. Falha: diagnosticar contexto, ferramenta, especificação ou capacidade; corrigir causa antes de escalar. No limite, parar teste e recomendar decisão com motivo e custo adicional esperado (não estimável se faltarem dados). Não escale para compensar informação ausente.

API: calcular faixas por categoria faturada (entrada sem cache, entrada em cache, saída), somar ferramentas e encargos confirmados. Não contar raciocínio duas vezes se já faturado na saída. Considerar contexto reenviado, cache aplicável, revisão e retrabalho. Assinaturas têm limites/créditos próprios; não convertê-los em tarifas API. Fontes oficiais devem ser consultadas no momento, por exemplo a página de preços indicada pela solicitação, sem fixar valores aqui.

Economia: carregar perfis sob demanda após checar herança, reutilizar resumos versionados e decisões, editar trechos afetados, evitar perguntas repetidas e usar validadores. Não remover segurança, testes, evidências ou aprovações. Múltiplos agentes não são requisito de economia. Atualize recomendação quando mudar contexto, catálogo, escopo ou evidência. Não prometa percentual de economia sem comparação equivalente mensurada.
