# Oracle Database e PL/SQL

Quando o PL/SQL sustentar página APEX da CS Compusoftware, aplique também `CSAPEX-011`, `CSAPEX-020` a `CSAPEX-026` e, quando houver collections, `CSAPEX-032` a `CSAPEX-034`, todos na baseline [empresa-desenvolvimento.md](../../assets/templates/empresa-desenvolvimento.md). Consulte o [índice do guideline CS APEX](../cs-apex/indice.md) apenas para detalhes. Preserve a separação entre regra corporativa fornecida, exemplo do guideline e objeto confirmado no schema atual.

Confirme versão/edição/restrições, schemas reais, privilégios e ferramentas antes de definir recursos. Consulte documentação Oracle da versão confirmada quando necessário, registrando fonte.

Especifique entidades, chaves, integridade, constraints, consultas e volumes. Justifique índices ou particionamento por consultas e evidências; não proponha otimização apenas pelo nome de uma coluna. Registre evolução de schema e compatibilidade com consumidores.

Preserve assinaturas e estrutura legada fornecidas. Identifique package responsável pelas regras, entradas/saídas, tipos, nulos, códigos de erro e direitos de execução. Nunca invente owner, grant, wrapper ou COMMIT. Defina quem controla COMMIT/ROLLBACK e a unidade atômica; em falha parcial, explicite persistência, retomada e compensação.

Analise bloqueios, concorrência e consistência com cenários de duas sessões. SQL dinâmico: parâmetros vinculados para valores quando aplicável; identificadores requerem validação/allowlist e não se tornam seguros por bind. Defina menor privilégio e contexto de execução com fonte do ambiente.

Migração exige pré-condições, compatibilidade, dados afetados e recuperação realista. DDL e perda de dados não têm rollback presumido. Testes propostos: integridade inválida, concorrência, falha intermediária, contrato de erro e recuperação. Escolha ferramenta somente após confirmação; compilação e execução no Oracle são evidências distintas de inspeção estática.
