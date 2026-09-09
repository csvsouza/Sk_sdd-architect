# Utilitários locais

Python com PyYAML conforme requirements.txt. Execute a partir de qualquer diretório passando caminhos explícitos. Os comandos leem arquivos locais e não fazem chamadas externas.

```powershell
python cs-sdd-architect/scripts/sdd.py rules projeto/sdd-config.yaml
python cs-sdd-architect/scripts/sdd.py rules projeto/sdd-config.yaml --baseline projeto/baseline.json
python cs-sdd-architect/scripts/sdd.py select projeto/context.json
python cs-sdd-architect/scripts/sdd.py ipc projeto/readiness.json
python cs-sdd-architect/scripts/sdd.py records projeto/traceability.json
python cs-sdd-architect/scripts/sdd.py render projeto/overview-input.yaml projeto/visao-geral-projeto.md
python cs-sdd-architect/scripts/sdd.py check projeto/visao-geral-projeto.md
```

`rules`: lê metadados/conteúdo das duas fontes, identifica incompletude, compara base e aceita fallback somente com hash adotado correspondente. Saída não substitui leitura semântica pelo agente e não grava/adota base. Após confirmar vigência/aprovação em projeto novo, registre sources em baseline.json; projeto existente exige análise e adoção explícita primeiro.

`select`: sugestão proporcional por components (inteiro), data_change/integration/operation (booleanos), risk (baixo/moderado/alto). O agente pode ajustar com justificativa e deve preencher conteúdo concreto.

`ipc`: valida rubrica fixa/IDs/notas/N/A/fontes e calcula global/por dimensão. `records`: verifica IDs de registros, metadados, estados, exceções e aprovações; existência de evidência não comprova conteúdo/autoria. Use matriz Markdown junto ao registro JSON, mantendo JSON como fonte dos estados se o adotar.

`render`: entrada metadata + sections (nomes exatos do template); cria somente destino inexistente. Falta de seção vira pendência. `check`: contrato, seções, links de arquivo, hashes, presença Mermaid e prontidão básica. Não verifica âncoras, links remotos, sintaxe Mermaid, semântica nem aprovação humana.

Códigos: 0 = checagens locais sem erros reportados; 1 = inconsistências/lacunas/drift; 2 = entrada/comando inválido ou acesso falho. Nenhum significa conformidade completa. Os comandos check/rules/ipc/records/select não alteram arquivos; render recusa sobrescrita.

Avaliações reproduzíveis do pacote: ver pasta validation na entrega, fora do diretório da skill. Não é necessário instalar testes para usar a skill.
