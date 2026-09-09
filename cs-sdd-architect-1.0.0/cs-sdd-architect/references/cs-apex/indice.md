# Guideline CS Compusoftware para APEX e PL/SQL

Use esta referência quando o projeto mencionar CS Compusoftware, Projeto 4.0, migração Delphi para APEX, página APEX, módulo APEX ou PL/SQL de apoio a uma página APEX.

## Fonte e rastreabilidade

- Fonte fornecida pelo usuário: `guidelines-de-apex (1).md`.
- Snapshot preservado em [guidelines-de-apex.snapshot.md](source/guidelines-de-apex.snapshot.md).
- SHA-256 do snapshot: `974c0ad79b8639faac3fc043c4e1abe71d560b57235d0c64cde5b07c46b0171b`.
- Data de incorporação: `2026-09-09`.
- O arquivo não declara versão, responsável, status formal nem evidência de aprovação. O usuário o identificou como guideline corporativo completo; trate seu conteúdo como padrão fornecido para elaboração do SDD, mas mantenha a vigência formal como pendência quando ela for necessária para declarar conformidade ou preparar release.

Os IDs `CSAPEX-*` na [baseline corporativa de desenvolvimento](../../assets/templates/empresa-desenvolvimento.md) foram criados para rastreabilidade da skill; não constam no documento original. Essa baseline é a única fonte normativa interna; este índice e o snapshot servem apenas para consulta detalhada e proveniência.

## Como consultar

1. Aplique as regras `CSAPEX-*` da [baseline corporativa de desenvolvimento](../../assets/templates/empresa-desenvolvimento.md) em toda especificação de página ou módulo APEX da CS.
2. Consulte no snapshot os capítulos relacionados aos componentes realmente presentes. Use `rg -n '^# Título|termo' references/cs-apex/source/guidelines-de-apex.snapshot.md` para localizar detalhes, parâmetros e exemplos.
3. Registre no SDD o título consultado, o hash acima, a aplicabilidade e os critérios derivados. Não copie todo o guideline para o projeto.
4. Trate IDs de aplicações, páginas, owners, packages, procedures, plugins e exemplos como valores a confirmar no ambiente, salvo quando o contexto do projeto provar que o componente corporativo indicado está disponível.
5. O guideline referencia também materiais UI/UX, vídeos, DevTools, Wiki.js e documentação Oracle não incorporados. Quando a decisão depender deles, registre a fonte externa como pendência ou consulte-a com autorização e acesso.

## Roteiro temático do snapshot

| Necessidade do SDD | Capítulos a consultar |
| --- | --- |
| Segurança e autenticação | `Alçada`, `Alçada "Por Contexto"`, `Controle de Acesso`, `Validações Back-end (APEX)` |
| Nova aplicação ou página | `Introdução ao APEX`, `Criação de uma nova gestão / módulo`, `Novo Módulo`, `Nova Página`, `Nomenclatura`, `Page Groups Coloridos` |
| Persistência e PL/SQL | `DML DINÂMICO`, `Objetos`, `Packages`, `Triggers`, `Owner APEX`, `View para Item ou Página`, `Informações do Usuário para LOG` |
| Estado temporário | `Collections`, `CRUD Collection`, `Global State`, `Popular Collection sem Rodar a Query da Grid Novamente` |
| Consultas e filtros | `Filtro GEF`, `Filtros de Consulta`, `Filtros Funcionário`, `Multifiltro`, `Multi-Filtro / LOV com Botões`, `Objeto de Custo` |
| Grids e cards | `Cards`, `CS Advanced Grid`, `Interactive Grid`, `IG - Interactive Grids`, `Totalizadores - IG` |
| Modais e navegação | `Controle de Abas`, `Menu Lateral - Tree View`, `Diálogos`, `Modal`, `Retorno de Item de Página Modal`, `Menu Popup`, `Sidebar Buttons` |
| Arquivos e importações | `Arquivos e Imagens`, `Preview/Download de Arquivos`, `Importações EXCEL (.xlsx)`, `Padronização Layout Arquivo` |
| Fórmulas e edição | `Editor para Campo Fórmula`, `Auto Complete Monaco`, `Campo Fórmula na Grid` |
| Execução longa | `Fila de Execução`, `Relatórios - Print Server`, `Ativação da Engine BigPdf` |
| Internacionalização e ajuda | `Text Messages`, `Help/Artigos On-line` |
| Entrega | `Gerar Release APEX`, `Aplicativo por Time`, `Página por Cliente`, `Release` |

## Conteúdo que não vira regra geral

- `Nomenclatura` está marcado como **EM CONSTRUÇÃO**: use os exemplos como orientação e confirme antes de tratá-los como obrigação. Regras de alias, itens e grids declaradas em capítulos concluídos continuam aplicáveis.
- `pr_multifiltro` está marcado como **BUILDING**: não imponha a solução sem validar o caso e a disponibilidade da package.
- `Controle do Page Item (tab index) - depreciado` e `Navegação TAB por ENTER (Depreciado)` servem apenas para reconhecer legado; não os prescreva em página nova.
- Callback de confirmação, DML dinâmico e outras soluções descritas como específicas ou pontuais só se aplicam quando a limitação relatada existir.
- Código, owner, tabela, página, aplicação, sessão e URL de exemplo demonstram uso; não são valores do projeto atual.
