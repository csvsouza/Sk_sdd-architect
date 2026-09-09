# Contrato documental 1.0

O produtor é a skill SDD; o consumidor futuro lê `visao-geral-projeto.md` e as fontes necessárias. Não depende da conversa e não constitui uma skill de manuais. YAML seguro no início do Markdown; sem tags executáveis, sem chaves duplicadas. Formato 1.0 independente das versões do projeto/documento. Mudança incompatível exige nova versão de contrato e migração explícita; consumidores devem rejeitar versões desconhecidas.

| Campo obrigatório | Tipo/valores |
| --- | --- |
| schema_version | string fixa "1.0" |
| project_id, project_name | string ou null se identificação desconhecida; IDs de projeto nunca inventados |
| document_version | string de revisão ou null no template |
| updated_at | string ISO YYYY-MM-DD ou null; data da atualização real, não aprovação |
| responsible | string ou null |
| project_phase | string do processo adotado ou null |
| intended_audiences | lista de strings |
| source_baseline | lista de objetos path (relativo à raiz documental), revision (string/null), sha256 (64 hex/null) |
| corporate_rules_baseline | exatamente dois objetos name, origin, revision, sha256, path; um para cada arquivo corporativo; valores desconhecidos null |
| documentation_readiness | pendente, parcial, pronto_para_revisao |
| known_gaps | lista de strings com lacunas ou referência à seção |
| outputs | lista de objetos type, audience, status, sources, evidence, gaps |

`origin` corporativa é string/null e pode ser URI da fonte central. `path` é snapshot relativo/null; se não nulo também consta em source_baseline. `revision` é versão/commit identificável e hash representa bytes reais; hash não autentica aprovação. Fontes corporativas ausentes continuam explicitadas com null. Links de consumo locais ficam dentro da raiz documental, sem caminhos de sessão. Se fonte central não for portátil, disponibilize snapshot permitido com origem preservada; nunca copie conteúdo restrito sem autorização.

Em outputs: type string (apresentacao_conceitual, manual_validado, guia_administrativo, guia_tecnico, treinamento, documentacao_operacional); audience string; status usa os mesmos três valores; sources/evidence/gaps são listas de strings. Não confunda pronto para revisão com publicação/aprovação. Manual validado exige evidência da execução real por perfil; conceitos podem estar prontos antes disso.

Todas as 14 seções do template devem ser consideradas. Texto ausente vira pendência; N/A tem justificativa. Funcionalidade: ID estável, fonte, estado (planejado, implementado, verificado, descontinuado), evidência/revisão quando realizada. Procedimento: ID, objetivo, público, pré-condições, passos conhecidos, resultado, exceções, fonte e estado de validação. Sem interface confirmada não invente tela/comando/botão. Registre material a coletar.

## Diagramas e atualização

Inclua fluxograma do negócio (início, atividades, decisões/resultados, erros conhecidos) e mindmap do projeto. Se contexto insuficiente, represente lacuna explícita e marque proposto. Cada bloco tem identificação do processo, fontes e equivalente textual. Mapa mental contempla produto, usuários, módulos, dados, integrações, regras e operação conforme aplicabilidade. Fluxo de aprovação do desenvolvimento, se útil, é outro diagrama identificado; não misture com o negócio.

Na mudança revise fontes primeiro, diagramas e textos depois; atualize versões/hashes somente após reconciliar conteúdo. Preserve histórico. Validadores detectam base antiga/ausente, mas não descobrem se a redação está correta. Execute renderizador Mermaid disponível; sem ferramenta registre sintaxe/renderização não verificadas. Não considere regex prova de sintaxe Mermaid.

`render` transforma seções já elaboradas pelo agente no arquivo com YAML; não inventa conteúdo nem sobrescreve arquivo. Para mudanças, edite o existente preservando histórico e rode `check`. O template editável também permite redação direta. Compare estado por público, classificação de acesso e evidências antes de entregar ao consumidor.
