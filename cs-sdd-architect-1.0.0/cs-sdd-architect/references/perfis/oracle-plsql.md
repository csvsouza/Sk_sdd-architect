# Oracle Database e PL/SQL

Confirme versão/edição/restrições, schemas reais, privilégios e ferramentas antes de definir recursos. Consulte documentação Oracle da versão confirmada quando necessário, registrando fonte.

Especifique entidades, chaves, integridade, constraints, consultas e volumes. Justifique índices ou particionamento por consultas e evidências; não proponha otimização apenas pelo nome de uma coluna. Registre evolução de schema e compatibilidade com consumidores.

Preserve assinaturas e estrutura legada fornecidas. Identifique package responsável pelas regras, entradas/saídas, tipos, nulos, códigos de erro e direitos de execução. Nunca invente owner, grant, wrapper ou COMMIT. Defina quem controla COMMIT/ROLLBACK e a unidade atômica; em falha parcial, explicite persistência, retomada e compensação.

Analise bloqueios, concorrência e consistência com cenários de duas sessões. SQL dinâmico: parâmetros vinculados para valores quando aplicável; identificadores requerem validação/allowlist e não se tornam seguros por bind. Defina menor privilégio e contexto de execução com fonte do ambiente.

Migração exige pré-condições, compatibilidade, dados afetados e recuperação realista. DDL e perda de dados não têm rollback presumido. Testes propostos: integridade inválida, concorrência, falha intermediária, contrato de erro e recuperação. Escolha ferramenta somente após confirmação; compilação e execução no Oracle são evidências distintas de inspeção estática.
