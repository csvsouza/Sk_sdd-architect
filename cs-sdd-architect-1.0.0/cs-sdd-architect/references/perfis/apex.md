# Oracle APEX

Quando o contexto for CS Compusoftware, Projeto 4.0 ou migração Delphi para APEX, aplique as regras `CSAPEX-*` da baseline [empresa-desenvolvimento.md](../../assets/templates/empresa-desenvolvimento.md) e use o [índice do guideline CS APEX](../cs-apex/indice.md) para consultar no snapshot somente os capítulos dos componentes presentes. Exemplos do guideline não autorizam inventar IDs, owners ou disponibilidade.

Confirme versão, aplicação existente, convenções e exportações disponíveis. Mapeie páginas, componentes compartilhados, navegação, estado de sessão, itens protegidos e validações no servidor. Não invente IDs de páginas, botões ou mensagens.

Especifique autenticação, autorização no servidor e isolamento de dados por perfil/tenant. Ocultar componente não basta: teste acesso direto e submissão indevida com perfis sem permissão. Trate escaping de saída, uploads, dados sensíveis e ciclo da sessão.

Distribua regras entre processos APEX e packages PL/SQL com responsabilidade explícita. Documente contratos ORDS apenas se houver integração confirmada. Exija exportação/versionamento, comparação e promoção entre ambientes conforme padrões reais. Testes: jornada válida, entrada inválida, sessão expirada, acesso direto não autorizado e isolamento. Recursos específicos exigem documentação Oracle da versão e evidência de disponibilidade.
