# Guidelines de APEX

# Alçada

# Alçada

Para adicionar o controle de acesso/autenticação por páginas (alçada) em uma página do APEX, basta cadastrar sua página no cadastro de [Alçadas](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-seguranca/alcadas) do Segurança (Segurança &gt; Manutenções &gt; Alçadas), como segue:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/wZDimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/wZDimage.png)

Lembrando sempre de validar se a página esta marcada para **"Solicitar Senha"**:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/MMwimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/MMwimage.png)

#### **Dependência**

---

Verificar se a aplicação possui os itens:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/jBFimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/jBFimage.png)

Que são computados no "*After Footer*" das páginas:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/28Rimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/28Rimage.png)

# Alçada "Por Contexto"

Alçada por contexto é utilizada quando temos um conjunto de páginas que pertencem ao mesmo **"grupo de autenticação"**, de forma que ao navegar entre elas, não seja solicitada confirmação de identidade em cada mudança entre página.

O melhor exemplo, para que possamos entender esse "contexto", é o de um Wizard. Uma vez que acessei um Wizard e ele solicitou confirmação de identidade na primeira página, ao navegar nas demais páginas do wizard, bem como, voltar à primeira página, não será solicitada a confirmação de identidade novamente, pois elas pertencem ao mesmo contexto.

#### **Como Implementar?**

---

Partido do ponto que a alçada já esta implementada nas páginas, com base no *guide* [Alçada | Compusoftware](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/alcada), basta **adicionar** o Atributo `contexto_alcada` ao Help da página com o código da página de origem / mãe do contexto.

##### **Exemplo**

Temos um wizard com 4 páginas, onde a página "inicial" do wizard é a página 10 sendo as demais páginas 11, 12, 13.

No help text das páginas 11, 12 e 13 **adicionamos** **o `contexto_alcada`** apontando para onde o processo inicia, no caso, a página 10:

```
contexto_alcada: 10;
```

**Página de exemplo:** 40101:640

# Alert Message para Exclusão

Para implementar um Alert Message que irá disparar ao pressionar o botão de Excluir da Interactive Grid, será utilizado o seguinte código JS:

Esse código será uma **Dynamic Action no Page Load ➝ Execute JavaScript Code**

```
$('#ig-item-beneficio_ig_toolbar_btn-excluir').click((event) => {
  event.preventDefault();
  event.stopPropagation();

  apex.message.confirm(apex.lang.getMessage('LBL_EXCLUIR_ITEM_BENEFICIO'), function (confirmado) {
    if (confirmado) apex.region('ig-item-beneficio').widget().interactiveGrid('getActions').invoke('selection-delete');
  });
});
```

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/5p5image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/5p5image.png)

1. Dê um Static ID para a sua Interactive Grid
2. No print, onde está escrito **`ig-item-beneficio` ➝ substituir pelo ID da sua grid**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/OjAimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/OjAimage.png)

Dentro de `apex.message.confirm()` , colocar a função de Text Message ➝ `apex.lang.getMessage()` , que também está nos nossos Helps.

# APEX Code Editor

Configuração Padrão do Editor de Código do APEX.

- Tab Inserts Spaces
- Tab Size = 2
- Indent Size = 2

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/zvNimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/zvNimage.png)

# Arquivos e Imagens

# Anexar Arquivos

<p class="callout warning">**ATENÇÃO:** Verifique se na sua tabela já existe o campo **BLOB**, o campo **FILENAME** e o campo **MIMETYPE.**  
Também verifique **qual a Package da tela** para criarmos a procedure de deletar o arquivo.</p>

Algumas telas do sistema é necessário fazer a importação de arquivos, para isso faremos a seguinte lógica, um link para acessar uma modal que servirá para anexar e também para visualizar o arquivo já anexado.

#### **Criando o Link**

---

Na SQL da grid, adicionaremos o link e a lógica para o link

```pl/sql
     , ''link
     , case when coluna_blob is not null then 't-Button--success'
            else 't-Button--warning'
       end button_css
     , case when coluna_blob is null then 'fa fa-upload'
            else 'fa fa-check'
       end button_icon
     , case when coluna_blob is not null then apex_lang.message('LBL_ARQUIVO_ANEXADO')
            else apex_lang.message('LBL_ANEXAR_ARQUIVO')
       end button_hint
```

<p class="callout info">**👀 Obs.:** Crie uma Text Message (link) para a mensagem ser **traduzida para outros idiomas.**</p>

<table border="1" id="bkmrk-lembrando-que-essa-t" style="border-collapse: collapse; width: 100%; height: 119.188px;"><colgroup><col style="width: 50.0596%;"></col><col style="width: 50.0596%;"></col></colgroup><tbody><tr style="height: 29.7969px;"><td rowspan="4" style="height: 29.7969px;">[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/YAnimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/YAnimage.png)  
</td><td rowspan="4" style="height: 29.7969px;">- Lembrando que essa tela em específico **possui duas colunas de arquivos**, por isso a duplicidade dos itens.
- Todos serão "**Query Only**".
- Exceto pelo **Link** que é um *<u>Link</u>*, todas essas colunas criadas colocaremos como **Hidden.**

</td></tr><tr style="height: 29.7969px;"></tr><tr style="height: 29.7969px;"></tr><tr style="height: 29.7969px;"></tr></tbody></table>

O link receberá o seguinte **Link Text**:

- Passaremos o ID pelo Link

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/x5gimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/x5gimage.png)

```html
<span class="t-Button t-Button--icon t-Button--stretch &BUTTON_CSS."><span class="t-Icon t-Icon--left &BUTTON_ICON."></span> &BUTTON_HINT.</span>
```

Agora na tela modal, criaremos uma region **Form**.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/fyhimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/fyhimage.png)

A SQL será:

```sql
select id_proctpproc 
     , descricao 
     , modelo_procuracao 
     , modelo_revogacao 
     , modelo_procuracao_tipo 
     , modelo_revogacao_tipo 
     , modelo_procuracao_nome 
     , modelo_revogacao_nome
     , case when :P41_MODELO = 'P' then modelo_procuracao_nome
            when :P41_MODELO = 'R' then modelo_revogacao_nome
       end arquivo_nome
from   proc_tipoprocuracao
```

<p class="callout info">💡 Lembrando que **nesse exemplo tudo está duplicado!**</p>

#### **File Browse**

---

O **File Browse** servirá para colocarmos na coluna BLOB e recebermos o arquivo.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/oGgimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/oGgimage.png)

Configuraremos o File Browse da seguinte maneira:

```
Dowload(&"suacolunanome".)
```

1. Colocaremos o **Display As** como *Inline File Browse* para ficar apenas uma linha input de arquivo
2. O **Dropzone Title** seria o *placeholder* do input
3. O **Storage Type** será *BLOB column specified in Item Source Attribute* para salvar o arquivo na coluna
4. Em **MIME Type Column** será a coluna "Tipo" de sua tabela
5. Em **Filename Column** será a coluna "Nome" de sua tabela
6. Devemos ativar a opção de **Display Dowload Link**, para o usuário ter a opção de baixar o arquivo e o **Dowload Link Text** será como: ```
    Dowload(&"suacolunanome".)
    ```
7. O *Tipo* será o **mime type** do arquivo(extensão).
8. O *Nome* será o **Nome** do arquivo de fato.

<p class="callout info">👀 Precisaremos **das colunas acima na tabela** para recriarmos o layout corretamente.</p>

#### **Display Image**

---

O **Display Image** servirá para darmos uma visualização do arquivo para o usuário sem a necessidade de baixar o arquivo.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/c6simage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/c6simage.png)

1. As configurações do **Display Image** será com seu **Label** recebendo o nome do arquivo via variável.
2. Depois em seu **Filename Column** colocaremos a coluna "Nome" de sua coluna.
3. No **MIME Type Column** colocaremos a coluna "Tipo" de sua coluna.

Para finalizar o formulário criaremos seus botões.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/46Yimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/46Yimage.png)

- Caso a **tabela sirva apenas para armazenar arquivos**, seguindo a regra de não deixar registros nulos, criaremos dois botões um de **SALVAR** com o Database Action como **SQL UPDATE action** e um de **DELETAR** com a *Database Action* como **SQL DELETE action.**
- Caso **sirva para além de armazenar um arquivo** faremos dois botões, um para salvar e o outro para excluir somente o arquivo, **os dois terão *action* de Submit Page e *Database Action* como SQL UPDATE action.**
- Caso seja da regra da tela **apenas apagar o arquivo e não o registro,** criaremos o processo para deletar o arquivo: ```pl/sql
    procedure pr_deletar_arquivo( pn_id_proctpproc in number) is
    begin
         update juridico.proc_tipoprocuracao       proc_tpproc 
         set    proc_tpproc.modelo_procuracao      = null
         ,      proc_tpproc.modelo_procuracao_nome = null
         ,      proc_tpproc.modelo_procuracao_tipo = null
         where  proc_tpproc.id_proctpproc          = pn_id_proctpproc;
    end pr_deletar_arquivo;
    ```
    
    <p class="callout info">💡 Lembrando que esse código é a da tela de exemplo, portanto deve se alterado o **"juridico"** pelo **owner** da sua tabela, e as colunas de acordo com o que está na tabela que fará a aplicação de sua tela.  
    **Não esquecer de declarar no *<u>head </u>*da <u>package </u>a <u>procedure </u>depois de terminar.**</p>

Agora criaremos o processo da tela do APEX:

 [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/1ZTimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/1ZTimage.png) [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/d2fimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/d2fimage.png)

O **Type** da procedure será **Execute Code** e colocaremos a chamada da *procedure* no source.

```
juridico.pkg_apex_anexos.pr_deletar_arquivo
( pn_id_proctpproc => :P41_ID_PROCTPPROC                                         , pv_modelo        => :P41_MODELO);
```

Lembrar de colocar no **Server side-Condition** o nome do botão de deletar.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/jtcimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/jtcimage.png)

#### **Resultado**

---

O resultado esperado independente da situação será:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/wbYimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/wbYimage.png)

<p class="callout warning">Vale ressaltar que essa tela em específico possui 2 campos para imagem, por isso existem algumas diferenças no que será mostrado para a tela.</p>

---

**Tela exemplo** ➝ [40202:40](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-procuracoes/tipos-de-procuracao?clear=Y&session=8819700883093&cs=3BZY5jpgf5NfNWL76aiBnj4Jd__IC-1ucvMJ6EMSoDWDpSi81wQ21oE4QuIQ7IbTkOAdiJYSgsvblci0Du-MIiQ "Tipos de Procuração") e 40202:41

# Imagem Sem Foto Padrão - Placeholder

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Stgimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Stgimage.png)

Caso precisem usar, **não é mais necessário colocar na página o css com o background da foto** acima para quando não houver foto.

#### **Como Usar**

---

1. Criar um item de página do tipo display image  
    [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/X3Ximage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/X3Ximage.png)
2. Em SETTINGS alterar o Based On para o da foto abaixo  
    [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/NLQimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/NLQimage.png)
3. Colocar essa SQL:  
    ```pl/sql
    select csweb.pkg_apex_utils.fn_nvl_image(vw.foto) foto
    from   (
    select foto
    from   rh.pessoa_foto
    where  cod_pessoa = [COD_PESSOA]
    
    union all
    
    select null from dual
    where  not exists (select 1 from rh.pessoa_foto
                       where  cod_pessoa = [COD_PESSOA])
    ) vw
    ```

# Preview/Download de Arquivos

De uma maneira geral, este guide explicará como ter um preview (visualização) de arquivos do tipo de imagem e também documentos, como por exemplo PDF's.

<span class="ql-badge-blue">Pode ser utilizado tanto em **Interactive Grids quanto em Reports**</span>, já que a essência do funcionamento é por via de uma **coluna *LINK* dentro da sua SQL e um *Page Item* por fora atrelado a uma *Dynamic Action*.**

1. Primeiro é necessário criar um page item. No exemplo utilizaremos o P1146\_PREVIEW;
2. Agora vamos criar sua coluna do tipo LINK dentro da SQL, faça isso da seguinte maneira:
    
    [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/mwLimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/mwLimage.png)
    
    ```
    'apex.item(''P1146_PREVIEW'').setValue('||ID_SOLCARANEX||');' link_preview
    ```

#### **Explicando o Código**

---

Basicamente estamos definindo o valor da PK da sua tabela para o page item `P1146_PREVIEW` sempre que clicar no LINK.

- `ID_SOLCARANEX `➝ É a PK da tabela utilizada no exemplo acima;
- `P1146_PREVIEW` ➝ O Item criado que receberá o valor;

Como dito acima, a coluna terá a configuração de type: LINK;

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/WtAimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/WtAimage.png)

O LINK terá como *TARGET TYPE* o tipo URL, contendo o seguinte código:

```
javascript:&LINK_PREVIEW.
```

`&LINK_PREVIEW.` ➝ É o nome da coluna LINK que você criou anteriormente dentro da SQL;

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/RZlimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/RZlimage.png)

Também crie um `<span class="fa fa-image"></span>` TAG no Link Text para utilizar um icon de imagem na column link;

#### **Finalizando: criando uma Dynamic Action para o `P1146_PREVIEW`**

---

1. Crie uma *Dynamic Action* do tipo onChange com *True Action* <span class="ql-badge-red">FOS - Download Files</span>
2. Apenas mude o File Mode para "Preview" e altere o Preview Title para o título que você deseja;

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/waSimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/waSimage.png)

Dentro da SQL Query, siga o exemplo da QUERY:

```
select file_name    as file_name
     , mime_type    as file_mime_type
     , blob_content as file_content_blob
from   sua_tabela
```

- **file\_name** ➝ O nome do arquivo;
- **file\_mime\_type** ➝ o mime\_type;
- **blob\_content** ➝ seu arquivo do tipo BLOB;

<p class="callout info">Lembre sempre de **estruturar as cláusulas where da sua query de acordo com as necessidades** <span class="cu-emoticon cu-emoticon_static" data-emoticon="{"code":"1f642","name":"Slightly Smiling Face"}">🙂</span></p>

#### **Minha tabela não possui MIME\_TYPE, e agora?**

---

```
select file_name                  as file_name
     , 'application/octet-stream' as file_mime_type
     , blob_content               as file_content_blob
from   sua_tabela
```

 Genericamente falando utilizar o 'application/octet-stream' como valor da sua coluna deve resolver seu problema;

#### **Resultado Esperado**

---

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/hqSimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/hqSimage.png)

# Biometria

# Validação Biométrica

#### **Executar *“cs\_biometria\_apex.exe”* com mesmo usuário logado no Apex**

---

**Caminho :** *“C:\\COMPUSOFT\\CONTROLEPATRIMONIAL\\cs\_biometria\\exe\\cs\_biometria\_apex.exe”*

#### **Configurar o: *“FOS-Redirect”* do *“triggering\_element\_id”* para abrir o modal da Biometria.**

---

**Tela Exemplo:** [40401:520](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-principal/alcada?session=9214413713697)

*P520\_ALMOXARIFE\_BIO\_TG &gt; onChange ou onClick &gt; FOS–Execute PL/SQL Code \[Plug-In\]:*

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/g6Iimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/g6Iimage.png)

---

 ***P520\_ALMOXARIFE\_BIO\_TG &gt; onChange ou onClick &gt; FOS–Redirect &gt; URL PL/SQL Expression:***

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/T6yimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/T6yimage.png)

#### **Configurar “*onDialogClosedOrCanceled”* do *“triggering\_element\_id”* para obter resultado da Biometria.**

---

**Tela Exemplo:** [40401:520](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-principal/alcada?session=9214413713697)

*P520\_ALMOXARIFE\_BIO\_TG &gt; onDialogClosedOrCanceled &gt; FOS–Execute PL/SQL Code \[Plug-In\]:*

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/1AMimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/1AMimage.png)

*P520\_ALMOXARIFE\_BIO\_TG &gt; onDialogClosedOrCanceled &gt; Submit Page (exemplo do que fazer depois que houver sucesso):*

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/9tpimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/9tpimage.png)

# Callback

# AJAX Callback

Para facilitar a implementação de AJAX Callback, de forma a não termos de atualizar todas aplicações quando criarmos uma chama global, criamos uma chamada genérica:

```
csweb.pkg_apex_scaffold.pr_callback;
```

Onde internamente são referenciadas apenas os procedimentos onde estão as regras de negócio de cada módulo, dessa forma a `pr_callback` da "csweb.pkg\_apex\_scaffold" fica totalmente ***"DUMB"*** e livre de regras de negócio.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/XjWimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/XjWimage.png)

Tomaremos como exemplo a `pr_executar_callback` da `csweb.pkg_apex_notificacao` onde aguardamos por um ***Callback Name*** `lerNotificacao` para executar nossa ação:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/I8simage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/I8simage.png)

<p class="callout info">💡 Nesse exemplo ela marca a mensagem como "Lida" `pr_ler_notificacao` e retorna um sinal de sucesso para o Plugin no Front-end.</p>

Que por sua vez chega até o ***back-end*** pela função JS `lerNotificacao` onde o nome do nosso Process genérico sempre será nomeado como `<strong>csCallback</strong>` , o primeiro parâmetro dele terá o nome do nosso ***Callback Name*** (a ser interpretado/esperado dentro da nossa procedure de Regra de Negócio) , no exemplo usamos o nome `lerNotificacao` (uma boa prática é manter esse nome único dentro do ERP), e do segundo parâmetro em diante, sim, passaremos parâmetros para uso dentro dos nossos procedimentos, no exemplo, enviamos o 2 parâmetro com o id da notificação a ser lida:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/G0Mimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/G0Mimage.png)

Por ser uma função **GLOBAL**, a mesma foi programada em um arquivo do Tema da aplicação SCAFOLD (40000).

Exemplo em : `scripts/apex-notification.js`

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/h5uimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/h5uimage.png)

Dessa forma, teremos sempre um PROCESS de aplicação "ouvindo" a chamada do **csCallback ,** disparando a `csweb.pkg_apex_scaffold.pr_callback;` cujo por sua vez faz a chamada das procedures que contem regra de negócio, onde dentro dessas procedures, está se orientando pelo primeiro parâmetro do `APEX_NOTIFICATION,` e caso seja a sua chamada, executa os procedimentos.

# Diálogos de Confirmação com Callback

<p class="callout warning">Esta solução foi desenvolvida para um **cenário específico** onde a ação dinâmica **Confirm** não atendia as necessidades da tela, pois se fazia necessário executar ações após clicar no botão de cancelar da confirmação, o que a ação dinâmica não faz.   
**A ação dinâmica Confirm ainda é a forma preferida** de se desenvolver diálogos de confirmação no APEX.</p>

#### **Como Fazer**

---

Adicione a chamada da função a qualquer ação **Execute JavaScript Code** da sua escolha.

```
confirmDialog(mensagem, function(okPressed) {
  //callback
}, {icon: 'fa fa-lg fa-question-circle u-hot-text'
   , confirmLabel: 'Sim'
   , cancelLabel: 'Não'
   , cssClasses: ''});
```

A função recebe os seguintes parâmetros:

- **mensagem**: *string*
    - A mensagem do dialog.
- **callback**: *function(okPressed)*
    - Função de callback que executa quando um botão é selecionado.
    - Funciona da mesma maneira que o callback da `apex.message.confirm:`

```
function(okPressed) {
  //callback
}
```

- **opcoes**: *Object*
- - - Opções de customização desejadas. Apenas as opções informadas afetarão o dialog.  
            Opções suportadas atualmente: 
            - icon: classes CSS do ícone desejado;
            - cssClasses: classes CSS do dialog;
            - confirmLabel: label do botão de confirmar;
            - cancelLabel: label do botão de cancelar;
        - **<u>Exemplo</u>**: 
            - `{icon: 'fa fa-lg fa-question-circle u-hot-text', confirmLabel: 'Sim', cancelLabel: 'Não'}`

# Cards

# Cards APEX

O processo de criação de cards no apex é simples, porém exige atenção em alguns detalhes importantes.

Existe um **modelo "padrão"** que estamos utilizando quando se trata de cards.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/3Orimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/3Orimage.png)

🔗 [Saiba as boas práticas de experiência e usabilidade para o usuário ao utilizar os cards em telas ou dashboards.](https://wiki.cscompusoftware.com.br/books/erp-guideline-de-uiux/page/cards "Boas Práticas dos cards")

Para criar um card igual a esse, devemos primeiro criar uma região do tipo card no apex, e criar colocar a query que será responsável por trazer o conteúdo nos cards, após isso, precisamos configurar algumas coisas na página de extrema importância.

A primeira coisa que deve ser feita é adicionar a classe: `cs-headcount-card` no campo "CSS Classes" no Appearence da região dos cards.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/9xkimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/9xkimage.png)

#### **Cor do Card**

---

É possível controlar a cor dos cards de forma individual pelo css, porém é necessário fazer isso de forma manual no atributo **"CSS Inline"** da sua página.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/ewwimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/ewwimage.png)

Existem diversas formas de alterar a cor do card, porém **a mais comum é criar um ID para cada card:**

- Fazer um seletor CSS que encontre esse ID.
- Depois de encontrado o ID, podemos alterar todo o CSS do card como bem entendermos, no entanto, é recomendado que seja alterado apenas o **"background-color"** e o **"font-color"**. Para manter o "padrão" determinado.

Exemplo de como retornar "ID's" para cada card individual na SQL:

```pl/sql
select 1 as qtd
     , 'Férias' title
     , 1 as id_card
     , 'fa fa-sun-o' icon
from   dual

union all

select 2 as qtd
     , 'Programadas' title
     , 2 id_card
     , 'fa fa-calendar-clock' icon
from   dual

union all

select 3 as qtd
     , 'À vencer' title
     , 3 id_card
     , 'fa fa-calendar-alarm' icon
from   dual
```

Neste exemplo, **cada "union" representa um card**, portanto, teremos 1 card com a descrição "Férias" e com o ID 1, um card com a descrição "Programadas" e ID 2 e assim sucessivamente.

Exemplo de como criar seletores para alterar a imagem de cada **cor via CSS Inline**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Exfimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Exfimage.png)

Depois de alteradas as cores, precisamos configurar a região dos cards. Para isso, devemos selecionar a região e **ir na aba "Atributtes"** que se encontra na parte superior direita do editor do Apex.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/eyeimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/eyeimage.png)

Existem algumas **configurações que devem ser definidas como "Padrão"**, no entanto, existem algumas configurações que podem ser alteradas com o intuito do card se "encaixar" melhor para a sua necessidade.

#### **Configurações Obrigatórias**

---

1. Definir **uma coluna de Primary Key** - Pode ser a PK da tabela que é realizada a query, ou até mesmo a coluna ID que criamos anteriormente.)
2. Selecionar qual vai ser o **título do card pelo atributo "Title"**, o title fica na parte central superior de cada card, caso o seu card deva se parecer igual ao da imagem do início deste guideline, devemos selecionar nesta região, a coluna que retorna a quantidade de registros.  
      
    <span style="background-color: rgb(251, 238, 184);"><span class="ql-bg-yellow">**🚨 Importante:** Devemos adicionar a seguinte classe CSS para esta região: </span>`card-headcount-qtd`  
      
    </span>
    
    [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/95Fimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/95Fimage.png)
3. Selecionar o **subtítulo da região**. O subtítulo fica logo abaixo do Título com uma fonte menor. Novamente, se seu card precisa estar igual ao da imagem do início, nesta região selecionamos a coluna da descrição que será apresenta nos cards.  
      
    <span style="background-color: rgb(251, 238, 184);"><span class="ql-bg-yellow">**🚨 Importante:** Devemos adicionar a seguinte classe CSS para esta região: </span>`card-headcount-titulo`  
      
    </span>
    
    [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/YrGimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/YrGimage.png)
4. Por fim, na região **"Icon and Badges"** devemos selecionar coluna que retorna o ícone. Para isso devemos deixar a configuração da região como:
    
    
    - Icon Source: Icon Class Column
    - Icon Column: #Sua coluna que retorna o ícone#
    - Icon CSS Classes: `card-headcount-icon`
    - Icon Position: Start  
          
        <span style="background-color: rgb(251, 238, 184);">🚨 <span class="ql-bg-yellow">**Importante:** Colocar a classe CSS nesta região. Caso contrário o card poderá ficar "desconfigurado".  
          
        </span></span>
        
        [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Zbuimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Zbuimage.png)
        
        <span style="background-color: rgb(251, 238, 184);"><span class="ql-bg-yellow">  
        </span></span>

<p class="callout info">💡**Lembrete:** A configuração da região "Atributtes" do card pode ser feita da forma que for necessário para sua tela. O desenvolvedor pode alternar quais informações exibir em cada região do card (Title, Subtitle, etc).</p>

#### **Outras Propriedades**

---

É possível **alterar outras propriedades** dos cards por CSS, como **por exemplo sua largura**, para isso, basta fazer um seletor que leve em consideração a classe CSS que o Apex monta do card, e a classe que CSS que nós passamos. Como por exemplo:

```
.cs-headcount-card .a-CardView-item{ 
    width: 190px !important;
    height: 70px !important;
}
```

# Collections

# APEX Collections x CS Collections

[Collections ](https://docs.oracle.com/cd/E59726_01/doc.50/e39149/apex_collection.htm#AEAPI531)são "tabelas temporárias" no APEX, normalmente, usamos elas quando precisamos de uma tabela "auxiliar/intermediária" <span class="ql-color-red">temporária </span>em algum processo.

Nativamente no APEX, a visibilidade das [Collections ](https://docs.oracle.com/cd/E59726_01/doc.50/e39149/apex_collection.htm#AEAPI531) são **limitadas por APLICAÇÃO** , como trabalhamos com um sistema integrado, onde as aplicações se intercomunicam, surgiu a necessidade da criação do nosso próprio sistema de collections, que carinhosamente ❤️ chamamos de *CS Collections ®*.

A CS Collection nos permite o uso de collections entre os APPs sem restrições. Centralizamos o uso na nossa PKG `csweb.pkg_apex_collection`**.**

#### **Exemplos básicos de usos**

---

##### **Para criar:**

```pl/sql
csweb.pkg_apex_collection.pr_create_collection(p_collection_name => 'COPIAR_BEM_IFRS');
```

<p class="callout info">O Nosso *create* já é um *Create or Truncate.*</p>

Caso precise que os dados não sejam truncados pela **pr\_create\_collection**, basta fazer uma condição externa usando a **fn\_collection\_exists** para verificar se a collection em questão já existe ou não.

```pl/sql
if not csweb.pkg_apex_collection.fn_collection_exists(p_collection_name => 'COPIAR_BEM_IFRS') then
   csweb.pkg_apex_collection.pr_create_collection(p_collection_name => 'COPIAR_BEM_IFRS');
end if;
```

##### **Para popular:**

```pl/sql
csweb.pkg_apex_collection.pr_add_member( p_collection_name => 'COPIAR_BEM_IFRS'
                                       , p_c001            => r_bem_ifrs.observacao);
```

##### **Para limpar :**

```pl/sql
csweb.pkg_apex_collection.pr_truncate_collection(p_collection_name => 'COPIAR_BEM_IFRS');
```

##### **Para ler:**

```pl/sql
select c001 
from   csweb.vw_apex_collections 
where  collection_name = 'COPIAR_BEM_IFRS';
```

<p class="callout warning">Para leitura das informações,<span class="ql-bg-red"> SEMPRE </span>use a view **csweb.vw\_apex\_collections** , pois ela garante que os dados que vc esta vendo são única e exclusivamente seus.</p>

---

**Tela exemplo:** 40255:171

# CRUD Collection

Neste guia será ensinado como realizar Insert, Update e Delete em uma collection, utilizando-a dentro de uma **Interactive Grid**.

**1.1** ➝ Sua SELECT deverá, obrigatoriamente, possuir a coluna **SEQ\_ID** e mantê-la como **PK**.

```pl/sql
select c001
     , c002
     , c003
     , seq_id
from   csweb.vw_apex_collections
where  collection_name = 'QR_HORARIO_FAIXA';
```

<div class="code-toolbar" id="bkmrk-"><div class="toolbar">  
</div></div>**1.2** ➝ Na sua página, aba **Processing**, selecione o processo da sua Interactive Grid.

<p class="callout info">😰 Nas opções ao lado direito, o **TARGET Type deverá ser do tipo PL/SQL Code** e a opção **LOCK ROW** deve estar com a seleção **"No"**.  
</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/scaled-1680-/3nYimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/3nYimage.png)

<p class="callout warning">**Atenção!** O LOCK ROW com a seleção "No" deverá ser somente em **operações DML na collection**.</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/scaled-1680-/OMMimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/OMMimage.png)

**1.3 ➝** Para finalizar, dentro do bloco de código "PL/SQL Code to Insert/Update/Delete", o código no **seguinte padrão**:

```pl/sql
declare
r_collection csweb.collection%rowtype;
begin

r_collection.seq_id := :SEQ_ID;
r_collection.collection_name := 'QR_HORARIO_FAIXA';

r_collection.c001 := :C001;
r_collection.c002 := :C002;
r_collection.c003 := :C003;
csweb.pkg_apex_collection.pr_crud_collection( p_row_status     => :APEX$ROW_STATUS
                                            , p_row_collection => r_collection );

end;
```

<div class="code-toolbar" id="bkmrk--3"><div class="toolbar">  
</div></div>**EXPLICAÇÃO DO CÓDIGO ACIMA:**

**1.3.1** ➝ No declare, será criado uma variável do tipo **csweb.collection%rowtype**. No exemplo citado, está sendo usada uma variável com o nome **"r\_collection"**, mas essa variável poderá ter o nome ajustado de acordo com a necessidade e com o que faz sentido da sua tela.

**1.3.2** ➝ Haverão duas linhas obrigatórias, sendo elas:

- `r_collection.seq_id` ➝ O valor deverá ser a sua coluna da grid **SEQ\_ID**;
- `r_collection.collection_name` ➝ O valor será o nome da sua collection;

**1.3.3** ➝ As demais linhas antes da chamada da procedure `pr_crud_collection` serão as colunas que você possuirá na sua Interactive Grid.

**1.3.4** ➝ Por fim, a chamada da `csweb.pkg_apex_collection.pr_crud_collection`, sendo os dois parâmetros passados do tipo fixo.

- O primeiro parâmetro, `APEX$ROW_STATUS` determinará qual tipo de operação está sendo realizada, seja ela Insert, Update ou Delete.
- O segundo parâmetro será a sua variável.

# Componentes de Busca Apex

#### **Configuração do Botão Redirect para Aplicação Diferente (Chamando a Modal de Busca)**

---

Para implementar o sistema de busca, é necessário criar um botão do tipo *Redirect in Different Application*, responsável por chamar a modal de busca.

- **Application:** 40010
- **Page:** 50

##### **Definição dos Parâmetros da Modal**

- **P50\_APP\_ID** → Número da aplicação onde a busca será realizada (exemplo: *40402*).
- **P50\_PAGES** → Lista de números das páginas individuais a serem pesquisadas, separadas por “-” (exemplo: *591-592-593*).
- **P50\_PAGES\_RANGE** → Definição do intervalo de páginas para busca, informando a página inicial e a página final, separadas por “-” (exemplo: *590-640*).

#### **Adição do Processo nas Páginas Destinadas à Busca**

---

Nas páginas onde a busca será executada, é necessário incluir um processo do tipo *Before Header* para destacar os componentes pesquisados.

- **Código PL/SQL:**

```
csweb.pkg_apex_pesquisa_componente.pr_destacar_componente;
```

- As regiões que serão destacadas devem ter um **STATIC ID** definido. O componente de busca **ignora** tanto páginas Modais, quanto regiões de Button Container, Blank with Attributes e Interactive Report

---

**Tela exemplo** ➝ [40402:590](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-informacoes-gerais/parametros-materiais)

# Componentes de Busca Apex

#### **Implementação**

---

##### **1. Configuração do Botão Redirect para Aplicação Diferente (Chamando a Modal de Busca)**

Para implementar o sistema de busca, é necessário criar um botão do tipo *Redirect in Different Application*, responsável por chamar a modal de busca.

- **Application:** 40010
- **Page:** 50

##### Definição dos Parâmetros da Modal

- **P50\_APP\_ID** → Número da aplicação onde a busca será realizada (exemplo: *40402*).
- **P50\_PAGES** → Lista de números das páginas individuais a serem pesquisadas, separadas por “-” (exemplo: *591-592-593*).
- **P50\_PAGES\_RANGE** → Definição do intervalo de páginas para busca, informando a página inicial e a página final, separadas por “-” (exemplo: *590-640*).

##### **2. Adição do Processo nas Páginas Destinadas à Busca**

Nas páginas onde a busca será executada, é necessário incluir um processo do tipo *Before Header* para destacar os componentes pesquisados.

- **Código PL/SQL:** ```
    csweb.pkg_apex_pesquisa_componente.pr_destacar_componente;
    ```
- As regiões que serão destacadas devem ter um **STATIC ID** definido. O componente de busca **ignora** tanto páginas Modais, quanto regiões de Button Container, Blank with Attributes e Interactive Report

---

**Tela exemplo** ➝ [40402:590](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-informacoes-gerais/parametros-materiais)

# Controle de Abas

# Controle de Abas

#### **"Por que não usar o Region Display Selector ou uma região com o template Tab Container"?**

---

As regiões de Region Display Selector e Tab Container não possuem o controle granulado de eventos que o CS precisa para muitas páginas, portanto foi escolhido implementar a funcionalidade de controle de abas através de controle manual da visibilidade das regiões usando botões.

#### **Implementando o Controle de Abas**

---

A estrutura do controle de abas é composta dos seguintes componentes:

- Um **Hidden Page Item** que guarda o índice (tab index) da aba selecionada.
- **Buttons** para cada aba;
- **Regions** que correspondem as abas dos botões;
- Uma série de **Dynamic Actions.**

#### **Hidden Page Item**

---

O Page Item é utilizado para simplificar a estrutura das Dynamic Actions e expor uma forma de controlar a aba ativa. Ele terá um **Default = Type** **static** de 0 (ou o índice que corresponde a aba desejada para o padrão).

<p class="callout info">Vale ressaltar que para os valores receberem dessa maneira ele não vai se manter na mesma página após o Submit page.</p>

#### **Botões**

---

Os botões criados para o controle de abas devem estar no **Breadcrumb Bar** dentro da region **tabs-container \[Global Page\]**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/ww4image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/ww4image.png)

Já quando for uma **modal** os botões devem estar em uma **Static Content Region** do tipo **Button Container** com as opções de template (**Appearance &gt; Template Options**):

- **Body Padding** = No Padding;
- **Style** = Borderless;

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/qwdimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/qwdimage.png)

Os botões também devem estar na posição **Previous**, para que fiquem lado a lado:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/Q4Timage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/Q4Timage.png)

Além disso, os botões devem ter um **Static ID** definido no seguinte formato:

`<strong>[NOMEDOITEM]</strong>_BTN_<strong>[VALOR]</strong>`

onde **\[NOMEDOITEM\]** corresponde ao nome do **Hidden Page Item** criado anteriormente, e **\[VALOR\]** corresponde ao número da aba.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/JQGimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/JQGimage.png)

#### **Regions**

---

As regions que contém o conteúdo de cada aba podem utilizar qualquer template que seja desejado, mas recomenda-se utilizar o template **Standard** com **Header = Hidden.**

Além disso, as regions devem ter um **Static ID** definido no seguinte formato:

`<strong>[NOMEDOITEM]</strong>_TAB_<strong>[VALOR]</strong>`

onde **\[NOMEDOITEM\]** corresponde ao nome do **Hidden Page Item** criado anteriormente, e **\[VALOR\]** corresponde ao número da aba.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/SbUimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/SbUimage.png)

#### **Dynamic Actions**

---

As Dynamic Actions que implementam controle de abas são compostas de 2 partes.

##### **Controle do Page Item (tab index)**

No Page Item, um evento **OnChange** com a ação **True** do tipo **Execute JavaScript Code** com o seguinte código:

`controlaAbas('<em>PXXX_NOME_ITEM</em>');`

onde PXXX\_NOME\_ITEM é o nome do Page Item do controle de abas.

##### **Controle dos Botões e Regiões**

Para definir a aba padrão, adicione a CSS Classes 'hidden' nas regions que não sejam a padrão.

<p class="callout info">**Por que fazer isso?** Para quando a página carregar não aparecer nenhum item que não seja da region padrão e depois eles aparecerem sem problemas.</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/lXqimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/lXqimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/gB7image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/gB7image.png)

Os botões devem possuir uma Dynamic action com evento **onClick** e ação **Set Value** para setar o valor do **Hidden Page Item** e assim fazer o **Client-side Condition** para o controle de abas. Lembrando que o valor a ser setado deve ser diferente para cada region e o botão da region padrão deve ter marcado a *Appearance* **Hot**.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/4FUimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/4FUimage.png)

<p class="callout info">Lembrando que o item afetado(P11\_TABINDEX) deve ser o **hidden page item** da sua página, ou seja, se for na tela 320 seria 'P320\_TABINDEX', o item **não** precisa ter esse nome, apenas para uma manutenção mais fácil deixamos assim.</p>

<p class="callout success">**⭐Saiba as boas práticas do controle de abas:** [Tradicional, Menu Lateral e Tree View.](https://wiki.cscompusoftware.com.br/books/erp-guideline-de-uiux/page/controle-de-abas-tradicional-menu-lateral-e-tree-view "Controle de Abas - Tradicional, Menu Lateral e Tree View")</p>

#### **Button Tabs**

---

Nativamente no Oracle APEX possuímos o um recurso de template de uma region chamada **"Region tabs"**. Que automaticamente é criado abas com controle ao adicionar regions dentro dela, é criado uma aba para cada region de forma automática com um visual moderno de abas. Porém, temos a desvantagem de não podermos capturar o click das abas ou o evento de trocar a aba de forma nativa ou simples. Pensando nisso, foi criado um método para que possamos utilizar esse visual moderno de forma simples e com a vantagem na captura de eventos utilizando o Button do APEX com uma classe CSS que aplica o estilo de abas.

##### **Como Utilizar**

Para adicionar o visual, vá em CSS Classes na sessão Appearance do seu Button e adicione a seguinte classe em CSS: `cs-Button--tabs`

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/7yNimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/7yNimage.png)

Feito isso, está pronto o seu botão com visual de abas moderno 🙂

Ao habilitar o **Hot** ou adicionar a classe em CSS `<strong>t-Button--hot</strong>`, o visual do botão será alterado para o visual selecionado.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/HXPimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/HXPimage.png)

<p class="callout success">⭐ O método de controle de abas **se mantém de acordo como está documentado na guideline:**[ Controle de Abas](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/controle-de-abas)</p>


#### **Controle do Page Item (tab index) - depreciado**

---

***A implementação abaixo é antiga e foi depreciada. É possível encontrar com controles de abas implementados dessa maneira, então essas instruções serão mantidas para referência.***

Desabilite "**Fire on Initialization**" para todos os eventos.

No Page Item, um evento **OnChange** com a **Client-Side Condition** de **Item = Valor** onde **Item** é o próprio Page Item, e **Valor** é o índice correspondente da região desejada;

Este evento terá duas ações **True** e duas ações **False**:

- Ação **True** do tipo **Show** afetando a Region da aba;
- Ação **True** do tipo **Add Class** afetando o botão da aba e adicionando a classe ***t-Button--hot**;*
- Ação **False** do tipo **Hide** afetando a Region da aba;
- Ação **False** do tipo **Remove Class** afetando o botão da aba e adicionando a classe **t-Button--hot**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/wAuimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/wAuimage.png)

#### **Exemplos**

---

**Tela exemplo →** [40104:1780](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-folha-de-pagamento/lancamento-funcionario?session=9214413713697) **Tela exemplo (implementação antiga) ➝** [40702:11](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-motomecanizacao/apontamentos?session=9214413713697)

# Menu Lateral - Tree View

O Plug-in APEX Fancy Tree oferece uma abordagem mais prática e eficiente para a criação de um menu lateral no APEX. Ao contrário do componente padrão Tree View do APEX, este Plug-in vem com detalhes configurados automaticamente, simplificando significativamente o processo de implementação.

#### **Quando Usar?**

---

 O uso do menu no formato *APEX Fancy Tree View* está alinhado com o **padrão estabelecido em reuniões com o time de UI/UX**. Este padrão serve como uma diretriz para determinar quando é apropriado empregar o *APEX Fancy Tree View.*

<p class="callout info">**💡 Mais informações:** [Controle de Abas - Tradicionais, Menu Lateral e Tree View](https://wiki.cscompusoftware.com.br/books/erp-guideline-de-uiux/page/controle-de-abas-tradicional-menu-lateral-e-tree-view#bkmrk-%C2%A0tree-view "Boas Práticas da Tree View")</p>

#### **Como Usar?**

---

<p class="callout success">⭐ Para **uma implementação bem-sucedida** do Plug-in, consulte o guia: [APEX Fancy Tree](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/apex-fancy-tree "APEX Fancy Tree")</p>

Ao criar o componente, você encontrará uma SQL que fornece os campos necessários para a construção do menu. Estes campos são essenciais para garantir a consistência e funcionalidade do menu conforme o padrão estabelecido.

- **ID:** É o ID de cada registro, Normalmente será a PK de sua tabela.
- **PARENT\_ID:** É o ID do pai do registro, exemplo no Objeto de custo: "objetocusto.objeto\_pai".
- **TITLE:** Será a descrição de cada registro.
- **SELECTED:** 1 para o registro carregar selecionado ou 0/null para o registro carregar selecionado.
- **LINK:** É o URL atribuído a página, utilizaremos o apex\_page.get\_url e passamos os parâmetros da página desejada.
- **ICON:** É o ícone de acordo com o contexto do menu criado.
- **VALUE:** É o valor do item que está sendo passado.

<p class="callout info">Vale ressaltar que para utilização do Plug-in criaremos uma **view para esse menu**, onde dentro dela que será feita toda a manutenção da select.</p>

**Exemplo de um trecho da view criada para a utilização do menu:**

```
select '1.0'      id
     , ''         parent_id
     , 'Produção, Mortalidade e Temperatura' title
     , case when v('APP_PAGE_ID') = 313 then ''
            else apex_page.get_url( p_application => '40901'
                                  , p_page        => '313')
       end  link
     , case when v('APP_PAGE_ID') = 313 then 1
            else 0
       end  selected
     , 'fa fa-bar-chart' icon
     , null value
     , 1 expanded
from   dual

union all

select '1.1'      id
     , '1.0'      parent_id
     , 'Produção de Ovos' title
     , case when v('APP_PAGE_ID') = 313 then ''
            else apex_page.get_url( p_application => '40901'
                                  , p_page        => '313'
                                  , p_items       => 'P313_TAB_INDEX'
                                  , p_values      => '1')
       end  link
     , 0 selected
     , 'fa fa-industry' icon
     , 1 value
     , 0 expanded
from   dual

union all

select '1.2'      id
     , '1.0'      parent_id
     , 'Mortalidade de Aves/Grupo Coleta' title
     , case when v('APP_PAGE_ID') = 318 then ''
            else apex_page.get_url( p_application => '40901'
                                  , p_page        => '318')
       end  link
     , 0 selected
     , 'fa fa-heartbeat' icon
     , 2 value
     , 0 expanded
from   dual
```

<p class="callout info">Para uma consulta completa, consultar na view **avicultura.vw\_apex\_40901\_4895\_tree\_view**.</p>

#### **Padrões de Layout**

---

Requisitos básicos de configuração de layout e funcionalidades que devem ter no menu.

O Treeview deve estar dentro de uma região com template "Blank With Attributes", cujo terá a seguinte classe CSS: `cs-menu-lateral`

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/l8jimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/l8jimage.png)

O input de busca deve estar no template "Hidden", com "Icon" e "Value Placeholder" informados conforme o print.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/NnMimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/NnMimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/M3Yimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/M3Yimage.png)

Quando for necessário colocar os botões de controle Expandir/Retrair, utilize uma Region template "Blank With Attributes" e informe a Classe CSS: `cs-treeview-buttons`

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/3lDimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/3lDimage.png)

##### **Template dos botões:**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/N0Limage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/N0Limage.png)

<p class="callout success">⭐ **O label dos botões serão:** "Mostrar todos" e "Ocultar todos"</p>

Para configurarmos a funcionalidade dos botões primeiro precisamos informar um ***Static ID*** para o Tree View.

**Exemplo:** menu-tree-view

No click dos botões informe uma ação Execute JavaScript Code com o seguinte código:

**Expandir:**

```
$("#menu-tree-view").trigger("expandAll");
```

**Retrair:**

```javascript
$("#menu-tree-view").trigger("collapseAll");
```

Seguido das ações show e hide para controle de visualização dos botões.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/srnimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/srnimage.png)

#### **Exemplo**

---

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/3sQimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/3sQimage.png)[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/MRLimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/MRLimage.png)

**Páginas de exemplo ➝** [40112:1211](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-medicina-trabalho/prontuario)

# Controle de Acesso

<p class="callout warning">É sempre importante **verificar a origem da tela desenvolvida.**</p>

Ao finalizarmos uma tela, devemos integrá-la ao sistema, o que geralmente envolve sua configuração no Controle de Acesso.

<p class="callout info">💡 Vale lembrar que somente quando **a tela for de acesso normal.**</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/E81image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/E81image.png)

Podemos acessar de duas formas: pelo menu lateral (Hambúrguer) ou diretamente no sistema, em **Configurações ➝ Controle de Acesso**.

A estrutura padrão adotada para essa configuração deve seguir o seguinte formato:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Uivimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Uivimage.png)

<p class="callout info">💡 Ao invés de 40702 no começo **deve ser o número de sua aplicação.**</p>

#### **Cadastro de Menu**

---

O **Cadastro de Menu** corresponde ao menu lateral (Hambúrguer) de cada módulo.

Para configurá-lo corretamente, devemos seguir estas diretrizes:

O primeiro link (**APP.000**) deve ser a **Home** do sistema, com:

- **ID APP:** 40010
- **ID Página:** 1
- **Título:** Home
- **Ícone:** `fa-home`

Em seguida, configuramos a **página inicial do módulo**, cujo link será **APP.001**, utilizando:

- **ID APP:** o próprio módulo
- **ID Página:** 1
- **Título:** nome do módulo criado
- **Ícone:** um que represente bem o módulo

Para criar **Submenus**, basta adicionar uma nova linha **sem link de página**, servindo apenas para estruturar a hierarquia do menu. A ordem dos submenus deve seguir a lógica do módulo.

<p class="callout info"> 💡 A cada "passo" no submenu deveremos passar para a próxima coluna a ser salva na **Chave Ordem.**</p>

Depois criaremos as **Funções** do módulo sendo:

<table border="1" id="bkmrk-menu-m%C3%B3dulo-%C3%8Dcone-pa" style="border-collapse: collapse; width: 100%; height: 249.797px;"><colgroup><col style="width: 25.9766%;"></col><col style="width: 21.58%;"></col><col style="width: 20.9774%;"></col><col style="width: 31.466%;"></col></colgroup><thead><tr style="height: 29.7969px;"><td class="align-center" style="height: 29.7969px;">Menu</td><td class="align-center" style="height: 29.7969px;">Módulo</td><td class="align-center" colspan="2" style="height: 29.7969px;">Ícone Padrão</td></tr></thead><tbody><tr style="height: 55px;"><td style="height: 55px;">Manutenções</td><td class="align-center" style="height: 55px;">010</td><td style="height: 55px;">fa-server-wrench</td><td style="height: 55px;">[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/MUdimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/MUdimage.png)

</td></tr><tr style="height: 55px;"><td style="height: 55px;">Processos</td><td class="align-center" style="height: 55px;">020</td><td style="height: 55px;">fa-gears</td><td style="height: 55px;">[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/scDimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scDimage.png)

</td></tr><tr style="height: 55px;"><td style="height: 55px;">Relatórios</td><td class="align-center" style="height: 55px;">030</td><td style="height: 55px;">fa-clipboard-edit</td><td style="height: 55px;">[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/5HBimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/5HBimage.png)

</td></tr><tr style="height: 55px;"><td style="height: 55px;">Consultas</td><td class="align-center" style="height: 55px;">040</td><td style="height: 55px;">fa-file-search</td><td style="height: 55px;">[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/x9zimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/x9zimage.png)

</td></tr></tbody></table>

<p class="callout success">**Padrão:** Cada tela criada faremos de 010 em 010 por padrão.</p>

Lembrar de em todo módulo criado fazer também os links para **SQLs Cadastradas** e **Consulta SQLs Cadastradas** cada um em seu devido lugar na posição, terminando em 999 dentro das funções para ocuparem a última posição da 'árvore'.

#### **Exemplo**

---

Como exemplo criaremos o **Controle de Acesso** para a tela **Material x Contabilidade**:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/k4eimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/k4eimage.png)

##### **Como devemos estruturar nosso pensamento para essa configuração?**

1. Verificar o número da aplicação.
2. Identificar sua função dentro do sistema.
3. Definir sua posição na hierarquia do menu.
4. Validar o Controle de Acesso já existente no APEX (passo essencial para evitar duplicações ou conflitos).

##### Exemplo Prático

- A aplicação de **Contabilidade** tem o número **40254**.
- Sua função no sistema é **Processos**.
- Sua posição será dentro de um **submenu**, que está dentro de outro **submenu**.

Se ainda **não existir nenhuma tela de Processos cadastrada** no módulo de Contabilidade dentro do Controle de Acesso, a **Chave Ordem** será: - **40254.020.010.010.01**

<p class="callout info">**👀 Obs.:** Não termina como 010 por conta de **exceder o tamanho de caracteres**.</p>

Como ordem para isso também teremos o **Material** como ➝ 40254.020.010.010

E também teremos o **Reintegrações** como ➝ 40254.020.010

# Criação de uma nova gestão / módulo

# Novo Módulo

Cada módulo do CS será uma aplicação.

E todas aplicações derivam do mesmo *template* (**40001 CS-TEMPLATE**).

Para criar um novo módulo, faça uma cópia do *template*, e atualize os dados básicos da aplicação.

Clique em *Create*, em seguida em ***Copy Application***

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/scaled-1680-/o4Qimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/o4Qimage.png)

Ou, acesse o *Template* e clique em ***Copy this Application***

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/scaled-1680-/L7fimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/L7fimage.png)

**A numeração (*****Application ID*****) segue a seguinte formatação:**

Para uma nova Gestão acrescentamos 50 (cinquenta) **unidades** ao ultimo APP 40000 existente ( *40050* \[TRIBUTÁRIA\], *40100 \[RH\] etc)* , sendo que, para cada Módulo 1 (uma) **unidade** diferente iniciando sempre pelo 01 ( *40101 - CS Recrutamento e Seleção, 40102 - CS Cargos e Salários ).*

> Reforçando: **Nunca** existirá módulos com final "0" (Zero), pois, o "0" (Zero) representa a **GESTÃO**. Todo módulo, obrigatoriamente, sempre terá início a partir do numeral 1 (um).

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/scaled-1680-/Ss8image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/Ss8image.png)

> Ao efetuar a copia, o processo pode demorar um pouco, retornando ***PROXY ERROR**,* pois, o navegador entende que a aplicação parou de responder, porém, o processo esta sendo executado em *backgroud* normalmente, então, após o erro, basta esperar alguns minutos e o novo APP aparecerá normalmente à lista de APPs.

Após a cópia, revisar detalhes/nomes nas propriedades da aplicação.

**App** &gt; **Edit Application Definition.**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/scaled-1680-/HGcimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/HGcimage.png)

Sempre altere o Nome e o Alias para os do módulo correspondente.

> O *Name* sempre terá o NOME <u>inteligível por extenso</u> do módulo, começando por CS , Ex.: CS Operações Financeiras.  
> Já o Alias por ser o que aparecerá na URL terá o nome todo <u>EM MAIUSCULO</u> separado por "-" e **SEM** caracteres especiais, Ex.: CS-OPERACOES-FINANCEIRAS

### Informar o Grupo da Aplicação.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/scaled-1680-/pMFimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/pMFimage.png)

Caso seja necessário criar um novo Grupo de Aplicação ( o que corresponde a `Gestão `no legado) basta acessar: **App Builder &gt; Wokspace Utilities &gt; Application Groups**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/scaled-1680-/tVnimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/tVnimage.png)

Sempre altere a string de substituição **APP\_NAME** do módulo correspondente para o NOME <u>inteligível por extenso</u> do módulo, começando por CS , Ex.: CS Operações Financeiras.

**SEMPRE** alterar o `OWNER `do *Parsing Schema* para o OWNER do módulo Correspondente.

**APP &gt; Shared Components &gt; Security Attributes &gt; Database Session**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/scaled-1680-/Rpzimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/Rpzimage.png)

> Rara serão as vezes que o `OWNER `CSWEB permanecerá como *Parsing Schema,* o mais comum será o uso dos owners da gestão Ex.: RH, FINANCEIRO, AUTOMOTIVO, GERAL, SEGURANCANOVO e etc.

Obs.: Caso o `<a href="https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/owner-apex">OWNER</a> `não seja listado, verifique como solucionar em:Private ([https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/owner-apex](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/owner-apex))

## Informar o código da gestão/módulo correspondente

**APP &gt; Shared Components &gt; Application Computations**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/scaled-1680-/FRNimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/FRNimage.png)

Selecione as *computations* para G\_COD\_GESTAO e G\_COD\_MODULO e em ***Computation*** **&gt;** ***Computation*** defina o valor que corresponde ao número da gestão e módulo, respectivamente, que correspondem ao módulo na versão desktop.

> **Atenção:** NUNCA usar a formatação de duas casas com "0" (Zero) a esquerda no início dos códigos de Gestão e Módulo (Ex.: **01** &lt;- Isso é errado), sempre encare essa configuração como um "Número Inteiro" e use sem zero a esquerda (Ex.: **1** &lt;- Isso é Correto). Esse cuidado é necessário, pois, isso pode provocar erros no tratamento desse dado posteriormente.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/scaled-1680-/E1Simage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/E1Simage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/scaled-1680-/bucimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/bucimage.png)

Você pode verificar o código da gestão e módulo através do Menu Principal CS.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/scaled-1680-/A2mimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/A2mimage.png)

## Ajustar página 01 - Home

**APP &gt; página 1: Home**

Alterar o Título da página 1 para o nome do módulo correspondente.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/scaled-1680-/Fpiimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/Fpiimage.png)

**SEMPRE** mantenha o Name / Alias como home.

## Controle de acesso do módulo

Sempre que criar um novo módulo lembre de configurar seu Private ([https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/controle-de-acesso](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/controle-de-acesso)) , além de cadastrar este novo módulo no menu da aplicação 40010, para que apareça na página inicial do usuário

# CS Advanced Grid (Grid Dinâmica, Grid Pivotada, CS Grid, Plugin Grid)

Este plug-in de grade utiliza o método de function returning CLOB JSON para a composição da grade de forma dinâmica. Visando oferecer flexibilidade para o desenvolvedor, forma de consiga fazer manipulações avançadas.

# Column - Styles

##### Em Advanced Grid temos a possibilidade de adicionar estilizações customizadas para ás colunas em tempo de execução.  


Para isso, iremos abrir uma sessão de objeto dentro de options &gt; columns &gt; suaColuna, utilizando a função  **APEX\_JSON.OPEN\_OBJECT** passando como parâmetro **styles**. Após isso iremos informar os seguintes parâmetro:

**borderTopColor: <span style="color: rgb(35, 111, 161);">string</span>** - Podemos informar a cor em hexadecimal, rgb ou podemos informar templates como:

<span style="background-color: rgb(203, 17, 0); color: rgb(255, 255, 255);"> **danger** </span>, <span style="background-color: rgb(255, 198, 40);"> </span><span style="color: rgb(43, 43, 43); background-color: rgb(255, 198, 40);">**warning** </span>, <span style="color: rgb(255, 255, 255);">**<span style="background-color: rgb(39, 135, 1);"> success </span>**</span>, **<span style="background-color: rgb(5, 106, 200); color: rgb(255, 255, 255);"> info </span>** ou **<span style="background-color: rgb(5, 106, 200);"> <span style="color: rgb(255, 255, 255);">primary</span> </span>**.

Para configurarmos ás customizações de estilos de coluna em PL/SQL faremos dessa forma:

```pl/sql
function fn_minha_function return clob as
declare
  cursor c_meu_cursor is
    select tabela.coluna1
      from owner.tabela tabela;

  v_variavel clob;
begin
  apex_json.initialize_clob_output;
  
  v_variavel := apex_json.get_clob_output;
  
  
  apex_json.open_object;

    apex_json.open_object(p_name => 'options');

      apex_json.open_object(p_name => 'columns');

        apex_json.write('header', 'Coluna 1', true);

        apex_json.open_object( p_name => 'styles');

          apex_json.write('borderTopColor', '#2EBFBC', true);

        apex_json.close_object;

      apex_json.close_object;

    apex_Json.close_object;

    apex_json.open_object(p_name => 'model');
    
      apex_json.open_array(p_name => 'data');
      
        for r_meu_cursor in c_meu_cursor loop
          apex_json.open_object;
          
            apex_json.open_object(p_name => 'coluna1');
            
              apex_json.write('value', r_meu_cursor.coluna1, true);
            
            apex_json.close_object;
          
          apex_json.close_object;
        end loop;
      
      apex_json.close_array;
    
    apex_json.close_object;
  
  apex_json.close_object;
  
  
  apex_json.free_output;
  
  return v_variavel;
end;
```

Resultado em JSON:

```json
{
  "options": {
    "columns": {
      "coluna1": {
        "header": "Código",
        "styles": {
          "borderTopColor": "#2EBFBC"
        }
      }
    }
  },
  "model": {
    "data": [
      {
        "coluna1": {
          "value": 1
        }
      }
    ]
  }
}
```

🎨 Feito isso, está feito a sua estilização para a coluna.

# Column Groups

##### Em Advanced Grid podemos utilizar a funcionalidade de grupo de colunas similares a Interactive Grid, com o diferencial de que podemos fazer atribuições no grupo de colunas de forma dinâmica.  


Para isso, iremos abrir uma sessão de objeto dentro de options utilizando a função <span style="background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);"> **APEX\_JSON.OPEN\_OBJECT** </span> passando como parâmetro **columnGroup**.   
  
Com isso, essa será a sessão do "container" na qual ficarão todas ás informações dos grupos de colunas, dentro do container abriremos uma nova sessão de objeto passando como parâmetro um id do grupo de colunas e iremos informar os seguinte parâmetro:

**header:** <span style="color: rgb(35, 111, 161);">**string** </span>- Passaremos o valor que aparecerá no título do grupo de coluna.

Após isso iremos nas configurações específicas em options &gt; columns &gt; suaColuna, e passaremos o valor group juntamente com o id do nosso grupo de coluna declarado utilizando a função <span style="background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);"> **APEX\_JSON.OPEN\_OBJECT** </span>.

Para configurarmos o nosso grupo de colunas em PL/SQL faremos dessa forma:

```pl/sql
function fn_minha_function return clob as
declare
  cursor c_meu_cursor is
    select tabela.coluna1
      from owner.tabela tabela;

  v_variavel clob;
begin
  apex_json.initialize_clob_output;
  
  v_variavel := apex_json.get_clob_output;
  
  
  apex_json.open_object;

    apex_json.open_object(p_name => 'columnGroup');

      apex_json.open_object(p_name => 'grupoExemploTeste');

        apex_json.write('header', 'Grupo de Exemplo Teste', true);

      apex_json.close_object;

    apex_json.close_object;

    apex_json.open_object(p_name => 'options');

      apex_json.open_object(p_name => 'columns');

        apex_json.write('group', 'grupoExemploTeste', true);
        apex_json.write('header', 'Coluna 1', true);

      apex_json.close_object;

    apex_json.close_object;

    apex_json.open_object(p_name => 'model');
    
      apex_json.open_array(p_name => 'data');
      
        for r_meu_cursor in c_meu_cursor loop
          apex_json.open_object;
          
            apex_json.open_object(p_name => 'coluna1');
            
              apex_json.write('value', r_meu_cursor.coluna1, true);
            
            apex_json.close_object;
          
          apex_json.close_object;
        end loop;
      
      apex_json.close_array;
    
    apex_json.close_object;
  
  apex_json.close_object;
  
  
  apex_json.free_output;
  
  return v_variavel;
end;
```

Resultado em JSON:

```json
{
  "options": {
    "columnGroup": {
      "grupoExemploTeste": {
        "header": "Grupo de Exemplo Teste"
      }
    },
    "columns": {
      "coluna1": {
        "header": "Código",
        "group": "grupoExemploTeste"
      }
    }
  },
  "model": {
    "data": [
      {
        "coluna1": {
          "value": 1
        }
      }
    ]
  }
}
```

Feito isso, está feito o seu grupo de colunas.

# Configurações iniciais

Primeiramente iremos adicionar o plug-in no page designer, iremos adicionar uma region a página e iremos em type. Selecionaremos a opção **CS - Advanced Grid**.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-12/scaled-1680-/izKimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-12/izKimage.png)

Feito isso, iremos montar o nosso JSON em CLOB.

Para criação do JSON é recomendado utilizar a biblioteca do Oracle APEX\_JSON por questões de performance ao montar o JSON em CLOB, utilizando bibliotecas como dbms\_lob.append, a performance tem uma queda brusca. Você pode encontrar mais informações lendo a documentação da Oracle.  
  
Declararemos uma variável do tipo CLOB em nossa function, após isso, **sempre** iremos colocar a procedure <span style="background-color: rgb(0, 0, 0); color: rgb(206, 212, 217);"> APEX\_JSON.INITIALIZE\_CLOB\_OUTPUT; </span> no começo da nossa função, <span style="color: rgb(206, 212, 217); background-color: rgb(0, 0, 0);"> V\_VARIAVEL := APEX\_JSON.GET\_CLOB\_OUTPUT; </span> para obtermos o valor do JSON montado em CLOB e antes de retornarmos esse valor chamaremos a procedure <span style="color: rgb(206, 212, 217); background-color: rgb(0, 0, 0);"> APEX\_JSON.FREE\_OUTPUT </span>.

```pl/sql
function fn_minha_function return clob as
declare
  v_variavel clob;
begin
  apex_json.initialize_clob_output;
  
  v_variavel := apex_json.get_clob_output;
  
  apex_json.free_output;
  
  return v_variavel;
end;
```

  
 Após criarmos a nossa function, selecionaremos o plug-in e iremos para attributes e adicionaremos a chamada da nossa function criada que retorna o JSON em CLOB.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-12/scaled-1680-/zEWimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-12/zEWimage.png)

Assim nossa estrutura base da function está montada 😊

Feito isso iremos adicionar nossas colunas e linhas. Para isso iremos utilizar a função <span style="background-color: rgb(0, 0, 0); color: rgb(206, 212, 217);"> APEX\_JSON.OPEN\_OBJECT </span>, essa função essa responsável por e abrir ás chaves de um objeto JSON "{". **Sempre** ao utilizarmos funções de aberturas de chaves de um objeto ou colchetes de uma array, precisamos utilizar a função que fechará a abertura, nesse caso utilizaremos a função <span style="background-color: rgb(0, 0, 0); color: rgb(206, 212, 217);"> APEX\_JSON.CLOSE\_OBJECT </span>. Assim nosso objeto está criado { }.   
  
Entre o OPEN\_OBJECT e o CLOSE\_OBJECT iremos criar ás nossas sessões de configurações da grade e de dados a serem mostrados.  
  
  
Caso tenha dúvidas, eis a documentação da Oracle sobre a função APEX\_JSON:  
[https://docs.oracle.com/cd/E59726\_01/doc.50/e39149/apex\_json.htm#AEAPI29655](https://docs.oracle.com/cd/E59726_01/doc.50/e39149/apex_json.htm#AEAPI29655)  
  
Caso ocorra algum erro com a montagem do JSON, eis um site que possa fazer a validação do JSON. Basta pegar o valor e colar no site, se houver algum erro, a validação apontará, caso contrário o JSON será indentado:   
[https://json-indent.com/](https://json-indent.com/)

# Custom column - Badge

##### Em Advanced Grid podemos fazer configurações em cada coluna a nível de célula. Dentre essas configurações, uma delas é o tipo Badge, assim como em outras grades.

  
Para isso iremos utilizar abrir uma sessão de object dentro da coluna em model -&gt; data. Feito isso temos alguns parâmetro a serem informados utilizando a função <span style="background-color: rgb(0, 0, 0);"> <span style="color: rgb(206, 212, 217);">APEX\_JSON.WRITE</span> </span>:

**displayType**: Iremos informar o tipo de visualização da célula que será exibido.

**badgeColor:** Nesse parâmetro é possível informar templates padrões como<span style="color: rgb(0, 0, 0);"> </span><span style="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);"><span style="background-color: rgb(186, 55, 42);"> </span><span style="background-color: rgb(186, 55, 42); color: rgb(255, 255, 255);">**DANGER** </span></span>, <span style="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);"><span style="background-color: rgb(241, 196, 15);"> **WARNING** </span></span>, <span style="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);"><span style="background-color: rgb(45, 194, 107);"> <span style="color: rgb(255, 255, 255);">**SUCCESS** </span></span></span> e <span style="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);"><span style="color: rgb(255, 255, 255); background-color: rgb(53, 152, 219);"> **INFO** </span></span>.

Ou podemos informar cores personalizadas do tipo hexadecimal exemplo: **\#202020**<span style="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);">  
</span>

**fontColor:** Caso seja atribuído algum template em **badgeColor** ou o **badgeType** for informado como 2, a cor da **fontColor** não será aplicada. Caso contrário, é possível informar uma cor de font personalizada no formato hexadecimal.

**badgeType:** É possível informar 1 e 2 para os tipo de badge type, sendo o número 1 uma cor sólida para o badge e uma borda solida e a font com a mesma cor, e com o fundo em uma cor mais "clara".

 **TIPO 1 TIPO 2**

**DANGER ![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-12/scaled-1680-/763image.png) [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-12/scaled-1680-/21Fimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-12/21Fimage.png)**

**<span style="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);">  
</span>WARNING** ![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-12/scaled-1680-/VDUimage.png) [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-12/scaled-1680-/YMYimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-12/YMYimage.png)

 **SUCCESS** ![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-12/scaled-1680-/JUaimage.png) [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-12/scaled-1680-/E6Timage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-12/E6Timage.png)

**INFO** ![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-12/scaled-1680-/qRiimage.png) [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-12/scaled-1680-/zMDimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-12/zMDimage.png)

**CUSTOM** ![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-12/scaled-1680-/2LTimage.png) [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-12/scaled-1680-/ZGiimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-12/ZGiimage.png)

Para configurarmos a customização por coluna será dessa forma :

```pl/sql
function fn_minha_function return clob as
declare
  cursor c_meu_cursor is
    select tabela.coluna1
         , tabela.coluna2
         , tabela.coluna3
      from owner.tabela tabela;

  v_variavel clob;
begin
  apex_json.initialize_clob_output;
  
  v_variavel := apex_json.get_clob_output;
  
  
  apex_json.open_object;
  
    apex_json.open_object(p_name => 'model');
    
      apex_json.open_array(p_name => 'data');
      
        for r_meu_cursor in c_meu_cursor loop
          apex_json.open_object;
          
            apex_json.open_object(p_name => 'coluna1');
            
              apex_json.write('value', r_meu_cursor.coluna1, true);
              
              apex_json.open_object(p_name => 'custom');
              
                apex_json.write('displayType', 'BADGE', true);
                apex_json.write('badgeColor', 'DANGER', true); /* ou apex_json.write('badgeColor', '#0CC4A9'); */
                apex_json.write('fontColor', '#FFFFFF', true);
                apex_json.write('badgeType', 1, true);
              
              apex_json.close_object;
            
            apex_json.close_object;
          
          apex_json.close_object;
        end loop;
      
      apex_json.close_array;
    
    apex_json.close_object;
  
  apex_json.close_object;
  
  
  apex_json.free_output;
  
  return v_variavel;
end;
```

Resultado em JSON:

```json
{
  "options": {
    "columns": {
      "coluna1": {
        "header": "Código",
        "alignment": "right",
        "width": 120
      },
      "coluna2": {
        "header": "Descrição",
        "alignment": "left",
        "width": 250
      },
      "coluna3": {
        "header": "Valor",
        "alignment": "right",
        "width": 150
      }
    },
    "paginations": {
      "type": "page",
      "pagination": 5
    }
  },
  "model": {
    "data": [
      {
        "coluna1": {
          "value": 1,
          "custom": {
            "displayType": "BADGE",
            "badgeColor": "DANGER",
            "badgeType": 1
          }
        },
        "coluna2": {
          "value": "Café"
        },
        "coluna3": {
          "value": 30
        }
      },
      {
        "coluna1": {
          "value": 2,
          "custom": {
            "displayType": "BADGE",
            "badgeColor": "#0CC4A9",
            "fontColor": "#FFFFFF",
            "badgeType": 1
          }
        },
        "coluna2": {
          "value": "Óleo vegetal"
        },
        "coluna3": {
          "value": 20
        }
      }
    ]
  }
}
```

# Custom column - Context menu

##### Em Advanced Grid podemos fazer configurações em cada coluna a nível de célula. Dentre essas configurações, uma delas é o context menu, permitindo mostrar um popup supenso na célula da coluna.

  
Para isso iremos utilizar abrir uma sessão de object dentro da coluna em model -&gt; data. Feito isso temos alguns parâmetro a serem informados utilizando a função <span style="background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);"> APEX\_JSON.WRITE </span>:

**displayType:** Iremos informar o tipo de visualização da célula que será exibido.

**icon:** Informaremos o ícone que será utilizado dentro da célula

Após isso iremos abrir uma array utilizando a função <span style="color: rgb(255, 255, 255); background-color: rgb(0, 0, 0);"> APEX\_JSON.OPEN\_ARRAY </span> no parâmetro da função "p\_name" iremos passar o valor 'list'.

Feito isso iremos utilizar a função <span style="color: rgb(255, 255, 255); background-color: rgb(0, 0, 0);"> APEX\_JSON.OPEN\_OBJECT </span> e após isso iremos informar os seguintes parâmetros utilizando a função <span style="color: rgb(255, 255, 255); background-color: rgb(0, 0, 0);"> APEX\_JSON.WRITE </span>   
  
Os seguintes parâmetros são:  
  
**icon:** Informaremos o ícone que será exibido no item do context menu.

**alignment:** Informaremos a posição na qual o icone ficará.

**application**: Informaremos a aplicação em que o context menu redicionará ao clicar.  
  
**page:** Informaremos a página em que o context menu redicionará ao clicar.  
  
**values:** Informaremos os valores que serão enviados ao sermos redirecionados pelo context menu similar a estrutura da função apex\_page.get\_url.  
  
**items:** Informaremos os items que receberão os valores que serão enviados ao ser redirecionados pelo context menu similar a estrutura da função apex\_page.get\_url.

Para configurarmos a customização por coluna será dessa forma:

```pl/sql
function fn_minha_function return clob as
declare
  cursor c_meu_cursor is
    select tabela.coluna1
         , tabela.coluna2
         , tabela.coluna3
      from owner.tabela tabela;

  v_variavel clob;
begin
  apex_json.initialize_clob_output;
  
  v_variavel := apex_json.get_clob_output;
  
  
  apex_json.open_object;

    apex_json.open_object(p_name => 'options');

      apex_json.open_object(p_name => 'columns');

        apex_json.write('header', 'Coluna 1', true);
        apex_json.write('alignment', 'left', true);
        apex_json.write('width', 120, true);
        apex_json.write('frozen', true);

      aepx_json.close_object;

    apex_Json.close_object;
  
    apex_json.open_object(p_name => 'model');
    
      apex_json.open_array(p_name => 'data');
      
        for r_meu_cursor in c_meu_cursor loop
          apex_json.open_object;
          
            apex_json.open_object(p_name => 'coluna1');
            
              apex_json.write('value', r_meu_cursor.coluna1);
              
              apex_json.open_object(p_name => 'custom');
              
                apex_json.write('displayType', 'CONTEXT-MENU', true);
                apex_json.write('icon', 'fa-info-square-o', true);
                apex_json.write('alignment', 'left', true);

                apex_json.open_array('list');
                  
                  apex_json.open_object;
                    apex_json.write('icon', 'fa-user', true);
                    apex_json.write('label', 'Perfil', true);
                    apex_json.write('application', 40010, true);
                    apex_json.write('page', 1, true);
                    apex_json.write('values', 1 || ',2', true);
                    apex_json.write('items', 'P123_PAGE_ITEM1,P123_PAGE_ITEM2', true);
                  apex_json.close_object;

                  apex_json.open_object;
                    apex_json.write('icon', 'fa-bell-o', true);
                    apex_json.write('label', 'Notificações', true);
                    apex_json.write('application', 40010, true);
                    apex_json.write('page', 1, true);
                    apex_json.write('values', 1 || ',2', true);
                    apex_json.write('items', 'P123_PAGE_ITEM1,P123_PAGE_ITEM2', true);
                  apex_json.close_object;

                  apex_json.open_object;
                    apex_json.write('icon', 'fa-gear', true);
                    apex_json.write('label', 'Minhas configurações', true);
                    apex_json.write('application', 40010, true);
                    apex_json.write('page', 1, true);
                    apex_json.write('values', 1 || ',2', true);
                    apex_json.write('items', 'P123_PAGE_ITEM1,P123_PAGE_ITEM2', true);
                  apex_json.close_object;

                apex_json.close_array;
              
              apex_json.close_object;
            
            apex_json.close_object;
          
          apex_json.close_object;
        end loop;
      
      apex_json.close_array;
    
    apex_json.close_object;
  
  apex_json.close_object;
  
  
  apex_json.free_output;
  
  return v_variavel;
end;
```

Resultado em JSON:

```json
{
  "options": {
    "columns": {
      "coluna1": {
        "header": "Código",
        "alignment": "right",
        "width": 120
      }
    },
    "paginations": {
      "type": "page",
      "pagination": 5
    }
  },
  "model": {
    "data": [
      {
        "coluna1": {
          "value": 1,
          "custom": {
            "displayType": "LINK",
            "icon": "fa-info-square-o",
            "alignment": "left",
            "list": [
              {
                "icon": "fa-user",
                "label": "Perfil",
                "application": 40010,
                "page": 1,
                "values": "1,2",
                "items": "P123_PAGE_ITEM1,P123_PAGE_ITEM2"
              }
              {
                "icon": "fa-bell-o",
                "label": "Notificações",
                "application": 40010,
                "page": 1,
                "values": "1,2",
                "items": "P123_PAGE_ITEM1,P123_PAGE_ITEM2"
              }
              {
                "icon": "fa-gear",
                "label": "Minhas configurações",
                "application": 40010,
                "page": 1,
                "values": "1,2",
                "items": "P123_PAGE_ITEM1,P123_PAGE_ITEM2"
              }
            ]
          }
        }
      }
    ]
  }
}
```

Resultado final:

[![{DD7EF426-0890-4C0A-B4BB-1D213E5CBA73}.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-01/scaled-1680-/dd7ef426-0890-4c0a-b4bb-1d213e5cba73.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-01/dd7ef426-0890-4c0a-b4bb-1d213e5cba73.png)

  
🗒️Feito isso está pronto o seu context menu!

# Custom column - Link

##### Assim como a custom column - badge, podemos criar colunas customizadas a nível de célula para os links.

Para isso, iremos abrir a sessão de objeto custom dentro de nossa coluna e informaremos o displayType como **LINK** e informaremos os seguintes parâmetros:   
  
**icon:** Podemos informar o ícone na qual será mostrado na coluna

**alignment:** Podemos informar em qual posição o ícone estará. Sendo elas: **left** (esquerda) e **right** (direita)

**application:** Podemos informar em qual aplicação da página será redirecionado  
  
**page:** Informamos a página na qual seremos redirecionado

**values:** Informaremos os valores que serão passados para a página. A função apex\_page.get\_url iremos passa dessa forma: 1, 2, 3, 4.

**items:** Informaremos os page items que receberão os values como valor em sequência

```pl/sql
function fn_minha_function return clob as
declare
  cursor c_meu_cursor is
    select tabela.coluna1
         , tabela.coluna2
         , tabela.coluna3
      from owner.tabela tabela;

  v_variavel clob;
begin
  apex_json.initialize_clob_output;
  
  v_variavel := apex_json.get_clob_output;
  
  
  apex_json.open_object;
  
    apex_json.open_object(p_name => 'model');
    
      apex_json.open_array(p_name => 'data');
      
        for r_meu_cursor in c_meu_cursor loop
          apex_json.open_object;
          
            apex_json.open_object(p_name => 'coluna1');
            
              apex_json.write('value', r_meu_cursor.coluna1, true);
              
              apex_json.open_object(p_name => 'custom');
              
                apex_json.write('displayType', 'LINK', true);
                apex_json.write('icon', 'fa-info-square-o', true);
                apex_json.write('alignment', 'left', true);
                apex_json.write('application', 40010, true);
                apex_json.write('page', 1, true);
                apex_json.write('values', 1 || ',2', true);
                apex_json.write('items', 'P123_PAGE_ITEM1,P123_PAGE_ITEM2', true);
              
              apex_json.close_object;
            
            apex_json.close_object;
          
          apex_json.close_object;
        end loop;
      
      apex_json.close_array;
    
    apex_json.close_object;
  
  apex_json.close_object;
  
  
  apex_json.free_output;
  
  return v_variavel;
end;
```

  
Resultado em JSON:

```json
{
  "options": {
    "columns": {
      "coluna1": {
        "header": "Código",
        "alignment": "right",
        "width": 120
      },
      "coluna2": {
        "header": "Descrição",
        "alignment": "left",
        "width": 250
      },
      "coluna3": {
        "header": "Valor",
        "alignment": "right",
        "width": 150
      }
    },
    "paginations": {
      "type": "page",
      "pagination": 5
    }
  },
  "model": {
    "data": [
      {
        "coluna1": {
          "value": 1,
          "custom": {
            "displayType": "LINK",
            "icon": "fa-info-square-o",
            "alignment": "left",
            "application": 40010,
            "page": 1,
            "values": "1,2",
            "items": "P123_PAGE_ITEM1,P123_PAGE_ITEM2"
          }
        },
        "coluna2": {
          "value": "Café"
        },
        "coluna3": {
          "value": 30
        }
      }
    ]
  }
}
```

  
  
🔗 Feito isso, ao usuário clicar na célula da coluna, será redirecionado

# Exportar relatório

##### Em Advanced Grid possuimos a opção para exportar relatório de dados da grade. 

Para isso iremos no botão de "Ações" e selecionaremos a opção "Fazer Download".

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-03/scaled-1680-/oOSimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-03/oOSimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-03/scaled-1680-/NR9image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-03/NR9image.png)

Após isso, será aberto a opção para opções de relatório. Selecionaremos a opção disponível do tipo de exportação do relatório e clicaremos no botão "Fazer Download"

📋Feito isso está pronto seu relatório exportardo direto da Advanced Grid

# Model - Data (rows)

Após ás configurações iniciais terem sido feitas, adicionaremos os registros de linhas e colunas da nossa SQL, para isso iremos inserir uma sessão de objetos dentro de nosso primeiro objeto aberto no topo e nomearemos como **model** e dentro dele criaremos uma outra sessão, porém dessa vez criaremos como uma array nomeada como **data**.

```pl/sql
function fn_minha_function return clob as
declare
  v_variavel clob;
begin
  apex_json.initialize_clob_output;
  
  v_variavel := apex_json.get_clob_output;
  
  
  apex_json.open_object;
  
    apex_json.open_object(p_name => 'model');
    
      apex_json.open_array(p_name => 'data');
      
      apex_json.close_array;
    
    apex_json.close_object;
  
  apex_json.close_object;
  
  
  apex_json.free_output;
  
  return v_variavel;
end;
```

Dentro dessa array, iremos criar nossas linhas da SQL no formato de objetos. Para cada linha abriremos um objeto e para cada coluna, abriremos outro objeto com o name da coluna.  
  
Exemplo:

```pl/sql
function fn_minha_function return clob as
declare
  cursor c_meu_cursor is
    select tabela.coluna1
         , tabela.coluna2
         , tabela.coluna3
      from owner.tabela tabela;

  v_variavel clob;
begin
  apex_json.initialize_clob_output;
  
  v_variavel := apex_json.get_clob_output;
  
  
  apex_json.open_object;
  
    apex_json.open_object(p_name => 'model');
    
      apex_json.open_array(p_name => 'data');
      
        for r_meu_cursor in c_meu_cursor loop
          apex_json.open_object;
          
            apex_json.open_object(p_name => 'coluna1');
            
              apex_json.write('value', r_meu_cursor.coluna1, true);
            
            apex_json.close_object;
            
            apex_json.open_object(p_name => 'coluna2');
            
              apex_json.write('value', r_meu_cursor.coluna2, true);
            
            apex_json.close_object;
            
            apex_json.open_object(p_name => 'coluna3');
            
              apex_json.write('value', r_meu_cursor.coluna3, true);
            
            apex_json.close_object;
          
          apex_json.close_object;
        end loop;
      
      apex_json.close_array;
    
    apex_json.close_object;
  
  apex_json.close_object;
  
  
  apex_json.free_output;
  
  return v_variavel;
end;
```

Resultado em JSON:

```json
{
  "options": {
    "columns": {
      "coluna1": {
        "header": "Código",
        "alignment": "right",
        "width": 120
      },
      "coluna2": {
        "header": "Descrição",
        "alignment": "left",
        "width": 250
      },
      "coluna3": {
        "header": "Valor",
        "alignment": "right",
        "width": 150
      }
    },
    "paginations": {
      "type": "page",
      "pagination": 5
    }
  },
  "model": {
    "data": [
      {
        "coluna1": {
          "value": 1
        },
        "coluna2": {
          "value": "Café"
        },
        "coluna3": {
          "value": 30
        }
      },
      {
        "coluna1": {
          "value": 2
        },
        "coluna2": {
          "value": "Óleo vegetal"
        },
        "coluna3": {
          "value": 20
        }
      }
    ]
  }
}
```

*Obs: Sempre ao utilizarmos a procedure APEX\_JSON.WRITE passaremos os seguintes parâmetros: apex\_json.write('nomeCampo', valor, <span style="color: rgb(53, 152, 219);">true</span>)<span style="color: rgb(53, 152, 219);"><span style="color: rgb(0, 0, 0);">. É necessário passar <span style="color: rgb(53, 152, 219);">**true** </span>no como ultimo parâmetro, caso contrário se o valor for nulo, o campo de JSON não é escrito. </span></span>*

💡 Dessa forma a grade já mostrara os registros da tabela, caso ás colunas não estejam configuradas na sessão options, a grade tentará montar uma configuração padrão para a coluna não configurada.

# Options - Columns

Após tivermos feito ás configurações iniciais da nossa Advanced Grid, iremos declarar ás configurações de colunas como título e alinhamento. Para isso, entre o nosso CLOSE\_OBJECT e OPEN\_OBJECT que adicionamos em configurações iniciais "{}", iremos adicionar outro OPEN\_OBJECT e CLOSE\_OBJECT, aqui declararemos a sessão de configurações da grade, com um diferencial que daremos um nome para o objeto criado utilizando o parâmetro p\_name e passando o valor 'options.

```pl/sql
function fn_minha_function return clob as
declare
  v_variavel clob;
begin
  apex_json.initialize_clob_output;
  
  apex_json.open_object;
  
    apex_json.open_object(p_name => 'options');
    
    apex_json.close_object;
  
  apex_json.close_object;
  
  apex_json.free_output;

  v_variavel := apex_json.get_clob_output;
  
  return v_variavel;
end;
```

Dentro dessa sessão de options, iremos criar mais uma sessão de objeto chamada columns. Lá iremos declarar ás configurações para cada coluna da grade. Feito isso, iremos adicionar dentro de columns a sessão de objeto da coluna em que iremos configurar, passaremos o nome da coluna na tabela como parâmetro em p\_name na função open\_object.  
  
Exemplo:   
\- Temos a tabela PRODUTOS com uma coluna chamada COD\_PRODUTO, iremos adicionar dessa forma <span style="background-color: rgb(0, 0, 0); color: rgb(206, 212, 217);"> APEX\_JSON.OPEN\_OBJECT( P\_NAME =&gt; 'cod\_produto'); </span>.

  
Dentro dela, iremos adicionar ás configurações da coluna especifica como:  
  
**header:** Título da coluna  
**alignment:** Alinhamento da coluna. Podemos utilizar valores como: left, center e right. **width:** Largura da coluna

  
Para isso, dentro do objeto da coluna que criamos, iremos utilizar a função <span style="background-color: rgb(0, 0, 0); color: rgb(206, 212, 217);"> APEX\_JSON.WRITE; </span> essa função é responsável por inserir valores dentro de objetos e arrays.  
  
Para isso iremos escrever dessa forma:  
<span style="background-color: rgb(0, 0, 0); color: rgb(206, 212, 217);"> APEX\_JSON.WRITE('header', 'Código'); </span>

<span style="background-color: rgb(0, 0, 0); color: rgb(206, 212, 217);"> APEX\_JSON.WRITE('alignment', 'right');</span>

```pl/sql
function fn_minha_function return clob as
declare
  v_variavel clob;
begin
  apex_json.initialize_clob_output;
  
  apex_json.open_object;
  
    apex_json.open_object(p_name => 'options');
    
      apex_json.open_object(p_name => 'columns');
      
        apex_json.open_object(p_name => 'cod_produtos');
        
          apex_json.write('header', 'Código', true);
          apex_json.write('alignment', 'right', true);
          apex_json.write('width', 250, true);
        
        apex_json.close_object;
      
      apex_json.close_object;
    
    apex_json.close_object;
  
  apex_json.close_object;
  
  v_variavel := apex_json.get_clob_output;
  
  apex_json.free_output;
  
  return v_variavel;
end;
```

Resultado em JSON

```json
{
  "options": {
    "column": {
      "cod_produto": {
        "header": "Código",
        "alignment": "right",
        "width": 250
      }
    }
  }
}
```

⚙️ Feito isso está feita a sua configuração de coluna. Sempre que houver uma nova linha de registro, essa configuração será aplicada na coluna da linha e do cabeçalho.

# Options - Columns - Frozen column

##### Em Advanced Grid podemos fazer configurações em cada coluna a nível de célula. Dentre essas configurações, uma delas é o frozen column, permitindo mostrar quea grade congele a coluna para navegarmos dentre elas horizontamente sem que percamos ás colunas escolhidas de vista assim como a Interactive Grid.  
  


Para isso iremos habilitar a opção "frozen" da coluna em options -&gt; columns -&gt; coluna. Feito isso adicionaremos o seguinte parâmetro utilizando a função <span style="background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);"> APEX\_JSON.WRITE </span>:

**frozen:** Esse parâmetro é responsável por indicar se a coluna está congelada ou não, iremos passar o valor **true** para habilitarmos.  
  
  
Para configurarmos a customização por coluna será dessa forma:

```pl/sql
function fn_minha_function return clob as
declare
  cursor c_meu_cursor is
    select tabela.coluna1
      from owner.tabela tabela;

  v_variavel clob;
begin
  apex_json.initialize_clob_output;
  
  v_variavel := apex_json.get_clob_output;
  
  
  apex_json.open_object;

    apex_json.open_object(p_name => 'options');

      apex_json.open_object(p_name => 'columns');

        apex_json.write('header', 'Coluna 1', true);
        apex_json.write('alignment', 'left', true);
        apex_json.write('width', 120, true);
        apex_json.write('frozen', true);

      aepx_json.close_object;

    apex_Json.close_object;

    apex_json.open_object(p_name => 'model');
    
      apex_json.open_array(p_name => 'data');
      
        for r_meu_cursor in c_meu_cursor loop
          apex_json.open_object;
          
            apex_json.open_object(p_name => 'coluna1');
            
              apex_json.write('value', r_meu_cursor.coluna1, true);
            
            apex_json.close_object;
          
          apex_json.close_object;
        end loop;
      
      apex_json.close_array;
    
    apex_json.close_object;
  
  apex_json.close_object;
  
  
  apex_json.free_output;
  
  return v_variavel;
end;
```

Resultado em JSON:

```json
{
  "options": {
    "columns": {
      "coluna1": {
        "header": "Código",
        "alignment": "right",
        "width": 120,
        "frozen": true
      }
    },
    "paginations": {
      "type": "page",
      "pagination": 5
    }
  },
  "model": {
    "data": [
      {
        "coluna1": {
          "value": 1
        }
      }
    ]
  }
}
```

❄️ Feito isso está pronto o seu context menu!

# Options - Columns - readOnlyStyle

##### Em Advanced Grid possuimos a opção de habilitarmos o estilo de linhas em "read only", deixando todas ás células da coluna escolhido com um estilo desabilitado.  
  


Para isso, iremos passar o seguinte parâmetro dentro de uma sessão de coluna declarada em **columns** dentro de **options** utilizando a função <span style="background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);"> **APEX\_JSON.WRITE** </span>:

 **readOnlyStyle:** <span style="color: rgb(53, 152, 219);">**boolean** <span style="color: rgb(0, 0, 0);">- Passaremos **true** para habilitarmos e por padrão virá desabilitada como **false**</span></span>

Para configurarmos a customização de coluna com o estilo read only em PL/SQL será dessa forma:

```pl/sql
function fn_minha_function return clob as
declare
  cursor c_meu_cursor is
    select tabela.coluna1
      from owner.tabela tabela;

  v_variavel clob;
begin
  apex_json.initialize_clob_output;
  
  v_variavel := apex_json.get_clob_output;
  
  
  apex_json.open_object;

    apex_json.open_object(p_name => 'options');

      apex_json.open_object(p_name => 'columns');

        apex_json.write('header', 'Coluna 1', true);
        apex_json.write('alignment', 'left', true);
        apex_json.write('width', 120, true);
        apex_json.write('readOnlyStyle', true);

      aepx_json.close_object;

    apex_Json.close_object;

    apex_json.open_object(p_name => 'model');
    
      apex_json.open_array(p_name => 'data');
      
        for r_meu_cursor in c_meu_cursor loop
          apex_json.open_object;
          
            apex_json.open_object(p_name => 'coluna1');
            
              apex_json.write('value', r_meu_cursor.coluna1, true);
            
            apex_json.close_object;
          
          apex_json.close_object;
        end loop;
      
      apex_json.close_array;
    
    apex_json.close_object;
  
  apex_json.close_object;
  
  
  apex_json.free_output;
  
  return v_variavel;
end;
```

Resultado em JSON:

```json
{
  "options": {
    "columns": {
      "coluna1": {
        "header": "Código",
        "alignment": "right",
        "width": 120,
        "readOnlyStyle": true
      }
    },
    "paginations": {
      "type": "page",
      "pagination": 5
    }
  },
  "model": {
    "data": [
      {
        "coluna1": {
          "value": 1
        }
      }
    ]
  }
}
```

📖 Feito isso, está concluido a sua coluna com o estilo em read only

# Options - Paginations

Em Advanced Grid, podemos declarar configurações para a sua paginação como tipo de paginação e quantidade de linhas. Para isso, dentro da sessão do objeto options, iremos criar dentro dela a sessão paginations utilizando dessa forma:  
  
<span style="background-color: rgb(0, 0, 0); color: rgb(206, 212, 217);"> APEX\_JSON.OPEN\_OBJECT( P\_NAME =&gt; 'paginations'); </span>

dentro dela criaremos uma nova sessão para configurações de linhas, para isso iremos chamar novamente a função dessa forma:  
  
<span style="background-color: rgb(0, 0, 0); color: rgb(206, 212, 217);"> APEX\_JSON.OPEN\_OBJECT( P\_NAME =&gt; 'rows'); </span>

Feito isso, podemos informar os seguintes parâmetros de configurações:  
  
**type:** Tipo de paginação na grade. Podemos informar os tipos **scroll** e **page**.

**pagination:** Essa opção funcionara somente se o tipo de paginação for do tipo page, pois nessa opção informaremos a quantidade de linhas a serem exibidas por página. Com o mínimo 5 linhas a serem exibidas.

```pl/sql
function fn_minha_function return clob as
declare
  v_variavel clob;
begin
  apex_json.initialize_clob_output;
  
  apex_json.open_object;
  
    apex_json.open_object(p_name => 'options');
    
      apex_json.open_object(p_name => 'columns');
      
        apex_json.open_object(p_name => 'cod_produtos');
        
          apex_json.write('header', 'Código', true);
          apex_json.write('alignment', 'right', true);
          apex_json.write('width', 250, true);
        
        apex_json.close_object;
      
      apex_json.close_object;
      
      apex_json.open_object(p_name => 'paginations');
        
        apex_json.open_object(p_name => 'rows'); 
        
          apex_json.write('type', 'page', true);
          apex_json.write('pagination', 5, true);

        apex_json.close_object;
      
      apex_json.close_object;
    
    apex_json.close_object;
  
  apex_json.close_object;

  v_variavel := apex_json.get_clob_output;
  
  apex_json.free_output;
  
  return v_variavel;
end;
```

Resultado em JSON:

```json
{
  "options": {
    "columns": {
      "header": "Código",
      "alignment": "right",
      "width": 250
    },
    "paginations": {
      "rows": {
        "type": "page",
        "pagination": 5
      }
    }
  }
}
```

Feito isso está pronta a suas configurações de páginas na grade 📃.

# Options - Style - Theme

##### Em Advanced Grid podemos informar o tema de estilização a sua estilização, cada uma fazendo com que cada item da grade tenha seu tamanho específico.  
  


Para isso iremos informar a opção "theme" da grade em options -&gt; style -&gt; theme. Feito isso adicionaremos o seguinte parâmetro utilizando a função <span style="background-color: rgb(0, 0, 0); color: rgb(236, 240, 241);"> APEX\_JSON.WRITE </span>:

**ag-fat:** O maior tamanho de layout disponível para configurar na grade, com esse tamanho, todos os elementos visíveis são maiores e explicitos.

[![{B844EEB1-5C09-46F8-B644-5BD0FDD52649}.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-01/scaled-1680-/b844eeb1-5c09-46f8-b644-5bd0fdd52649.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-01/b844eeb1-5c09-46f8-b644-5bd0fdd52649.png)

**ag-slim:** Tamanho mediano e configurado por padrão na grade. Com esse tamanho é ganho um maior espaço na tela sendo possível posicionar mais elementos no campo de visão do usuário.

[![{EB377298-5DB0-4DE9-BE6F-CD42646ECBBF}.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-01/scaled-1680-/eb377298-5db0-4de9-be6f-cd42646ecbbf.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-01/eb377298-5db0-4de9-be6f-cd42646ecbbf.png)

**ag-ultra-slim:** Sendo o menor tamanho disponíbilizado, com esse tema, o layout da grade fica ainda menor, podendo ganhar o maior espaço para posicionar elementos no campo de visão do usuário.

[![{5C66BC73-E777-421A-BF57-283AF4A0C66D}.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-01/scaled-1680-/5c66bc73-e777-421a-bf57-283af4a0c66d.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-01/5c66bc73-e777-421a-bf57-283af4a0c66d.png)

Para configurarmos a customização do tema em PL/SQL será dessa forma:

```pl/sql
function fn_minha_function return clob as
declare
  cursor c_meu_cursor is
    select tabela.coluna1
      from owner.tabela tabela;

  v_variavel clob;
begin
  apex_json.initialize_clob_output;
  
  v_variavel := apex_json.get_clob_output;
  
  
  apex_json.open_object;

    apex_json.open_object(p_name => 'options', true);

      apex_json.open_object(p_name => 'style', true);

        apex_json.write('theme', 'ag-slim', true);

      apex_json.close_object;

    apex_Json.close_object;
  
  apex_json.close_object;
  
  
  apex_json.free_output;
  
  return v_variavel;
end;
```

Resultado em JSON:

```json
{
  "options": {
    "style": {
      "theme": "ag-slim"
    }
  }
}
```

🎨 Feito isso, está pronto a sua configuração de tema para a Advanced Grid

# Options - Toolbar

##### Em Advanced Grid podemos configurar a nossa toolbar para ser exibida e exibir suas opções da grade.

Para implementarmos a sessão de configuração da toolbar abriremos um objeto dentro de options utilizando a função **<span style="background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);"> APEX\_JSON.OPEN\_OBJECT </span>** passando **toolbar** como valor do parâmetro.

Após isso, temos algumas opções que podem ser configuradas. Dentre elas são:  
  
**showToolbar:** Nesse parâmetor informaremos **true** ou **false** para ser exibido a região de toolbar na grade

\- <span style="color: rgb(45, 194, 107);">**TRUE**</span>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-01/scaled-1680-/axkimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-01/axkimage.png)

\- <span style="color: rgb(224, 62, 45);">**FALSE**</span>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-01/scaled-1680-/IU8image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-01/IU8image.png)

Para configurarmos a customização da toolbar em PL/SQL será dessa forma:

```pl/sql
function fn_minha_function return clob as
declare
  v_variavel clob;
begin
  apex_json.initialize_clob_output;
  
  v_variavel := apex_json.get_clob_output;
  
  
  apex_json.open_object;

    apex_json.open_object(p_name => 'options');

      apex_json.open_object(p_name => 'toolbar');

        apex_json.write('showToolbar', true);

      apex_json.close_object;

    apex_Json.close_object;
  
  apex_json.close_object;
  
  
  apex_json.free_output;
  
  return v_variavel;
end;
```

Resultado em JSON:

```json
{
  "options": {
    "toolbar": {
      "showToolbar": true
    }
  }
}
```

🧰 Feito isso, está pronto a sua configuração de toolbar para a Advanced Grid

# Toolbar - Actions

##### Em Advanced Grid possuimos o botão de "Ações", na qual podemos executar funcionalidades da grade como exportação de relatório em Excel (.xlsx) por exemplo.  
  


Para isso, abriremos a sessão **actions** utilizando a função **<span style="background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);"> APEX\_JSON.OPEN\_OBJECT </span>**. Dentro do objeto podemos informar os parâmetros de ações como por exemplo:   
  
**showActionsButton: <span style="color: rgb(53, 152, 219);">boolean</span>** - A opção por padrão virá ativa, mas podemos passar o valor <span style="color: rgb(45, 194, 107);">**true**</span>/<span style="color: rgb(224, 62, 45);">**false** </span>para deixarmos o botão visível. O botão de ações será responsável pelas demais ações, caso todas ás ações estejam desabilitadas ele também será desabilitado.

**showDownloadReport: <span style="color: rgb(53, 152, 219);">boolean </span>**- Por padrão virá habilitado, mas podemos passar o valor <span style="color: rgb(45, 194, 107);">**true**</span>/<span style="color: rgb(224, 62, 45);">**false** </span>para deixarmos a opção visível. Essa opção é responsável pela exportação de relatório da grade.

Para configurarmos a customização das ações em PL/SQL será dessa forma:

```pl/sql
function fn_minha_function return clob as
declare
  v_variavel clob;
begin
  apex_json.initialize_clob_output;
  
  v_variavel := apex_json.get_clob_output;
  
  
  apex_json.open_object;

    apex_json.open_object(p_name => 'options');

      apex_json.open_object(p_name => 'toolbar');

        apex_json.open_object(p_name => 'actions');

          apex_json.write('showActionsButton', true);

          apex_json.write('showDownloadReport', true);

        apex_json.close_object;

      apex_json.close_object;

    apex_Json.close_object;
  
  apex_json.close_object;
  
  
  apex_json.free_output;
  
  return v_variavel;
end;
```

Resultado em JSON:

```json
{
  "options": {
    "toolbar": {
      "actions": {
        "showActionsButton": true,
        "showDownloadReport": true
      }
    }
  }
}
```

⚙️ Feito isso, está concluido a sua configuração do botão e ações

# Toolbar - Search Field

##### Em Advanced Grid possuimos o campo de pesquisa na toolbar, permitindo fazer buscas de linhas com o valor de uma das colunas digitado.

Para isso, iremos abrir uma sessão de objeto utilizando a função **<span style="color: rgb(236, 240, 241); background-color: rgb(0, 0, 0);"> APEX\_JSON.OPEN\_OBJECT</span>**<span style="color: rgb(236, 240, 241); background-color: rgb(0, 0, 0);"> </span> passando como parâmetro **searchField**. Após isso iremos informar os seguintes parâmetros:

**showSearchField: <span style="color: rgb(53, 152, 219);">boolean</span>** - Parâmetro responsável por exibir o campo de pesquisa, passaremos **<span style="color: rgb(22, 145, 121);">true</span>** ou **<span style="color: rgb(186, 55, 42);">false</span>** como valor. Como padrão o valor será **<span style="color: rgb(22, 145, 121);">true</span>**

  
**ignoreCaseSensitive: <span style="color: rgb(53, 152, 219);">boolean</span>** - Parâmetro responsável pela pesquisa de colunas em linhas, com ele, a grade poderá iniciar com a opção de distinguir palavras maiúsculas de minúsculas. Passaremos **<span style="color: rgb(22, 145, 121);">true</span>** ou **<span style="color: rgb(186, 55, 42);">false</span>** como valor, por padrão o valor será <span style="color: rgb(22, 145, 121);">**true**</span>.

**searchFor:** **<span style="color: rgb(53, 152, 219);">String</span>** - Parâmetro responsável pela pesquisa de colunas em linhas de forma geral ou específica. Com ele, a grade poderá inicial com a pesquisa em alguma coluna específica. Passaremos a **key** da coluna em **model.data** para pesquisa específica ou **all** para todas ás colunas. Por padrão o valor será <span style="color: rgb(53, 152, 219);">**all**</span>.

Para configurarmos a customização do campo de pesquisa em PL/SQL será dessa forma:

```pl/sql
function fn_minha_function return clob as
declare
  v_variavel clob;
begin
  apex_json.initialize_clob_output;
  
  v_variavel := apex_json.get_clob_output;
  
  
  apex_json.open_object;

    apex_json.open_object(p_name => 'options');

      apex_json.open_object(p_name => 'toolbar');

        apex_json.open_object(p_name => 'searchField');

          apex_json.write('showSearchField', true);

          apex_json.write('ignoreCaseSensitive', true);

          apex_json.write('searchFor', 'nome');

        apex_json.close_object;

      apex_json.close_object;

    apex_json.close_object;

    apex_json.open_object('model');

      apex_json.open_array('data');

        apex_json.open_object('nome');

        ...

        apex_json.close_object;

      apex_json.close_array;

    apex_json.close_object;
  
  apex_json.close_object;
  
  
  apex_json.free_output;
  
  return v_variavel;
end;
```

Resultado em JSON:

```json
{
  "options": {
    "toolbar": {
      "searchField": {
        "showSearchField": true,
        "ignoreCaseSensitive": true,
        "searchFor": "nome"
      }
    }
  }
  "model": {
    "data": [
      "nome": {
        ...
      }
    ]
  }
}
```

🔎 Feito isso, está pronto a sua configuração de pesquisa para a Advanced Grid

# Zebragem de linhas

##### Em Advanced Grid possuimos a opção de habilitarmos a zebragem por linhas. Ao habilitar a opção, deixamos a linha com um tom levemente "acinzentado" em linhas impares.  


Para isso, iremos abrir uma sessão de objeto dentro de options utilizando a função <span style="background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);"> **APEX\_JSON.OPEN\_OBJECT** </span> passando como parâmetro **rows**. Após isso iremos informar os seguinte parâmetro:

**enableZebraStriping: <span style="color: rgb(53, 152, 219);">boolean <span style="color: rgb(0, 0, 0);"> </span></span>**<span style="color: rgb(53, 152, 219);"><span style="color: rgb(0, 0, 0);">- Passaremos o valor **true** para habilitar e por padrão virá com o valor **false** desabilitado.</span></span>

Para configurarmos a customização da zebragem em PL/SQL faremos dessa forma:

```pl/sql
function fn_minha_function return clob as
declare
  v_variavel clob;
begin
  apex_json.initialize_clob_output;
  
  v_variavel := apex_json.get_clob_output;
  
  
  apex_json.open_object;

    apex_json.open_object(p_name => 'options');

      apex_json.open_object(p_name => 'rows');

        apex_json.write('enableZebraStriping', true);

      apex_json.close_object;

    apex_json.close_object;
  
  apex_json.close_object;
  
  
  apex_json.free_output;
  
  return v_variavel;
end;
```

Resultado em JSON:

```json
{
  "options": {
    "rows": {
      "enableZebraStriping": true
    }
  }
}
```

🦓 Feito isso, sua zebragem por linhas está concluida

# CSS Rápido

Este capítulo foi criado para algumas funcionalidades que temos em CSS que necessitamos por limitações do APEX.

<span>Colocaremos elas em </span>**Classes CSS**<span> que fica em </span>**Appearance** de cada item, independente de ser um botão, region ou coluna. Deve ser analisado cada caso

# Alinhar Botão / Checkbox

**Para que os itens sejam alinhados disso:**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/scaled-1680-/JItimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/JItimage.png)

---

**Para isso:**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/scaled-1680-/EgHimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/EgHimage.png)

---

**Basta usar a classe:**

```
cs-flex-end
```

No **"Column CSS Classes"** do item ou botão em questão, assim:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/scaled-1680-/8vFimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/8vFimage.png)

# Apex Disabled

Quando necessário ter um input **Read Only** mas precisa receber dados utilizaremos a classe `apex_disabled`

**Exemplo:**

Nessa tela teremos que colocar um valor na coluna de <u>Nome do Funcionário</u> quando for selecionado o <u>usuário</u>, porém esse campo não pode ser ativado, para isso colocaremos na **CSS Classes** da coluna a classe **apex\_disabled** para termos uma impressão de <u>Read Only</u>, porém não é um ***<u>Read Only</u>*** de fato!

---

**Tela exemplo ➝** [40451:80](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-operacoes-financeiras/autorizacoes-usuario?session=9214413713697)

# btnWarning

Utilizaremos a Classe 'btn-warning' quando teremos uma pendência que o usuário deva visualizar.

Colocaremos sua condição para ser ativada e faremos ela por meio de uma **Dynamic Action** com a *action* de **Add Class**, a classe adicionada será `btn-warning.`

Por exemplo, nessa tela a condição para ter o aviso no botão é caso tenha alguma procuração com o status *pendente*

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/scaled-1680-/SsFimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/SsFimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/scaled-1680-/jqPimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/jqPimage.png)

Fiz um cursor que retorna '1' caso tenha pelo menos uma procuração pendente, e fiz a condição da **Dynamic Action**, via Client-Side Ciodition, caso o valor do item seja 1 logo fará o **Add Class**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/scaled-1680-/0Hfimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-09/0Hfimage.png)

Ele fará a *action* **Add Class** e adicionará a classe `<em>btn-warning</em>` no botão *SOLICITACAO*

<p class="callout info">Nesse caso como é no carregamento da página a verificação habilitei o **Fire on Inicialization**</p>

---

**Tela exemplo ➝** [40202:60](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-procuracoes/gerenciamento-de-solicitacoes?session=9214413713697)

# Show in Dialog

A classe **CSS** `<em>show-in-dialog</em>` serve para em campos de que possuem muito conteúdo (normalmente campos de "observação") dentro de uma grid facilite a visualização do conteúdo trazendo ele em uma modal a partir do Double-click na coluna.

<p class="callout warning">Para que a classe funcione, a grid **não pode ter as operações "Add Row" e nem "Update Row"** habilitadas. Se for uma grid que possua **apenas o delete a classe funciona.**</p>

# Custom Templates

<p class="callout warning">**ATENÇÃO:** A criação de templates personalizados deve ser **analisada previamente e comunicada ao time P&amp;D** para evitar problemas com a publicação de tema da aplicação 40000-CS-SCAFFOLD.</p>

Quando for necessário criar um Custom Template, deve-se criá-lo no Scaffold, e depois publicar o tema do mesmo.

# Debug APEX

O debug em Apex é o processo de rastrear e entender o que está acontecendo com seu código Apex dentro da plataforma, geralmente para diagnosticar problemas, encontrar bugs ou entender comportamentos inesperados

# Ferramentas para Debug

#### **Comando para retornar textos na tela do Debug** 

---

```javascript
APEX_DEBUG.ERROR('Mensagem apresentada na tela do debug');
```

<div class="code-toolbar" id="bkmrk--1"><div class="toolbar"></div></div>####  **Como Utilizar o Debug**

---

No PL/SQL Code quando necessário retornar resultado, basta colocar o comando acima.

**Exemplo:**

```
Begin
    APEX_DEBUG.ERROR('Monaco');
End;
```

#### **Como Acessar o Resultado**

---

No Apex na ferramenta Debug tem o comando de acesso "**Depurar"** &gt; **Exibir Depuração** / **Ativar Depuração**.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/HwBjiGimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/HwBjiGimage.png)

[![Sem título.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/sem-titulo.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/sem-titulo.png)

[![Sem título.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/TVnsem-titulo.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/TVnsem-titulo.png)

# Diálogos

# Diálogos de Confirmação

O APEX implementa diversos **templates para diálogos** de alerta, informação e sucesso, mas não possui um template para um diálogo de confirmação.

<p class="callout success">⭐ Para saber as boas práticas, tipos e qual diálogo utilizar. **Acesse:** [Diálogos](https://wiki.cscompusoftware.com.br/books/erp-guideline-de-uiux/page/dialogos "Diálogos")</p>

##### **Configure desta forma:**

- **Dê preferência a ação dinâmica "Confirm" do APEX**

<p class="callout warning">Diálogos invocados por `apex.message.*` **não são configuráveis** **dessa forma.**</p>

- Style: **Default**
- Icon: **fa-lg fa-question-circle u-hot-text**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/ZWTimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/ZWTimage.png)

**O resultado final deve se parecer com isso:** [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/ruaimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/ruaimage.png)

# DML DINÂMICO

<span style="font-family: Google Sans, serif;">A package pkg\_apex\_dml foi desenvolvida para automatizar operações de DML em ambientes **Oracle APEX**. Ela utiliza metadados da aplicação para identificar colunas, chaves primárias e tipos de dados, permitindo a execução dinâmica de comandos **SQL** via **DBMS\_SQL** e **EXECUTE IMMEDIATE**.</span>

## <span style="font-family: Google Sans, serif;">Visão Geral das Funcionalidades</span>

- <span style="font-family: Google Sans, serif;">**DML Dinâmico:**</span><span style="font-family: Google Sans, serif;"> Suporta INSERT, UPDATE e DELETE.</span>
- <span style="font-family: Google Sans, serif;">**Otimização de Update:**</span><span style="font-family: Google Sans, serif;"> Compara valores antigos com os novos (incluindo CLOB) e só executa o update se houver mudanças reais.</span>
- <span style="font-family: Google Sans, serif;">**Flexibilidade de Identificação:**</span><span style="font-family: Google Sans, serif;"> Suporta identificação de registros via </span><span style="font-family: Google Sans, serif;">**RowID**</span><span style="font-family: Google Sans, serif;"> ou via </span><span style="font-family: Google Sans, serif;">**Primary Key**</span><span style="font-family: Google Sans, serif;"> definida no APEX.</span>
- <span style="font-family: Google Sans, serif;">**Integração Nativa:**</span><span style="font-family: Google Sans, serif;"> Lê automaticamente as configurações de regiões de formulário (FORM) ou Grids Interativos (IG).  
    </span>

## <span style="font-family: Google Sans, serif;">Como usar no Oracle APEX</span>

<span style="font-family: Google Sans, serif;">Existem três exemplos principais de invocar esta procedure dentro de um processo de página (**Page Process**).</span>

<p class="callout info">**<span style="font-family: Google Sans, serif;">Exemplo 01 : Em uma Interactive Grid ( IG ) </span>**</p>

<span style="font-family: Google Sans, serif;">Esta é a forma mais comum. Use este código em um processo do tipo </span><span style="font-family: Google Sans, serif;">**"Interactive Grid - Automatic Row Processing"**</span><span style="font-family: Google Sans, serif;">, substituindo o alvo nativo por um código **PL/SQL**.</span>

### <span style="font-family: Google Sans, serif;">Configuração do Processo : </span>

- <span style="font-family: Google Sans, serif;">**TYPE**: Interactive Grid - Automatic Row Processing ( DML )</span>
- <span style="font-family: Google Sans, serif;">**TARGET** : PL/SQL Code  
    </span>

**SQL**

```pl/sql
declare 
vr_rowid   rowid  := :rowid;   -- Passagem por referência caso não informado ele irá pegar a PK e fazer um where dinâmico 

begin
    csweb.pkg_apex_dml.pr_apex_dml(
        pv_tabela      => 'NOME_DA_SUA_TABELA',
        pv_tipo_regiao => 'IG',
        pv_region_name => 'NOME_ESTATICO_DA_REGIAO', -- Static ID da Região   
        pv_rowid       => vr_rowid 
  );
end;
```

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-04/scaled-1680-/8nhimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-04/8nhimage.png)

<p class="callout info">**Exemplo 02 :** Em um Formulário Simples ( **FORM** )</p>

<span style="font-family: Google Sans, serif;">Ideal para páginas de cadastro único onde os itens da página estão vinculados a colunas da tabela.</span>

Configuração do Processo:

- <span style="font-family: Google Sans, serif;">**TYPE:** Form - Automatic Row Processing ( DML )</span>
- **TARGET TYPE :** PL/SQL Code

**SQL**

```pl/sql
begin
    csweb.pkg_apex_dml.pr_apex_dml(
        pv_tabela      => 'MINHA_TABELA_CADASTRO',
        pv_tipo_regiao => 'FORM',
        pv_region_name =>  'NOME_ESTATICO_DA_REGIAO',
        pv_status      =>  :APEX$ROW_STATUS,    
        pv_rowid       => :P1_ROWID
    );
end;
```

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-04/scaled-1680-/WCUimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-04/WCUimage.png)

<p class="callout info">**Forma 03 :** Chamada Manual ( Passando String ) </p>

<span style="font-family: Google Sans, serif;">Útil para integrações via **Web Services**, processos em lote ou quando você quer definir manualmente quais colunas serão afetadas, sem depender dos metadados da página **APEX**.</span>

**SQL**

```pl/sql
declare
    v_rid rowid;
begin
    csweb.pkg_apex_dml.pr_apex_dml(
        pv_tabela      => 'MINHA_TABELA',
        pv_colunas_str => 'NOME;EMAIL;SETOR',        -- Colunas separadas por ';'
        pv_valores_str => 'João Silva;joao@ex.com;TI', -- Valores na mesma ordem
        pv_status      => 'C',                       -- 'C' para Insert
        pv_rowid       => v_rid
    );
end;
```

## <span style="font-family: Google Sans, serif;">Parâmetro da Procedure</span>

<p class="callout info">**<span style="font-family: Google Sans, serif;">pr\_apex\_dml</span>**</p>

<table border="1" id="bkmrk-par%C3%A2metro-tipo-descr" style="border-collapse: collapse; width: 100%;"><colgroup><col style="width: 33.3333%;"></col><col style="width: 33.3333%;"></col><col style="width: 33.3333%;"></col></colgroup><tbody><tr><td class="align-center">**Parâmetro**</td><td class="align-center">**Tipo**</td><td class="align-center">**Descrição**</td></tr><tr><td><span style="font-family: Google Sans, serif;">pv\_tabela</span>

</td><td>IN</td><td><span style="font-family: Google Sans, serif;">Nome da tabela no banco de dados (ex: 'CAD\_CLIENTES').</span>

</td></tr><tr><td><span style="font-family: Google Sans, serif;">pv\_colunas\_str</span>

</td><td>IN</td><td><span style="font-family: Google Sans, serif;">String com nomes das colunas separados por ;. Usado na Forma 3.</span>

</td></tr><tr><td><span style="font-family: Google Sans, serif;">pv\_valores\_str</span>

</td><td>IN</td><td><span style="font-family: Google Sans, serif;">String com valores correspondentes separados por ;.</span>

</td></tr><tr><td><span style="font-family: Google Sans, serif;">pv\_tipo\_regiao</span>

</td><td>IN</td><td><span style="font-family: Google Sans, serif;">Origem dos metadados: 'IG' (Grid) ou 'FORM' (Formulário).</span>

</td></tr><tr><td><span style="font-family: Google Sans, serif;">pv\_status</span>

</td><td>IN</td><td><span style="font-family: Google Sans, serif;">Ação: 'C' ou 'I' (Insert), 'U' (Update), 'D' (Delete). caso não informado ele irá pega o valor default do </span><span style="font-family: Google Sans, serif;">APEX$ROW\_STATUS</span>

</td></tr><tr><td><span style="font-family: Google Sans, serif;">pv\_rowid</span>

</td><td>IN OUT</td><td><span style="font-family: Google Sans, serif;">O RowID do registro. Se nulo no Update/Delete, a PK será usada.</span>

</td></tr><tr><td><span style="font-family: Google Sans, serif;">pv\_region\_name</span>

</td><td>IN</td><td><span style="font-family: Google Sans, serif;">Static ID ou Nome da região no APEX para filtrar os itens/colunas.</span>

</td></tr></tbody></table>

## <span style="font-family: Google Sans, serif;">Diferenciais de Lógica Interna</span>

<p class="callout info">**<span style="font-family: Google Sans, serif;">Tratamento de Tipos (fn\_formatar\_valor)</span>**</p>

<span style="font-family: Google Sans, serif;">A **package** identifica automaticamente se a coluna é numérica ou string:</span>

- **Números** : Substitui vírgula por ponto para garantir compatibilidade com o motor **SQL**
- **String** : Adiciona aspas simples (') e trata escapes de aspas simples internas
- **Nulos** : Converte a string '**NULL**' ou vazios no valor NULL real do banco

### **Comparação Inteligente** 

<span style="font-family: Google Sans, serif;">Antes de dar um UPDATE, a procedure executa um SELECT dinâmico do valor atual. Ela compara o valor do banco com o valor vindo da tela usando **dbms\_lob.compare**. Se os valores forem idênticos, a coluna é removida da cláusula SET, reduzindo o overhead de redo log e triggers de auditoria desnecessários.</span>

## Cuidados Importantes

- **Static ID :** <span style="font-family: Google Sans, serif;">No Interactive Grid, certifique-se de preencher o campo </span><span style="font-family: Google Sans, serif;">**Static ID**</span><span style="font-family: Google Sans, serif;"> nas propriedades da região e passar esse mesmo nome no parâmetro **pv\_region\_name.**  
      
    </span>
- **Primary Key :** <span style="font-family: Google Sans, serif;">Se não usar RowID, as colunas na sua região IG ou **Form** </span><span style="font-family: Google Sans, serif;">devem</span><span style="font-family: Google Sans, serif;"> estar marcadas como "Primary Key = Yes" para que o WHERE seja construído corretamente.  
    </span>

<p class="callout warning">**Atenção ao uso:**  
**Esta solução foi desenhada para casos pontuais onde o processo nativo do APEX encontra limitações. Não é indicado para uso geral em formulários simples, onde as funcionalidades padrão da plataforma já atendem perfeitamente.**  
</p>

# Editor para Campo Fórmula

# APEX VS Monaco Editor

APEX VS Monaco Editor é o **plug-in padrão** que utilizaremos para edições de formulas dentro do ERP. Ele traz o código indentado e colorido, trazendo as principais funcionalidades de *code editor* para facilitar a criação e manutenção em campos fórmulas*.*

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/PFgimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/PFgimage.png)

Ele pode ser utilizado de 2 maneiras:

#### **Modal**

---

Para acomodar o editor em um tamanho mais confortável para digitação.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/4fQimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/4fQimage.png)

#### **In Page**

---

Para demonstração de pequenas fórmulas.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/u0aimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/u0aimage.png)

<p class="callout success">**⭐ Boas práticas de UX - Acesse:** [Monaco Editor](https://wiki.cscompusoftware.com.br/books/erp-guideline-de-uiux/page/textos-longos#bkmrk-markdown-editor---mo)</p>

#### **Como Usar**

---

O APEX Monaco Editor é um plug-in do tipo *region,* então para utiliza-lo você deve criar uma nova região e alterar o tipo para *"**APEX-VS-Monaco-Editor \[Plug-In\]"*** .

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/4c5image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/4c5image.png)

 Após alterar o tipo de região o plug-in passa a funcionar.

##### **Ele funciona da seguinte forma**

Para carregar os valores no editor é necessário utilizar uma *SQL* ou realizar um ***bind*** de um *page item.* Como demonstrado abaixo.

Quando informado apenas o valor da coluna *`VALUE_EDIT`* o editor será montado de forma simples, se passado o valor da coluna *`VALUE_DIFF`,* o editor será montado de forma que mostre as diferenças dos 2 códigos.

<p class="callout info">**💡** Lembrando que todo o valor que você utilizar através de ***bind***, você **deve informá-los no campo** ***Page Items to Submit**,* **caso contrario o componente** **não irá resgatar os valores**.</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/m8Eimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/m8Eimage.png)

Já na aba ***Attributes**,* temos algumas opções de customização do editor, como altura, linguagem, tema e botões.

<p class="callout success">⭐ O padrão adotado é o tema ***Visual Studio Dark*** por se destacar melhor e indicar para o usuário que se trata de uma configuração avançada, pois se tratando de uma tela escura com **formatação de código e *highlight.***</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/GYoimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/GYoimage.png)

<p class="callout info">Na parte de botões optamos por **desabilitar o botão de** ***Switch between Single Editor and Diff-Editor*** quando se tratar de **manutenção em fórmulas**, e **habilitando ele quando utilizado em modo comparação**.   
O botão de ***Save*** pode ser habilitado dependendo do seu caso de uso.</p>

#### **Return value to item e Execute on Save**

---

Essas opções são referente ao c**omportamento do componente no momento de** ***Save**.*

Por padrão no componente não existia o atributo ***Return value to Item**.* Esse atributo foi adicionado ao componente, pois o comportamento padrão era disparar um código PL/SQL salvando o valor do editor na tabela de ***collections*** do *APEX*, sendo necessário realizar um ***select*** na tabela logo após a execução do ***Execute on Save***, tornando a implementação um pouco trabalhosa quando a tela exige uma grande quantidade de campos fórmula.

Sendo assim foi adicionado outro comportamento, quando habilitado o ***Return value to item**,* ao invés de executar um bloco PL/SQL no momento de ***Save*** ele simplesmente irá **retornar o valor diretamente para o *Page Item*** em tela, este *Page Item* deve ser do **tipo hidden**, dessa forma torna possível a utilização de uma região do tipo form para realizar o ***INSERT* e** ***UPDATE*** das informações, o campo a ser utilizado é o campo ***Page Items to Submit**.*

<p class="callout info">💡 Lembrando que neste caso você deverá informar **somente o valor de 1 Page Items to Submit.** Outra coisa que você deve fazer é **desabilitar o Value** **protect** do campo informado, pois como esse valor será alterado através do JS do componente o APEX irá reclamar que o valor foi alterado.</p>

Caso informe mais de 1 item será gerado um comportamento diferente do esperado. Podendo gerar uma ***<u>catástrofe</u>*** na sua tela ao momento de Save.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/r3Limage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/r3Limage.png)

<p class="callout warning">Esse opção ***Return value to item*** está limita ao uso de campos fórmula do tipo **varchar2 até 4k de caracteres**, quando o campo for **CLOB** é recomendado utilizar o Save através da collection para evitar problemas com quantidade alta de caracteres.</p>

#### **Executando Save do Editor**

---

##### **Para quando o campo for VARCHAR até 4000.**

Para executar o *Save* do componente você setar um ***Static ID*** para a região do componente.

 [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/I74image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/I74image.png)

Feito isso, caso você esteja salvando os dados com uma região do tipo ***Form*** você deve ir no botão que executa o ***submit*** da página e alterar a ***Action*** do botão para ***Defined by Dynamic Action.***

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/Re6image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/Re6image.png)

Lembre-se de definir um ***Name*** para o botão e também uma ***Database Action***.

No botão defina uma ***Dynamic Actions*** do tipo ***Click**,* em ***true*** adicione 2 ações uma do tipo ***Execute JavaScript Code*** e outra ***Submit Page.***

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/UYcimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/UYcimage.png)

Na ação ***Execute JavaScript Code*** defina como código javascript o seguinte trecho:

```
$('#static-id-regiao').trigger('save');
```

Substituindo o *`static-id-regiao`* pelo o ***Static ID*** que você definiu na região do editor. isso irá disparar a função do editor para salvar o conteúdo do componente.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/ZH1image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/ZH1image.png)

Na ação ***Submit Page*** defina em ***Request/Button Name*** o nome que você atribuiu ao botão no momento de criação.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/fNzimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/fNzimage.png)

Quando haver a necessidade de executar alguma validação da formula, ou executar alguma coisa após o *save* do editor. Existe o evento ***"Upload of Text finished \[APEX-VS-Monaco-Editor\]"*** que pode ser adicionado na região do editor.

Esse evento é disparado logo após o ***save*** do editor for finalizado.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/2E8image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/2E8image.png)

E no evento **adicione um FOS** para que seja executado a validação.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/tTpimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/tTpimage.png)

##### **Para quando for campo CLOB**

Quando haver a necessidade de gravar um campo CLOB, basta desabilitar a opção ***Return value to item*** nas opções do componente do editor.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/cwsimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/cwsimage.png)

Você pode utilizar de 2 formas, a primeira é realizar o ***insert* ou** ***update*** diretamente na tabela no *E**xecute on Save*** do componente, a segunda é criar um evento ***process*** e recuperar o valor diretamente na collection do APEX utilizando a SQL abaixo.

A SQL abaixo recupera o valor da collection.

```
select clob001 from apex_collections where collection_name = 'EDITOR_CODE_COLLECTION';
```

# Auto Complete Monaco

Em Oracle APEX, possuímos o plug-in APEX VS Monaco Editor, onde podemos utilizar para adicionar e editar fórmulas. Em telas há contextos onde possuímos variáveis ou valores para auxiliar na criação das fórmulas. Pensado nisso foi implementado recurso de **✨AutoComplete✨**.

[![intellisense.gif](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/intellisense.gif)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/intellisense.gif)

Função essa que permite cadastrar:

- **Keys:** Para sugestões de AutoComplete.
- **InsertText:** Para o retorno da Key direto na posição do texto no Monaco.
- **Detail:** Para título de descrição da Key de sugestões.
- **Documentation:** Para descrição da Key de sugestões.
- **Kind:** Para ícone da Key.

#### **Cadastrar um AutoComplete ao nosso Monaco**

---

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/0pAimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/0pAimage.png)

Começaremos adicionando um Static ID para o nosso Monaco. **SEMPRE** ao adicionar AutoComplete para o Monaco declare um Static ID no plug-in.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/U9Iimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/U9Iimage.png)

Feito isso, iremos criar um process no Before Header da nossa página.

Criaremos dentro do Process uma collection, onde será armazenado as informações do AutoComplete. Crie a collection e nomeie como **AUTOCOMPLETE\_COLLECTION**

```
csweb.pkg_apex_collection.pr_create_collection('AUTOCOMPLETE_COLLECTION');
```

Agora alimentaremos a nossa collection de AutoComplete com ás suas devidas informações em seus respectivos campos:

- **p\_collection\_name:** Será o nome da nossa collection criada: **AUTOCOMPLETE\_COLLECTION**
- **p\_c001:** Será o Static ID que foi declarado no Monaco.
- **p\_c002:** Será a key de sugestão para AutoComplete.
- **p\_c003:** Será o InsertText de AutoComplete ao selecionar a key.
- **p\_c004:** Será o título da Key de AutoComplete (*Campo Opcional*).
- **p\_c005:** Será a descrição da Key de AutoComplete (*Campo Opcional.* Caso o campo p\_c004 for preenchido, o campo p\_c005 herdará ás informações de tal).
- **p\_c006:** Será o ícone de sugestão da Key. (*Campo opcional*. Virá por padrão o ícone de Property. Insira sempre o nome do ícone com a primeira letra maiúscula)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/96limage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/96limage.png)

**Imagem meramente exemplar. Você pode alimentar os campos de informações da collection como desejar.**

O campo de ícone **p\_c006** há diversos ícones que você poderá escolher. Dentre eles são:

<table border="1" class="align-center" id="bkmrk-%C3%8Dcone-nome-do-%C3%8Dcone-" style="border-collapse: collapse; width: 93.5714%; height: 30px;"><colgroup><col style="width: 50.001%;"></col><col style="width: 50.001%;"></col></colgroup><thead><tr><td class="align-left">**Ícone**</td><td class="align-left">**Nome do Ícone para declarar**</td></tr></thead></table>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/dMGimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/dMGimage.png)

<p class="callout info">👀 Os ícones podem estar divergentes da imagem ou poderão haver ícones que ficaram de fora. Para isso consulte a **documentação de [Monaco da Microsoft](https://microsoft.github.io/monaco-editor/)**[.](https://microsoft.github.io/monaco-editor/) </p>

Feito os passos corretamente, está prontinho seu AutoComplete/Intellisense para o plugin do APEX VS Monaco😄

---

**Tela exemplo ➝** [40451:160](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-operacoes-financeiras/tipo-formula?session=9214413713697)-161

# Campo Fórmula na Grid

<p class="callout success">⭐ Este é o padrão para apresentar **1 (um) fórmula** ou comando SQL em grid.</p>

O padrão adotado consiste em acionar a modal da fórmula por meio de um botão.

- Caso o registro não contenha dados da SQL, o botão será exibido em <span class="ql-color-blue">azul</span> **(u-info)**, com o texto:  
    <u>Digitar comando SQL</u> ou <u>Digitar fórmula SQL  
      
    </u>
- Caso o registro já possuir dados registrados, o botão será exibido em <span class="ql-color-green">verde</span> **(u-success),** acompanhado do texto: <u>Visualizar/Editar SQL  
      
    </u>
- No caso de uma tela que exige a inserção **obrigatória** de uma fórmula, o botão será <span class="ql-color-red">vermelho </span>**(u-danger)**, acompanhado do texto: <u>Obrigatório inserir fórmula</u>

Esses botões serão adicionados na Grid como nesse exemplo:

```
'<span class="t-Button u-danger" title="Fórmula Padrão"><span> '||apex_lang.message('LBL_FORMULA_OBRIGATORIA')||' </span></span>'

 '<span class="t-Button u-info" title=" Digitar Fórmula "><span> '||apex_lang.message('LBL_DIGITAR_COMANDO_SQL')||' </span></span>'

 '<span class="t-Button u-success" title="Visualizar/Editar Fórmula"><span> '||apex_lang.message('LBL_VIZUALIZ
```

<p class="callout info">💡 Lembrando pra **não deixar o texto do label estático na SQL devido a internacionalização!**</p>

Tem que fazer a concatenação'`||apex_lang.message('NOME_TEXT_MSG')||`<span class="ql-color-yellow">', conforme o guideline: Text Messages</span>

<span class="ql-color-yellow">**(**[**https://app.clickup.com/36914160/docs/136gzg-1043/136gzg-29263)**](https://app.clickup.com/36914160/docs/136gzg-1043/136gzg-29263))</span>

Ficando dessa forma:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/uuBimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/uuBimage.png)

Lembrando de deixar o link como Query Only, e fazer o redirecionamento para a página modal criada para o Campo de Fórmula, utilizando o [plugin do Moanaco](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/apex-vs-monaco-editor).

<p class="callout success">⭐ **Saiba mais sobre as boas práticas ao utilizar o plugin:** [Textos Longos - Monaco Editor](https://wiki.cscompusoftware.com.br/books/erp-guideline-de-uiux/page/textos-longos#bkmrk-markdown-editor---mo)</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/OyXimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/OyXimage.png)

<p class="callout warning">Este novo padrão será aplicado exclusivamente quando houver **APENAS UMA fórmula SQL**, facilitando a visualização na grid para o usuário se o registro possui ou não uma fórmula SQL cadastrada.</p>

**Tela de Exemplo:** [40157:80](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-controle-analises/especies-de-praga?session=9214413713697)

# Fila de Execução

#### **Fila de Execução Simples**

---

Para utilizar a fila de execução, no botão que executará processo, em Appearance, adicione a classe CSS `cs-async` e **crie um ID** para este botão.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/7nhimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/7nhimage.png)

Adicione uma **dynamic action** com uma **Action** **Execute server-side code,** ou um **Process** atrelado ao **botão.**

No **server-side code** ou **process** chame a procedure:

```
csweb.pkg_queue.pr_adicionar_execucao_fila(
                    pn_out_id_filaexec        =>
                  , pc_bloco                  =>
                  , pv_static_id              =>
                  , pv_titulo                 =>
                  , pv_titulo_erro            =>
                  , pv_msg_sucesso            =>
                  , pv_msg_erro               =>
                  , pv_impeditivo             =>
                  , pv_notifica_usuario       =>
                  , pv_attach_session         =>
                  , pv_interrupcao_programada =>
                  , pv_interrupcao_forcada    =>
                  );
```

##### **Breve Descrição sobre os Parâmetros**

No parâmetro `pc_bloco` passe seu bloco/chamada de procedure como **string** e concatenando com os itens necessários para a execução agora também é possível utilizar itens da sessão do **APEX** dentro da sua procedure que será executada pelo job, pois dentro dos jobs está sendo "setado" a mesma **SESSION/APP\_ID/PAGE\_ID** do **Usuário** que executou o processo.

##### Exemplo

```
csweb.pkg_queue.pr_adicionar_execucao_fila(
        pn_out_id_filaexec  => :ID_FILA_EXECUCAO
      , pc_bloco            => 'owner.pkg_apex_tal.procedure_tal('''||:P10_ITEM||''');'
      , pv_static_id        => 'id_botao'
      , pv_titulo           => 'Processo tal'
      , pv_titulo_erro      => 'Erro ao processar'
      , pv_msg_sucesso      => 'Processo tal executado'
      , pv_msg_erro         => 'falha ao executar processo tal'
      , pv_impeditivo       => 'N'
      , pv_notifica_usuario => 'N');
```

- No parâmetro `pn_out_id_filaexec` coloque o **item global** **:ID\_FILA\_EXECUCAO**
- No parâmetro `pv_static_id` coloque o mesmo **ID do botão** que executa esse **server-side code/processo**.
- No parâmetro `pv_titulo` coloque um titulo adequado.
- O parâmetro `pv_impeditivo` tem como valor default 'N', passe 'S' se deseja que o usuário fique **impedido** de utilizar a tela durante a execução.
- O parâmetro `<strong>pv_notifica_usuario</strong>` tem como valor default 'N', passe 'S' se deseja que o usuário receba uma **mensagem/notificação** interna sobre o resultado da execução.
- O parâmetro `pv_interrupcao_programada` tem como valor default 'N', indica se é possível interromper o processo de forma programada. Ao definir como 'S', a interrupção será habilitada, e um botão para interromper o processo aparecerá no modal de feedback. Ao clicar neste botão, um **raise** será disparado informando que o usuário interrompeu o processo. Para habilitar essa interrupção, **é necessário que o bloco/procedure contenha passos/etapas**.
- O parâmetro `pv_interrupcao_forcada` tem como valor default 'N', indica se é possível interromper o processo de forma forçada. Ao definir como 'S', a interrupção forçada será habilitada, e um botão para interromper o processo aparecerá no modal de feedback. Ao clicar neste botão, a função **dbms\_scheduler.stop\_job** será chamada, forçando a interrupção do JOB responsável pelo processo. Essa interrupção não requer a presença de etapas no bloco/procedure.

Os demais parâmetros **não são obrigatórios**, porém convém a utilização dos mesmos caso o processo seja **impeditivo** e/ou queira uma **mensagem adequada** para o resultado da execução.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/yByimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/yByimage.png)

Caso queira **vincular** uma **Action** ao **resultado** da execução, basta adicionar um **CustomEvent** e dentro dele em **When**, no atributo **Custom Event** passe **filaExecCallback**, no atributo **Selection Type** selecione **JavaScript Expression** e passe **document.**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/8jMimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/8jMimage.png)

Esse **callback** será executado automaticamente após a **finalização** da execução, nele é possível acessar informações da fila como **ID da fila**, **ID do botão**, **titulo/msg de sucesso/msg de erro** da execução.

Essas informações podem ser acessadas através do **this.data** nas **Actions do callback** que permitam **JavaScript**.

#### **Adicionando Ações ao Fechar a Modal de Feedback**

---

Dentro do bloco de código que será executado pela fila é possível registrar passos para o feedback, esse feedback é feito pela modal de feedback e é gerado uma progress bar para cada etapa adicionada, sendo a procedure da fila sempre criará uma etapa MASTER para o processo, mas é possível alterar propriedades da MASTER também, para isso chame a procedure:

```
csweb.pkg_queue.pr_registrar_etapa(pn_passo_atual     => ,
                                   pn_qtd_passos      => ,
                                   pv_chave           => ,
                                   pv_passo_descricao => );
```

##### **Breve Descrição sobre os Parâmetros**

- `pn_passo_atual` ➝ passo atual da etapa, por exemplo: **rownum** da select de um loop dentro do bloco.
- `pn_qtd_passos` ➝ quantidade total de passos, por exemplo: **count(\*) over(\*)** da select do loop.
- `pv_chave` ➝ Identificador da etapa, podendo ser **'MASTER'** para manipular as propriedades dela ao invés de criar uma outra.
- `pv_passo_descricao` ➝ Uma descrição pequena do passo atual, por exemplo: **filtrando funcionários**.

#### **Fila de Execução com Maestro**

---

Essa fila de execução deve ser usada somente se há a necessidade de adicionar algo para ser executado em segundo plano e que seja necessário que a chamada da procedure da fila esteja dentro de um **loop**.

Para utilizar a fila de execução com maestro, dentro do seu **processo/loop**, chame a procedure:

```
csweb.pkg_queue.pr_adicionar_execucao_controlada(pc_bloco               => ,
                                                 pv_static_id           => ,
                                                 pv_titulo              => ,
                                                 pn_job_atual           => ,
                                                 pn_qtd_jobs            => ,
                                                 pv_titulo_erro         => ,
                                                 pv_msg_sucesso         => ,
                                                 pv_msg_erro            => ,
                                                 pv_notifica_usuario    => ,
                                                 pv_identificador_unico => );
```

Os parâmetros adicionais dessa procedure são para controle de quando será feita a criação do Job Maestro(Job que será responsável pelo enable dos demais Jobs)

- `pn_job_atual` ➝ Linha atual do loop, por exemplo: **rownum** da select do loop.
- `pn_qtd_jobs` ➝ Quantidade de voltas do loop, por exemplo: **count(\*) over()** da select do loop.
- `pv_identificador_unico` ➝ Necessário que seja **único** para cada volta do loop, por exemplo: uma concatenação do **rownum** com alguma **PK** da select do loop.
- `pn_job_atual e pn_qtd_jobs` tem como valor **default** **1**

# Filtro GEF

Para casos de seleção múltipla acesse: Link página multifiltro

# Como Exibir a GEF

Quando tivermos a GEF dentro de uma grid no delphi, temos dois casos para como definirmos ela na IG - Interactive Grid do APEX,

#### **Grid Read Only (Consulta)**

---

Em grids "Read Only" devemos colocar a GEF em **colunas separadas e centralizadas**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/glVimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/glVimage.png)

#### **Grid Editável**

---

Caso seja uma grid que seja possível alterar a GEF do registro, devemos colocar uma coluna **Query Only** e fazermos que quando marcarmos uma filial popular as devidas colunas.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/lhbimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/lhbimage.png)

#### **Como Fazer**

---

Devemos criar uma coluna Query Only dentro da grid que receba os valores da GEF.

##### Por que fazer isso?

Para quando a coluna receber os valores ainda aparecer o nome da filial, e **não apenas os valores da GEF**.

```
select objeto_custo_recebido.id_obj_custor
     , objeto_custo_recebido.cod_grupoempresa
     , objeto_custo_recebido.cod_empresa
     , objeto_custo_recebido.cod_filial
     --AQUI
     , objeto_custo_recebido.cod_grupoempresa || '-' || objeto_custo_recebido.cod_empresa || '-' || objeto_custo_recebido.cod_filial GEF
     --AQUI
     , objeto_custo_recebido.cod_objetocusto
     , objeto_custo_recebido.data_inicial
     , objeto_custo_recebido.data_final
from   planejamento.objeto_custo_recebido
where case when :P60_SOMENTE_ATIVOS  = 'N' then 1
           when objeto_custo_recebido.data_final is null then 1
      end = 1 
```

<p class="callout info">Esta SQL é da tela 40352:60, lembre-se de **adequar a sua SQL de forma que a sua tela deva receber**.</p>

Esta coluna nova que deixamos o *alias* como <u>GEF</u> deve ser um LOV, que possui a seguinte **SQL padrão:**

```
select cod_grupoempresa||'.'||cod_empresa||'.'||cod_filial||' - '||
       nvl(geral.fn_busca_info_gef(cod_grupoempresa, cod_empresa, cod_filial, 'FN'),
           geral.fn_busca_info_gef(cod_grupoempresa, cod_empresa, cod_filial, 'FR')) D
     , cod_grupoempresa||'-'||cod_empresa||'-'||cod_filial R
from   geral.filial vw
order  by cod_grupoempresa
     ,    cod_empresa
     ,    cod_filial
```

Agora devemos criar um evento **onChange** na coluna para quando a coluna for populada na verdade insira os devidos valores nas colunas corretas por meio de uma ação **Set Value.**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/bZIimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/bZIimage.png)

Devemos colocar um Set Value para cara coluna por meio de regex.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/PyQimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/PyQimage.png)

```
regexp_substr(:GEF, '[^-]+', 1, 3)
```

Devemos atentar que o `:GEF` é a coluna e o `3` é a posição que queremos pegar do retorno, ou seja: <u>1 será Grupoempresa</u>, <u>2 Empresa</u> e <u>3 Filial</u>.

Devemos lembrar de sempre colocar a coluna no ***Items to Submit*** e de colocar a devida coluna no ***Affected Elements**.*

---

**Tela de Exemplo:** [40352:60](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-planejamento/objetos-de-custo-recebido?session=9214413713697)

# Necessidade do Filtro de GEF

Uma questão que ocorre em muitas telas é sobre a GEF. No delphi a maioria das telas possuem o devido filtro porque se não o usuário sempre teria que recarregar o módulo apenas para alterar a GEF, já no APEX não possuímos este problema devido ao **botão de alterar a GEF.**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/H31image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/H31image.png)

Para os que nunca perceberam é este botão que está na **parte superior à direita em todas as telas do sistema Web**.

Com isso muitas telas perdem a necessidade de colocarmos o filtro de GEF nelas, então para isso vamos padronizar como devemos fazer para cada caso.

#### **Telas de Manutenção**

---

Em telas de **Manutenção** onde o filtro de GEF apareceria para que o usuário insira um novo registro e com isso armazene a GEF selecionada, não colocaremos o filtro.

##### **Por que?** 

Porque já possuímos a GEF selecionada no sistema, então vamos colocar para que por padrão se insira o registro na GEF que o usuário está logada.

#### **GEF Seleção Simples**

---

Se o caso da tela ter GEF com **seleção simples** (uma única GEF por vez) devemos fazer um filtro LOV que aparece apenas a **Filial**.

##### **Por que?** 

Porque assim o usuário tem a capacidade de marcar a GEF que deseja com apenas um click e não mais marcando primeiro seu Grupo empresa, depois sua Empresa e depois sua Filial.

Em caso da tela ter a opção de **Filial 0**, vamos manter o filtro da GEF e colocarmos <span style="text-decoration: underline;">Multifiltro</span> para que o usuário tenha a opção de marcar mais de uma Filial como já se faz no legado.

([https://app.clickup.com/36914160/docs/136gzg-1043/136gzg-25403](https://app.clickup.com/36914160/docs/136gzg-1043/136gzg-25403)

# Filtros de Consulta

Nas telas possuímos alguns padrões para filtros em cada tela.

#### **Apenas um Input**

---

Quando tivermos apenas um filtro para a tela (Manutenções e Processos) adicionamos um evento **onChange** e uma ação **Refresh** no Page Item filtro para atualizar a grid quando mudamos o filtro.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/WQqimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/WQqimage.png)

<p class="callout success">**⭐Padrão:** Caso a tela seja de **Consulta, o input deverá estar dentro de um drawer.**</p>

#### **A partir de 2 Inputs**

---

Quando não ocupar muito espaço da tela teremos os **filtros na própria tela** (Manutenções e Processos) e utilizaremos o botão **Filtrar** com o evento **onClick** e uma ação **Refresh** para atualizarmos a grid.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/OSdimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/OSdimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/BtAimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/BtAimage.png)

<p class="callout info">💡 Para colocarmos o botão na mesma linha tiramos o **Start New Row** e colocamos em seu **Column CSS Classes** o seguinte código: `cs-flex-end`</p>

#### **Filtros em Telas de Consulta ou Processo com Muitos Inputs**

---

Faremos um menu lateral para aparecer todos os filtros e assim a visão da grid ser mais limpa. Devemos colocar um botão com um evento **OnClick** e uma ação **Open Region** para abrir a região de filtros, no ***Breadcrumb Bar* no *page-title \[Global Page\]* na position *Copy.***

<p class="callout success">**⭐ Padrão:** **Todas as telas de consulta** devem ter seus filtros em drawer.</p>

<p class="callout info">💡 Pode ocorrer também quando a tela tiver mais de uma grid ou até mesmo mais itens de o botão Filtros ao invés de estar no *<u>page-title</u>* ficar sim no header da grid.</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/30Cimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/30Cimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/gz7image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/gz7image.png)

<p class="callout success">**⭐ Padrão:** O botão deve conter o ícone `fa-filter`.</p>

##### **Resultado Esperado**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/TTVimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/TTVimage.png)

**ou**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/qgzimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/qgzimage.png)

<p class="callout info">💡 Vale lembrar que para obter esse resultado deveremos colocar o botão na Position **COPY**.</p>

Logo após devemos criar uma região **Static Content** com o *Template* **Inline Drawer.**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/5cmimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/5cmimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/gG9image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/gG9image.png)

Seu tamanho deve ser **de acordo com os filtros necessários da tela**.

Os botões de **Filtrar** e de **Limpar filtros** devem estar localizados a esquerda na position <u>Delete</u>, sendo o **Filtrar** <u>Hot</u>, ficando o resultado assim:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/wapimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/wapimage.png)

Sendo o **Filtrar** dando um *Submit Page e* o **Limpar filtros** voltando ao default dos filtros.

##### **Limpar Filtros**

O botão "Limpar Filtros" deve **retornar todos os itens de tela (filtros) para seu valor padrão**, isto é, para os mesmos valores que os mesmos possuíam ao iniciar a tela pela primeira vez.

# Filtros Funcionário

Será apresentado o que deverá ser aplicado para os filtros de funcionários.

# Funcionário

<p class="callout info">Foi criada a package `rh.pkg_apex_filtro_funcionario` com o objetivo de otimizar a performance na obtenção dos resultados dos registros.</p>

#### **Segue Abaixo os Paramêtros:**

**Filtro de Grupo empresa =** `pn_cod_grupoempresa `

**Filtro de empresa deve ser informado ‘1-1’=** `pv_filtro_empresa`

**Filtro de filial deve ser informado ‘1-1-1’=** `pv_filtro_filial`

**Número da aplicação** = `app_id`

**Númedo da Página**= `pn_page_id`

**Id do usuário logado**= `pn_id_logon`

**Data inicial**= `pd_data_inicial `

**Data final**= `pd_data_final`

**Data Referência**= `pd_data_ref_historico`

**Filtro tipo de folha**= `pv_filtro_tipo_folha`

**Filtro objeto de custo**= `pv_filtro_objeto_custo`

**Filtro plano de cargo**= `pv_filtro_plano_cargo`

**Filtro vínculo**= `pv_filtro_vinculo`

**Filtro sindicato**= `pv_filtro_sindicato`

**Filtro escala**= `pv_filtro_escala`

**Filtro turma**= `pv_filtro_turma`

**Filtro setor**= `pv_filtro_setor`

**Filtro departamento**= `pv_filtro_departamento`

**Filtro funções**= `pv_filtro_funcoes`

**Filtro local trabalho**= `pv_filtro_local_trabalho`

**Filtro FPAS**= `pv_filtro_fpas`

**Filtro funcionário responsável**= `pv_filtro_responsavel`

**Filtro agrupamento de pessoa**= `pv_filtro_agrupamento_pessoa`

**Filtro tipo de ponto**= `pv_filtro_tipo_ponto`

**Filtro divisão de objeto de custo**= `pv_filtro_divisao_objetocusto`

- Com o parâmetro `pv_valida_acesso_funcionario`, é possível informar os valores 'S' ou 'N', sendo que o **valor padrão (default) é 'N**'. Esse parâmetro validará as permissões configuradas na tela ‘Acesso Funcionário x Depto x Cargo \[5736\]’.
- A função `rh.fn_acesso_funcionario` será adicionada à SQL para essa validação. Para utilizar essa opção deve ser informado os parâmetros**:** `pn_cod_formulario, pd_data_final, pn_cod_grupoempresa, pn_funcionario_logado e pn_id_logon.`
- Com o parâmetro `pv_dbms_output_put_line` é possível Utilizado para obter a SQL montada informar os seguintes valores: S ou N. O **valor padrão (default) é N.**

<p class="callout info">**👀 Observação:** O valor 'S' deve ser informado apenas quando a funcionalidade for utilizada no PL/SQL.</p>

- Com o parâmetro `pv_listar_apenas_ativos_hj `é possível informar os seguintes valores: True ou False. O valor padrão (default) é False. Será adicionado à cláusula WHERE a condição de filtro: `and periodotrabalhado.data_demissao is null`
- Com o parâmetro `pv_listar_apenas_demitidos `é possível informar os seguintes valores: True ou False. O valor padrão (default) é False. Será adicionado à cláusula WHERE a condição de filtro: `and periodotrabalhado.data_demissao is not null`
- Com o parâmetro `pv_valida_supervisor `é possível informar os seguintes valores: **NAOVALIDA, VALIDA\_SUPERVISORSETOR, VALIDA\_SUPERVISOR\_DEPARTAMENTO.**

**VALIDA\_SUPERVISOR\_PARAMETRIZADO.** O valor padrão default() é **NAOVALIDA .** "O parâmetro 'Supervisor' será validado conforme a configuração na tela 6969(Parâmetros Ponto), no campo 'Identificação entre Líder/Liderado'. Para utilizar essa opção deve ser informado os parâmetros: `pn_id_logon, pd_data_inicial e pd_data_final.`

- Com o parâmetro `pv_status_funcionario` é possível informar os seguintes valores: **ADMISSAO, DEMISSAO, ATIVOSPERIODO, ATIVOSANOMES e TODOS**. O valor padrão (default) é **ATIVOSPERIODO**.

 **ADMISSAO**: Será adicionado à cláusula WHERE a condição de filtro, que deve ser informada pelos parâmetros `pd_data_inicial` e `pd_data_final`, conforme a seguinte expressão: `(periodotrabalhado.data_admissao BETWEEN :data_inicial AND :data_final)`

**DEMISSAO:** Será adicionado à cláusula WHERE a condição de filtro, que deve ser informada pelos parâmetros `pd_data_inicial` e `pd_data_final`, conforme a seguinte expressão: `and (periodotrabalhado.data_demissao between :data_inicial  and :data_final)`"

**ATIVOSPERIODO:** Será adicionada à cláusula WHERE a seguinte condição  de filtro, que deve ser informada pelos parâmetros `pd_data_inicial` e `pd_data_final`, conforme a seguinte expressão:`and rh.intersecao(:data_inicial, :data_final, periodotrabalhado.data_admissao, periodotrabalhado.data_demissao) = 'TRUE'`

**ATIVOSANOMES :** Será adicionada à cláusula WHERE a seguinte condição  de filtro, que deve ser informada o parâmetros `:data_ref_historico` pela entrada de parâmetro `pd_data_ref_historico `, conforme a seguinte expressão:

`and((( :data_ref_historico >= periodotrabalhado.data_admissao) and (periodotrabalhado.data_demissao is null))  or(( :data_ref_historico >= periodotrabalhado.data_admissao) and  (( :data_ref_historico <= periodotrabalhado.data_demissao)  or(to_char(periodotrabalhado.data_demissao,'MM/YYYY' ) = to_char( :data_ref_historico , 'MM/YYYY' )))))`

- Com o parâmetro `pv_historico_empresa` é possível informar os seguintes valores: **HISTORICOABERTO, HISTORICOFECHADO, HISTORICODATADEMISSAO, HISTORICOPERIODO, HISTORICODATAREFERENCIA, HISTORICOANOMES, HISTORICOANOMES\_RESCISAOCOMPLEMENTAR e TODOS**. O valor padrão (default) é **HISTORICODATAREFERENCIA**.

 **HISTORICOABERTO**: Será adicionado à cláusula WHERE a condição de filtro, `and historicoempresa.datafinal is null`

 **HISTORICOFECHADO**: Será adicionado à cláusula WHERE a condição de filtro, `and historicoempresa.datafinal is not null`

**HISTORICOPERIODO**: Será adicionada à cláusula WHERE a seguinte condição  de filtro, que deve ser informada pelos parâmetros `pd_data_inicial` e `pd_data_final`, conforme a seguinte expressão:

**HISTORICODATAREFERENCIA**: Será adicionada à cláusula WHERE a seguinte condição  de filtro, que deve ser informada pelos parâmetros `pd_data_inicial` e `pd_data_final`, conforme a seguinte expressão: `and rh.intersecao((case when :data_ref_historico > to_date(periodotrabalhado.data_demissao) then periodotrabalhado.data_demissao else  :data_ref_historico end ),(case when :data_ref_historico > to_date(periodotrabalhado.data_demissao) then periodotrabalhado.data_demissao else :data_ref_historico end),                                                     historicoempresa.datainicio,historicoempresa.datafinal  ) = 'TRUE'`

**HISTORICOANOMES:** Será adicionada à cláusula WHERE a seguinte condição  de filtro, que deve ser informada o parâmetros `:data_ref_historico` pela entrada de parâmetro `pd_data_ref_historico `, conforme a seguinte expressão:

`and (  (    ( TO_DATE( :data_ref_historico )   >= historicoempresa.DATAINICIO )  AND ( historicoempresa.DATAFINAL    IS NULL)  ) OR  (  ( TO_DATE( :data_ref_historico ) >= historicoempresa.DATAINICIO)   AND ( TO_DATE( :data_ref_historico ) <= historicoempresa.DATAFINAL)  ) OR  (TO_CHAR(historicoempresa.DATAFINAL,'||''''||'MM/YYYY'||''''||') = TO_CHAR(:data_ref_historico,'MM/YYYY') )  )`

**HISTORICOANOMES\_RESCISAOCOMPLEMENTAR:** Será adicionada à cláusula WHERE a seguinte condição  de filtro, que deve ser informada o parâmetros `:data_ref_historico` pela entrada de parâmetro `pd_data_ref_historico `, conforme a seguinte expressão:

`and (( (    ( TO_DATE( :data_ref_historico )   >= historicoempresa.DATAINICIO ) AND ( historicoempresa.DATAFINAL  IS NULL)) OR  (   ( TO_DATE( :data_ref_historico )   >= historicoempresa.DATAINICIO)   AND ( TO_DATE( :data_ref_historico )        <= historicoempresa.DATAFINAL)) OR  (TO_CHAR(historicoempresa.DATAFINAL,'MM/YYYY') = TO_CHAR(:data_ref_historico,'MM/YYYY')  ) )   OR  (   historicoempresa.DATAFINAL   = periodotrabalhado.DATA_DEMISSAO  AND historicoempresa.DATAFINAL    IS NOT NULL      AND periodotrabalhado.DATA_DEMISSAO   IS NOT NULL   )  )`

- Com o parâmetro `pv_objetocusto_join `é possível informar os seguintes valores: **JOIN\_PERIODOTRABALHADO, JOIN\_PERIODOTRABALHADO\_HISTORICODATAREFERENCIA, JOIN\_PERIODOTRABALHADO\_HISTORICOPERIODO, JOIN\_PERIODOTRABALHADO\_HISTORICOABERTO, JOIN\_PERIODOTRABALHADO\_HISTORICODEMISSAO, JOIN\_PERIODOTRABALHADO\_HISTORICOANOMES, JOIN\_PERIODOTRABALHADO\_HISTORICOANOMES\_RESCISAOCOMPLEMENTAR, JOIN\_OBJETOCUSTO\_FN\_OBJETOCUSTO\_CODDESCRICAO\_DATAATUAL, JOIN\_OBJETOCUSTO\_FN\_OBJETOCUSTO\_CODDESCRICAO\_DATADEMISSAO, JOIN\_OBJETOCUSTO\_FN\_OBJETOCUSTO\_CODDESCRICAO\_DATAREFERENCIA, JOIN\_OBJETOCUSTO\_FN\_OBJETOCUSTO\_CODDESCRICAO\_DATAREFERENCIA\_DEMISSAO, UTILIZA\_APENAS\_FILTRO, SEMJOIN**. O valor padrão (default) é **JOIN\_PERIODOTRABALHADO\_HISTORICODATAREFERENCIA**.
- Com o parâmetro `pv_vinculo_join` é possível informar os seguintes valores:**JOIN\_PERIODOTRABALHADO, JOIN\_PERIODOTRABALHADO\_HISTORICODATAREFERENCIA, JOIN\_PERIODOTRABALHADO\_HISTORICOPERIODO, JOIN\_PERIODOTRABALHADO\_HISTORICOABERTO, JOIN\_PERIODOTRABALHADO\_HISTORICODEMISSAO, JOIN\_PERIODOTRABALHADO\_HISTORICOANOMES, JOIN\_PERIODOTRABALHADO\_HISTORICOANOMES\_RESCISAOCOMPLEMENTAR, JOIN\_VINCULO\_FN\_BUSCA\_VINCULO\_DATAATUAL, JOIN\_VINCULO\_FN\_BUSCA\_VINCULO\_DATADEMISSAO, JOIN\_VINCULO\_FN\_BUSCA\_VINCULO\_DATAREFERENCIA, JOIN\_VINCULO\_FN\_BUSCA\_VINCULO\_DATAREFERENCIA\_DEMISSAO, UTILIZA\_APENAS\_FILTRO, SEMJOIN**. O valor padrão (default) é **JOIN\_PERIODOTRABALHADO\_HISTORICODATAREFERENCIA**.
- Com o parâmetro `pv_cargo_join `é possível informar os seguintes valores: **JOIN\_PERIODOTRABALHADO, JOIN\_PERIODOTRABALHADO\_HISTORICODATAREFERENCIA, JOIN\_PERIODOTRABALHADO\_HISTORICOPERIODO, JOIN\_PERIODOTRABALHADO\_HISTORICOABERTO, JOIN\_PERIODOTRABALHADO\_HISTORICODEMISSAO, JOIN\_PERIODOTRABALHADO\_HISTORICOANOMES, JOIN\_PERIODOTRABALHADO\_HISTORICOANOMES\_RESCISAOCOMPLEMENTAR, JOIN\_CARGO\_FN\_BUSCA\_CARGO\_FUNCIONARIO\_DATAATUAL, JOIN\_CARGO\_FN\_BUSCA\_CARGO\_FUNCIONARIO\_DATADEMISSAO, JOIN\_CARGO\_FN\_BUSCA\_CARGO\_FUNCIONARIO\_DATAREFERENCIA, JOIN\_CARGO\_FN\_BUSCA\_CARGO\_FUNCIONARIO\_DATAREFERENCIA\_DEMISSAO, UTILIZA\_APENAS\_FILTRO, SEMJOIN**. O valor padrão (default) é **UTILIZA\_APENAS\_FILTRO**.

#### **Exemplo Inicial**

```
select tmp.*
from table( rh.pkg_apex_filtro_funcionario.fn_filtro_funcionario(  pn_cod_grupoempresa           => &P1460_COD_GRUPOEMPRESA
                                                                 , pv_filtro_empresa             => &P1460_COD_EMPRESA
                                                                 , pv_filtro_filial              => &P1460_COD_FILIAL
                                                                 , pn_app_id                     => &pn_app_id
                                                                 , pn_page_id                    => &pn_page_id
                                                                 , pn_id_logon                   => &pn_id_logon
                                                                 , pv_vinculo_join               => 'SEMJOIN'
                                                                 , pv_objetocusto_join           => 'SEMJOIN'
                                                                 , pv_cargo_join                 => 'SEMJOIN'
                                                                 , pv_historico_empresa          => 'SEMJOIN'
                                                                 , pv_status_funcionario         => 'SEMJOIN'
                                                                 , pv_dbms_output_put_line       => 'S'
                                                                 )) tmp;
```

#### <span class="text-big">**Exemplos de Sucesso tela** </span>[<span class="text-big">**388**</span>](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-ponto-eletronico/espelho-ponto?session=9546391715832)

```
select tmp.cod_funcionario||' - '||nome D
     , tmp.cod_funcionario R
     , tmp.cod_funcionario
     , tmp.nome
     , tmp.periodo
     , tmp.cpf
     , tmp.pis
     , tmp.pai
     , tmp.mae
     , tmp.data_admissao
     , tmp.data_demissao
from table( rh.pkg_apex_filtro_funcionario.fn_filtro_funcionario( pn_cod_grupoempresa           => :P690_COD_GRUPOEMPRESA
                                                                , pv_filtro_empresa             => :P690_COD_EMPRESA
                                                                , pv_filtro_filial              => :P690_COD_FILIAL
                                                                , pn_app_id                     => v('APP_ID')
                                                                , pn_page_id                    => nv('APP_PAGE_ID')
                                                                , pn_id_logon                   => nv('G_ID_LOGON')
                                                                , pd_data_ref_historico         => last_day('01/'||v('G_PROCESSAMENTO_MES')||'/'||V('G_PROCESSAMENTO_ANO'))
                                                                , pd_data_inicial               => :P690_DRH_1
                                                                , pd_data_final                 => :P690_DRH
                                                                , pv_filtro_tipo_folha          => :P690_TF
                                                                , pv_filtro_turma               => :P690_TU
                                                                , pv_filtro_setor               => :P690_SET
                                                                , pv_filtro_departamento        => :P690_DEP
                                                                , pv_filtro_sindicato           => :P690_SIN
                                                                , pv_filtro_escala              => :P690_ES
                                                                , pv_filtro_tipo_ponto          => :P690_TP
                                                                , pv_filtro_objeto_custo        => :P690_OC
                                                                , pv_filtro_responsavel         => :P690_RESP
                                                                , pv_filtro_agrupamento_pessoa  => :P690_AP
                                                                , pv_historico_empresa          => 'HISTORICODATAREFERENCIA'
                                                                , pv_status_funcionario         => 'TODOS'
                                                                , pv_listar_apenas_ativos_hj    => case when :P690_SITUACAO_FUNC = 0 then 'True' end
                                                                , pv_listar_apenas_demitidos    => case when :P690_SITUACAO_FUNC = 1 then 'True' end
                                                                , pv_valida_supervisor          => 'VALIDA_SUPERVISOR_PARAMETRIZADO'
                                                                , pv_vinculo_join               => 'SEMJOIN'
                                                                , pv_objetocusto_join           => 'UTILIZA_APENAS_FILTRO'
                                                                )) tmp
                                                                where tmp.cod_cracha is not null;
```

#### <span class="text-big">**Exemplos de Sucesso tela** </span>[<span class="text-big">**597**</span>](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-ponto-eletronico/eventos-ponto?session=5225374067253)

```
select tmp.cod_funcionario||' - '||nome D
     , tmp.cod_funcionario R
     , tmp.cod_funcionario
     , tmp.nome
     , tmp.periodo
     , tmp.cpf
     , tmp.pis
     , tmp.pai
     , tmp.mae
     , tmp.data_admissao
     , tmp.data_demissao
from table( rh.pkg_apex_filtro_funcionario.fn_filtro_funcionario(
                                pn_cod_grupoempresa        => :P670_COD_GRUPOEMPRESA
                              , pv_filtro_empresa             => :P670_COD_EMPRESA
                              , pv_filtro_filial              => :P670_COD_FILIAL
                              , pn_app_id                  => v('APP_ID')
                              , pn_page_id                 => nv('APP_PAGE_ID')
                              , pn_id_logon                => nv('G_ID_LOGON')
                              , pd_data_inicial            => :P670_DT_INI
                              , pd_data_final              => :P670_DT_FIM
                              , pv_filtro_tipo_folha              => :P670_TP_FOLHA
                              , pv_filtro_cargo                   => :P670_CC
                              , pv_filtro_nivel_cargo             => :P670_CN
                              , pn_nivel_npsa              => :P670_NIVEL
                              , pv_filtro_npsa                    => :P670_NPSA
                              , pv_filtro_setor                   => :P670_SETOR
                              , pv_filtro_departamento            => :P670_DEPART
                              , pv_filtro_sindicato               => :P670_SIND
                              , pv_filtro_divisao_objetocusto     => :P670_DIVISAO_OBJ_CUSTO
                              , pv_filtro_escala                  => :P670_ESCALA
                              , pv_filtro_objeto_custo            => :P670_OBJ_CUSTO
                              , pv_filtro_agrupamento_pessoa      => :P670_AGRUP_PESSOA
                              , pv_historico_empresa       => case when :P670_TIP = 0 and :P670_ATIVO = 'False' then 'HISTORICOPERIODO'
                                                                   when :P670_TIP = 0 and :P670_ATIVO = 'True'  then 'HISTORICOABERTO'
                                                                   when :P670_TIP = 1 then 'HISTORICODATADEMISSAO'
                                                                   when :P670_TIP = 3 then 'TODOS'
                                                              end
                              , pv_status_funcionario       => case when :P670_TIP = 0 then'ATIVOSPERIODO'
                                                                   when :P670_TIP = 1 then 'DEMISSAO'
                                                                   when :P670_TIP = 2 then 'TODOS'
                                                              end
                              , pv_listar_apenas_ativos_hj => case when :P670_TIP = 0 then :P670_ATIVO --somente passar o Valor do cb se selecionar ativos no radiogroup de funcionarios
                                                                   else 'False'
                                                              end
                              , pv_vinculo_join            => 'JOIN_VINCULO_FN_BUSCA_VINCULO_DATAREFERENCIA_DEMISSAO'
                              , pv_objetocusto_join        => 'JOIN_OBJETOCUSTO_FN_OBJETOCUSTO_CODDESCRICAO_DATAREFERENCIA_DEMISSAO'
                              , pv_cargo_join              => 'UTILIZA_APENAS_FILTRO'
                              )) tmp;
```

# Menu de Navegação dos Funcionários

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/CjHimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/CjHimage.png)

A função que cria o Menu de navegação deve ser chamada na SQL de um Contextual info com as informações do funcionário atual e sua coluna deve ser do tipo **Plain Text** com o **Escape special characters - Desligado**

<table border="1" id="bkmrk--1" style="border-collapse: collapse; width: 100%;"><colgroup><col style="width: 50%;"></col><col style="width: 50%;"></col></colgroup><tbody><tr><td>[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/3R661Timage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/3R661Timage.png)</td><td>[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/YBqimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/YBqimage.png)</td></tr></tbody></table>

####  **Função**

---

```
rh.pkg_ornenacao_func.fn_ordenacao_func(pn_cod_funcionario in number
                         , pn_periodo         in number

                         , pv_componente_func in varchar2

                         , pn_ordenacao       in number
                         , pn_tipo_modal      in number default 0
                         , pn_page_id         in number default v('APP_PAGE_ID')
                         , pn_application_id  in number default v('APP_ID')
                        )
```

####  **Explicação dos Parâmetros**

---

- **pn\_cod\_funcionario:** Valor do código do funcionário (Exemplo: 3)
- **pn\_periodo**: Periodo do funcionário (Exemplo: 1)
- **pv\_componente\_func:** Nome do componente dos funcionários com retorno "Código-Periodo" que terá a SQL da consulta e será modificado pela navegação (Exemplo: ‘P5\_FILTRO\_FUNC’)
- **pn\_ordenacao:** Valor da ordenação da navegação (Exemplo: 0) 
    - 0 - Código
    - 1 - Nome
    - 2 - Data de Admissão
- **pn\_tipo\_modal (OPCIONAL):** Tipo de modal de exibição na lupa central (Exemplo: 0) 
    - 0 - Seleção única pela GRID
    - 1 - Seleção única por CARDS
- **pn\_page\_id (OPCIONAL):** o ID da página que possui o componente dos funcionários (Exemplo: 220)
- **pn\_application\_id (OPCIONAL)**: o ID da aplicação que possui o componente dos funcionários (Exemplo: 40104)

#### **Tela Exemplo com o Resultado Esperado (40107:1180)**

---

**[![demo_menu_func.gif](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/demo-menu-func.gif)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/demo-menu-func.gif)**

# Forms

Documentação Técnica sobre campos de formulário/itens de página.

# Itens de Página

<p class="callout success">**🔗[Saiba as boas práticas de usabilidade e experiência do usuário para itens de página ](https://wiki.cscompusoftware.com.br/books/erp-guideline-de-uiux/page/campos-de-formulario "Boas Práticas para Campos de Formulários")**</p>

O template visual padrão para itens de tela é o **Optional - Above** com Size = **Large** no Template Options.

<p class="callout info">**💡 Recomendação:** habilitar "Stretch Form Item" sempre que possível.</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/r3Ximage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/r3Ximage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/BF1image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/BF1image.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/51timage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/51timage.png)

#### **Desabilitar Itens na Tela**

---

Para desabilitar a edição de um item na tela, há duas formas:

- Quando for uma condição estática (que só muda no carregar na página) é recomendado utilizar a propriedade **Read Only do APEX,**
- Quando for dinâmica utilizar a classe CSS `apex_disabled`.
- Item com borda pontilhada: `cs-custom-dashed-item`.

# LOVs

Vamos **concentrar TODAS as LOVs genéricas no APP 40000 Scaffold**, e posteriormente fazer a Subscription dessa LOV no APP que desejamos utilizar essa lista.

#### **Exemplo**

App 40000 &gt; Shared Components &gt; List of Values

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/pc3image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/pc3image.png)

App 40101 &gt; Shared Components &gt; List of Values &gt; Subscription

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/dNsimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/dNsimage.png)

Exceções **apenas àquelas LOVs específicas** ao módulo.

#### **LOV por Módulo** 

---

Crie um novo List of Values em **Shared Components &gt; Lists of Values**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/MBkimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/MBkimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/KzVimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/KzVimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/34cimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/34cimage.png)

Em Source Type, selecione **SQL Query** e na SQL passe as seguintes colunas:

- Uma coluna chamada "d", referente ao **Display Value**. Deve ser o código da tabela que será exibido no Text Field referente ao código;
- Uma coluna chamada "v", referente ao **Return Value**. Deve ser o código da tabela que será gravado na tabela;
- Caso seja necessário exibir colunas além do Display Value para o usuário, selecione as colunas na SQL com um nome identificável.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/YvFimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/YvFimage.png)

Logo em seguida, selecione o Return Value no seletor **Return Column**, e o Display Value no seletor **Display Column**:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/zDtimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/zDtimage.png)

Depois de criar o List of Values, entre nele e clique no botão **Select Columns**:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/tcKimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/tcKimage.png)

Coloque os campos adicionais no lado direito (quando aplicável) e clique em **Update**:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/4rqimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/4rqimage.png)

Ajuste os **Headings** (labels) das colunas e aplique as alterações:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/S9Vimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/S9Vimage.png)

#### **Configuração dos Campos do Form/Grid para Passagem de Múltiplos Campos de Uma Vez**

---

Na página, certifique-se que o seu Form ou Interactive Grid está com a **Source &gt; Type** definida como **SQL Query**.

<p class="callout info">**✍ Nota:** Em páginas criadas pelo Wizard do APEX, alterar o Type para SQL Query gera uma Query simples com todos os campos selecionados.</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/y5Bimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/y5Bimage.png)

No SELECT da SQL adicione **colunas de subquery** para buscar as descrições dos campos de FK que serão utilizadas para mapear aos campos de descrição. Ao salvar o APEX gerará automaticamente itens Text Field ou Textarea que correspondem a esses campos de descrição da query.

<p class="callout warning">**Importante:** Ao buscar descrições de chaves estrangeiras **sempre utilize colunas de subquery para evitar gravação indevida** de dados em outras tabelas.</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/R4Fimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/R4Fimage.png)

No **List of Values** da coluna do código colocar o list of values criado:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/L0Uimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/L0Uimage.png)

E em **Settings &gt; Additional Outputs**, coloque o seguinte texto:

***\[TERCEIRO CAMPO DO LOV\]:\[IDENTIFICADOR DO ITEM DESCRIÇÃO\]***

Onde **\[TERCEIRO CAMPO DO LOV\]** corresponde ao campo do LOV criado que você teve que adicionar manualmente na lista de valores, e **\[IDENTIFICADOR DO ITEM DESCRIÇÃO\]** é o **nome do item** ou **nome da coluna** que corresponde ao campo de descrição no form/grid.

##### **Exemplo**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/o6qimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/o6qimage.png)

# Gerar Release APEX

#### **Organograma**

---

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/kLEimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/kLEimage.png)

#### **Boas Práticas**

---

Solicitar à equipe a liberação das telas da aplicação que será enviada. Eles podem ver pela página do **DevTools**.

Isso gerará uma versão da página no nosso sistema de **AUTOSAVE/CHECKIN.**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/pZdimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/pZdimage.png)

##### **Verificação de Páginas Bloqueadas**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/insimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/insimage.png)

##### **Associação da Aplicação ao Time**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Uwzimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Uwzimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/sUGimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/sUGimage.png)

# Global State

Para o controle de estado de informações globais nas aplicações utilizamos **Applications Items** criados com escopo global.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Hgximage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Hgximage.png)

APP &gt; Shared Components &gt; Applications Items

# Help/Artigos On-line

Nossa referência/consumo de Help dentro do CS 4.0 é **feito toda por API**, logo, basta adicionar a **"Aplicação:Página" nas TAGs** da página no [Wiki.js](https://doc.cscompusoftware.com.br/login "Documentação WIKI")

Uma vez página referenciada na TAG (Palavra Chave) no nosso portal de artigos:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/n23image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/n23image.png)

Automaticamente a documentação já aparecerá na pesquisa de **HELP em TODOS** os nossos clientes, sem depender de liberação.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/hYqimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/hYqimage.png)

<p class="callout info">💡 Vale lembrar que a página precisa estar como **pública e também publicada**, seja manualmente ou pós data de agendamento da publicação.</p>

# Importações EXCEL (.xlsx)

# Importações de Planilhas

Em alguns casos, é necessário importar planilhas para o sistema, a fim de facilitar a vida do usuário.

Para importar, precisamos criar os itens de tela para alimentação.

- Primeiro, vamos criar um item do tipo navegador de arquivos **"File Browser"**.
- Coloque o **Label** para identificar o campo, **"Selecione um arquivo"**.
- Defina o **File Types** como ".xlsx", que é a <span class="ql-bg-red">ÚNICA</span> extensão aceita.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/WBiimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/WBiimage.png)

Uma vez item criado, vamos criar uma ***Dynamic Action*** com o evento **onChange** contendo 2 ações ***True***, sendo elas:

A primeira com um ***Execute Server-side Code*** contendo a chamada do seguinte procedimento:

```
csweb.pkg_apex_importacao_xlsx.pr_sanitizar_tmp;
```

A segunda com **Submit Page**.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/DSIimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/DSIimage.png)

Crie um campo de seleção para exibir todas as abas (<span class="ql-bg-yellow">PASTAS</span>) da planilha selecionada.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/1Eximage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/1Eximage.png)

No **List of Values**, adicione a seguinte SQL:

```
select tmp.nome_planilha D
     , tmp.nome_planilha R
from   apex_application_temp_files
     , table(csweb.pkg_apex_importacao_xlsx.fn_abas_xlsx(apex_application_temp_files.blob_content)) tmp
order  by nome_planilha
```

Em uma breve explicação da **`apex_application_temp_files`:** Quando você permite que os usuários carreguem arquivos, como imagens, documentos ou outros tipos de mídia, para dentro de um aplicativo APEX, esses arquivos geralmente precisam ser armazenados temporariamente em algum lugar enquanto o aplicativo os processa ou os associa a algum tipo de registro ou funcionalidade.

A tabela `<strong>apex_application_temp_files</strong>` é usada para esse armazenamento temporário de arquivos. Ela tem as seguintes colunas principais:

```
ID: Um identificador único para cada arquivo temporário carregado.
SESSION_ID: O ID de sessão do usuário que carregou o arquivo.
PAGE_ID: O ID da página APEX na qual o arquivo foi carregado.
APPLICATION_ID: O ID da aplicação APEX.
FILE_NAME: O nome original do arquivo.
MIME_TYPE: O tipo MIME do arquivo (por exemplo, image/jpeg, application/pdf, etc.).
FILE_CONTENT: O conteúdo do arquivo em si, armazenado em formato binário.
EXPIRATION_DATE: A data de expiração do arquivo temporário, após a qual ele será automaticamente removido.
```

Essa tabela é uma parte importante da funcionalidade de upload de arquivos no APEX, pois ajuda a manter os arquivos temporários organizados e controlados.

A função `<strong>table(geral.fn_leitor_xlsx())</strong>` lê o conteúdo da planilha armazenada na tabela temporária **apex\_application\_temp\_files**. Você pode ler tanto o conteúdo que está em abas separadamente quanto o conteúdo das próprias abas.

Por exemplo:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/Y5qimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/Y5qimage.png)

Ao selecionar a **planilha1**, serão importados 11 registros. Já ao selecionar a **planilha2**, serão importados apenas 3 registros.

Vamos adicionar uma condição para exibir a pasta que pode ser selecionada quando um arquivo for carregado.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/pAXimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/pAXimage.png)

Após isso, crie um botão na seção **Rodapé do Diálogo (Dialog Footer)** para importar esses dados. O botão só deve aparecer quando um arquivo for carregado.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/Ivyimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/Ivyimage.png)

A tela ficará semelhante à atual.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/id0image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/id0image.png)

Depois disso, vamos adicionar um evento no ***After Submit*** para recuperar os valores da planilha importada.

```
csweb.pkg_apex_importacao_xlsx.pr_importacao_xlsx( pb_blob_content => csweb.pkg_apex_importacao_xlsx.fn_blob_content(pv_name => :P86_NOMEARQUIVO)
                                                     , pv_pasta        => P86_PASTA
                                                     );
```

A procedure **pr\_importacao\_xlsx** aceita parâmetros dinâmicos, que podem ser ajustados de acordo com a necessidade.

```
pn_celulas_info : Se você informar o valor 0, todas as células da planilha serão consideradas. Se você informar o valor 1, será obrigatório informar as células no parâmetro pv_celulas. 

pv_celulas : Informe uma (ou mais separada por ":" 2 pontos) célula específica para não importar todas as células.

pv_nome_collection : Por padrão, o nome será 'CSWEB.IMPORTACAO_XLSX'. Se você deseja trabalhar com um nome específico, basta informar o nome desejado.
```

**Exemplo de utilização da procedure com os itens extras:**

```
csweb.pkg_apex_importacao_xlsx.pr_importacao_xlsx( pb_blob_content    => csweb.pkg_apex_importacao_xlsx.fn_blob_content(pv_name => :P86_NOMEARQUIVO)
                                                 , pv_pasta           => :P86_PASTA
                                                 , pv_nome_collection => 'GRID_TESTE'
                                                 , pn_celulas_info    => 1
                                                 , pv_celulas         => 'A:B:C');
```

Os dados são todos baseados por coleções, para conseguir ler os dados somente fazer uma seleção na coleção:

```
select c001 date   
     , c002 valor
     , c003 sem_valor
from   csweb.vw_apex_collections 
where  collection_name = 'GRID_TESTE' 
```

<p class="callout info">💡 Para mais informações sobre **como** **funciona uma collection. Acesse:** [Collections - Dev Guideline](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/chapter/collections "Collections")</p>

---

**Tela exemplo ➝** 40255:61

# Padronização Layout Arquivo

Em telas onde existirão **importações de arquivo do tipo Excel (.*xlsx*)**, o usuário terá a possibilidade de realizar o download de um layout exemplo para fazer a importação, o que facilitará e muito o cotidiano dele.

A seguir terão os passos de como fazer e, o mais importante: A padronização do layout *xlsx* que **DEVE ser seguida.**

#### **Passo a Passo**

---

**1 ➝** O arquivo *xlsx* será chamado de `layout_exemplo`

**2 ➝** O arquivo Excel de Layout Exemplo possuirá duas abas, sendo a primeira delas o layout que o usuário quer. Já a segunda aba, obrigatoriamente terá o nome de "`regras_planilha`".

No exemplo abaixo a primeira aba chama "Plan1" e a segunda possui o nome padronizado "`regras_planilha`".

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/YGJimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/YGJimage.png)

**3 ➝** Na aba `regras_planilha` será onde ficarão as instruções e explicações para o usuário sobre o layout e como montá-lo adequadamente.

Seguindo o ponto do guia [Importações de Planilhas](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/importacoes-de-planilhas "Importações de Planilhas - Dev Guideline"), dentro da **SELECT** da planilha, haverá uma cláusula **WHERE**, para que na seleção da planilha desejada para a importação não seja mostrado para o usuário a opção do `regras_planilha`.

```
select distinct tmp.nome_planilha D
              , tmp.nome_planilha R
from   apex_application_temp_files
     , table(geral.fn_leitor_xlsx(apex_application_temp_files.blob_content)) tmp
where  tmp.nome_planilha != 'regras_planilha'
order  by nome_planilha
```

#### **Criando o Download de Arquivo**

---

**1 ➝** Dentro da aplicação que você estiver trabalhando, vá em **Shared Components** ➝ **Static Application Files**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/QPFimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/QPFimage.png)

**2 ➝** Lá dentro, você clicará em "**Create File**" dando um nome de Diretório como por exemplo page-300 *(page-<u>o número da sua página APEX</u>).*

Depois disso é só selecionar o arquivo Excel do layout exemplo que foi criado para o usuário realizar o download e, por fim, selecionar o botão "**Create**".

**2.1**➝ Após criado, o APEX informará para você as seguintes informações:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/7b8image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/7b8image.png)

**2.2 ➝** Copie o **Reference**, você precisará dele a seguir;

**2.3 ➝** Agora na sua página do APEX, crie um botão que irá realizar o download. Nele você criará uma ação dinâmica do tipo **onClick**, com a **True Action** de **Execute JavaScript Code**.

Dentro do code block, insira o seguinte código, ajustando-o para a sua tela:

```
let link = document.createElement('a');
link.href = '#APP_FILES#page-740/layout_exemplo.xlsx';
link.download = 'layout_exemplo.xlsx';
link.click();
```

Na segunda linha de código, substitua o que está no `<em>'link.href'</em>` pelo que você copiou anteriormente do passo 2.2;

Pronto, agora é só realizar o download <span class="cu-emoticon cu-emoticon_static" data-emoticon="{"code":"1f642","name":"Slightly Smiling Face"}">🙂</span>

# Informações do Usuário para LOG

Em algumas tabelas, encontramos **colunas que armazenam informações relacionadas a máquina, programa e/ou usuário**.

Essas informações são normalmente preenchidas por meio de acionadores (triggers) que utilizam dados da tabela v$session. No entanto, ao trabalhar com o Oracle APEX, percebemos que **não é possível obter as mesmas informações de usuário dessa maneira**, uma vez que a tabela v$session fornece apenas dados relacionados ao Tomcat.

Para superar essa limitação, pode utilizar a função `fn_informacao_usuario`, que está disponível em `csweb.pkg_apex_utils`.

Essa função desempenha um **papel crucial ao retornar informações específicas dependendo do contexto da sessão**.   
Quando a sessão está vinculada ao Delphi ou ao Banco de Dados, a função fornece detalhes como o módulo, o usuário e a máquina. Por outro lado, quando a sessão é relacionada ao Oracle APEX, a função retorna informações como a aplicação, a página e o endereço IP.

```
csweb.pkg_apex_utils.fn_informacao_usuario
```

# Interactive Grid

# Botões na Actions Bar da Grid pelo Plugin FOS

Existem algumas opções de locais para adicionarmos um botão de ação que é atrelado a uma grid, ou seja, quando o botão afeta diretamente a grid e os registros que estão contidos nela.

De acordo com o nosso padrão de desenvolvimento, toda grid precisa estar dentro de outra região e seguir uma nomenclatura padrão (ex: `ig-autorizacao`), onde a região "pai" ou com hierarquia maior possui o título escrito corretamente, sendo esta a que irá aparecer na página, para o exemplo anterior, a hierarquia de regiões seria: (Autorizações&gt; ig-autorizacao).

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/OEmimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/OEmimage.png)

<p class="callout success">⭐ Saiba as boas práticas, layout e padrões de botões e botões em grid. **Acesse:** [Botões](https://wiki.cscompusoftware.com.br/books/erp-guideline-de-uiux/page/botoes "Botões") e [Grids](https://wiki.cscompusoftware.com.br/books/erp-guideline-de-uiux/page/grid "Grids")</p>

#### **Grid com Header**

---

Quando a região "pai" for exibida, mostrando seu header (faixa azul com o título), normalmente colocaremos o botão de ação na **position copy desta região**, desta forma:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/qtdimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/qtdimage.png)

#### **Grid sem Header**

---

No entanto, existem algumas situações em que **não é válido exibir o header da região apenas para colocarmos um botão de ação** na grid, para isso, utilizaremos uma *Dynamic Action* do Plugin FOS.

Esta *Dynamic Action* incluirá um botão dentro da grid, fazendo com que o header da região pai não seja mais necessário.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/0Qjimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/0Qjimage.png)

Como citado anteriormente, para isso utilizaremos o plugin FOS - Interactive Grid - Add Button no Page Load da página que queremos adicionar o botão na grid.

<p class="callout info">**💡** Importante ressaltar **cada botão será criado por uma única *Dynamic Action***, caso seja necessário adicionar **mais de um botão, será necessário criar uma nova True Action da *Dynamic Action* onPageLoad** já criada anteriormente.</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/CyAimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/CyAimage.png)

Existem algumas configurações que podemos alterar, como a label e o ícone do botão, bem como qual evento será executado quando o botão for clicado.

O campo **"Event Name"** é utilizado para **referenciar um nome de um evento custom** que iremos configurar posteriormente. Por padrão, **escolha um nome que evidencie** da melhor forma q**ual será o processo que o botão irá executar**, no exemplo da imagem, ao clicar no botão, será cancelada uma aprovação.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/V7Nimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/V7Nimage.png)

Depois de configurado o botão pela *Dynamic Action* do FOS, agora é necessário **configurar uma *Dynamic Action* do tipo Custom** na sua grid, que irá realizar todo o processo necessário. Normalmente temos um padrão para nomear *Dynamic Actions*, como por exemplo "onChange.......", porém neste caso específico, **o nome da dynamic action criada será o mesmo do "Event Name"** lá do Plugin FOS - Interactive Grid - Add Button. Além do nome, é necessário **alterar o tipo do evento para Custom**, e no campo Custom Event passar o mesmo nome do "Event Name" novamente.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/gluimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/gluimage.png)

Dessa forma, ao clicar no botão, o evento `cancelar-aprovacao` será executado, agora basta programar as ações (True e False Actions) para que a *Dynamic Action* executa o processo necessário.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/T8vimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/T8vimage.png)

# Checkbox Header na Grid

Para adicionar a Checkbox ela pode ser colocada tanto dentro da `ig-grid`**,** como também no **Header da Página**.

<p class="callout success">⭐ Saiba as boas práticas, layout e posição do checkbox em grids. **Acesse:** [Grids](https://wiki.cscompusoftware.com.br/books/erp-guideline-de-uiux/page/grid "Grids").</p>

#### **Header da Página**

---

No Checkbox coloque na seção **"Advanced"** uma div no **"Pre Text"** e feche no **"Post Text".**

##### **Pre Text**

```
<div id="chk-todas-filiais" style="padding-inline-end: 5px">
```

##### **Post Text**

```
</div>
```

Depois crie uma ação dinâmica no page load e adicione a seguinte função JS

<p class="callout info">**👀 Observação** : Note que o id criado na &lt;div&gt; será o mesmo dentro da função.</p>

```
addElementToPageTitle('chk-todas-filiais')
```

#### **Checkbox no Header da Grid**

---

Na sua checkbox em "**Advanced**" abra a DIV no "**Pre Text**" e feche no "**Post Text**".

##### **Pre Text**

```
<div id="checkboxGEF" aria-hidden="true" style="margin-top: 8px; margin-right: 4px;">
```

#####  **Post Text**

```
</div>
```

Criar uma ação dinâmica do tipo "**Page Load**" da pagina e crie uma ação "**Execute JavaScript Code**" com a função:

```plaintext
addElementToGridHeader('ig-hist', 'checkboxGEF');
```

# Coloração Dinâmica de Células

#### Conceito

A funcionalidade se baseia em três pilares:

1. Coluna de Estilo na SQL: A consulta SQL da Interactive Grid deve incluir uma coluna adicional que, para cada linha, conterá o nome da classe CSS a ser aplicada.
2. Função JavaScript de Inicialização: Uma chamada à função setCustomConfig com passagem de parâmetros é adicionada nas configurações da IG (Advanced &gt; Initialization JavaScript Function).
3. Configuração de Parâmetros: A função é configurada para reconhecer a coluna de estilo, aplicar a classe CSS em todas as colunas desejadas e ignorar colunas especificadas.

#### Como Utilizar

Siga os passos abaixo para implementar a coloração dinâmica em sua Interactive Grid.

##### Passo 1: Modificar a Consulta SQL

Adicione uma nova coluna à sua consulta. Esta coluna servirá como fonte das classes CSS.

Exemplo:

Suponha que você queira pintar linhas com base no status de uma fatura.

```sql
select faturas.id_fatura
     , faturas.numero_documento
     , faturas.data_vencimento
     , faturas.valor
     , faturas.status
     , case when faturas.status = 'PAGO' then 'u-color-15-bg' 
            when faturas.status = 'VENCIDO' then 'u-color-5-bg'
            when faturas.status = 'A VENCER' then 'u-color-4-bg'
            else null
       end as css_class_column
from   owner.faturas faturas
```

<p class="callout info">**Observação**  
 Classes CSS: Para manter a consistência visual prefira usar as classes de cores definidas como padrões, em casos onde não exista ainda uma classe para a cor desejada crie sua classe e utilize as cores definidas como padrão na Paleta de Cores.  
**Paleta de Cores:**  
 <span style="background-color: rgb(254, 233, 171);"> <span style="color: rgb(0, 0, 0);">Amarelo</span> </span>: #FEE9AB  
 <span style="background-color: rgb(254, 222, 232);"> <span style="color: rgb(0, 0, 0);">Rosa</span> </span>: #FEDEE8  
 <span style="background-color: rgb(200, 209, 252);"><span style="color: rgb(0, 0, 0);"> Roxo</span> </span>: #C8D1FC  
 <span style="color: rgb(0, 0, 0); background-color: rgb(251, 210, 184);"> Laranja </span>: #FBD2B8  
 <span style="color: rgb(0, 0, 0); background-color: rgb(203, 239, 226);"> Turquesa </span>: #CBEFE2  
 <span style="color: rgb(0, 0, 0); background-color: rgb(208, 241, 204);"> Verde </span>: #D0F1CC  
 <span style="color: rgb(0, 0, 0); background-color: rgb(255, 214, 210);"> Vermelho </span>: #FFD6D2</p>

##### Passo 2: Configurar o JavaScript de Inicialização

1. Selecione a região da sua Interactive Grid no Page Designer.
2. No painel de propriedades à direita, vá para Advanced &gt; Initialization JavaScript Function.
3. Insira o código a seguir, ajustando os parâmetros conforme sua necessidade.

Caso queira informar células ignoradas:

```JS
(config) => setCustomConfig( config, {

  enableCssColumn: true,

  cssColumnName: "CSS_CLASS_COLUMN",

  ignoredColumns: ["VALOR", "DATA_VENCIMENTO"]

})
```

Ou informar somente as células coloridas:

```JS
(config) => setCustomConfig( config, {

  enableCssColumn: true,

  cssColumnName: "CSS_CLASS_COLUMN",

  selectedColumns: ["VALOR", "DATA_VENCIMENTO"] 

})
```

<p class="callout info">**Observação**  
 **ignoredColumns e SelectedColumns: São excludentes, então se utilizar o selectedColumns não utilize na mesma grid o ignoredColumns.**</p>

##### Entendendo os Parâmetros:

- **cssColumnName**: "CSS\_CLASS\_COLUMN"
    
    
    - Obrigatório. O nome da coluna (alias) que você definiu na sua consulta SQL. Atenção: O valor deve ser em maiúsculas e corresponder exatamente ao alias que o APEX reconhece para a coluna.
- i**gnoredColumns ou selectedColumns**: \[“COLUNA\_TAL”\] 
    - Opcional. Uma lista (array) de nomes de colunas que devem ou não receber a coloração, de acordo com o tipo de atributo alimentado (selectedColumns ou ignoredColumns).

##### Passo 3: Ocultar a Coluna de Estilo

Para que a coluna CSS\_CLASS\_COLUMN não apareça para o usuário final:

1. Vá para a seção Columns dentro da sua região de Interactive Grid.
2. Selecione a coluna de estilo (ex: CSS\_CLASS\_COLUMN).
3. No painel de propriedades da coluna, altere o Type para Hidden.

# Colunas de Destaque (Badges)

Primeiramente será explicado como utilizar os `"col-badges"` em Interactive Reports e Classic Reports.

No final da página será explicado como utilizar em Interactive Grids.

Para casos em que precisamos destacar um registro de Report criamos uma classe para **usarmos como alternativa ao highlight de linha**. Essa classe deve ser utilizada em uma determinada coluna para destaque.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/vhfimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/vhfimage.png)

A classe em questão é a `cs-col-badge.` Essa classe CS monta o badge para destaque, e em conjunto com ela é necessário determinar qual será o tema do badge.

Esse tema pode ser determinado de duas formas: **Tipo Simples ou Tipo Dinâmico.**

#### **Tipo Simples**

---

Badges de tipo simples podem ter variantes de 4 tipos.

<table border="1" class="align-center" id="bkmrk-tipo-classe-css-suce" style="border-collapse: collapse; width: 42.7381%;"><colgroup><col style="width: 28.9256%;"></col><col style="width: 71.0744%;"></col></colgroup><thead><tr><td>**Tipo**</td><td>**Classe CSS**</td></tr></thead><tbody><tr><td>Sucess</td><td>`cs-col-badge--success`</td></tr><tr><td data-row="row-dmbu2a" data-table-cell-color="blue">Info

</td><td data-row="row-dmbu2a">`cs-col-badge--info`

</td></tr><tr><td data-row="row-wjfr2j" data-table-cell-color="yellow">Warning

</td><td data-row="row-wjfr2j">`cs-col-badge--warning`

</td></tr><tr><td data-row="row-izy1ww" data-table-cell-color="red">Danger

</td><td data-row="row-izy1ww">`cs-col-badge--danger`

</td></tr></tbody></table>

Para determinar o tipo, de acordo com o registro da Query, precisamos trazer essa informação em uma coluna da SQL.

**Exemplo:**

```pl/sql
select status_desc
     , case status
            when 'S' then 'success'
            when 'E' then 'danger'
       end status_type
from   exemplos.tabela
```

 Essa coluna pode ser oculta pelo Type Hidden.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/33Himage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/33Himage.png)

Com essa coluna que trás o tipo criada, tudo que precisa ser feito é determinar o type da coluna onde queremos exibir a badge para HTML Expression, e em seguida informar o código HTML da coluna, que consiste em um simples span com as classes.

Exemplo com a coluna `STATUS_DESC`.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/xR1image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/xR1image.png)

```html
<span class='cs-col-badge cs-col-badge--#STATUS_TYPE#'>
  #STATUS_DESC#
</span>
```

##### **Resultado**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/F6eimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/F6eimage.png)

#### **Tipo Dinâmico**

---

Badges do tipo dinâmico são usados quando as cores do tipo simples não são suficientes, ou mesmo quando a cor precisa ser determinada pelo registro da SQL.

Para implementar esse tipo, a SQL precisa retornar as duas cores separadamente.

**Exemplo:**

```pl/sql
select status_desc
     , cor_fonte
     , cor_fundo
from   exemplos.tabela
```

 O HTML Template da coluna deve determinar o style.

```html
<span class='cs-col-badge' style='background-color: #COR_FUNDO#; color: #COR_FONTE#;'>
  #STATUS_DESC#
</span>
```

##### **Resultado**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/K8Kimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/K8Kimage.png)

<p class="callout info">**👀 Obs:** Essa classe também pode ser implementada em Interactive/Classic Report. O funcionamento em si é basicamente o mesmo.</p>

##### **Para Utilizar em Interactive Grids**

Será feito de uma forma um pouco diferente dos Reports, pois se fizer igual, não será possível filtrar informações pela coluna na grid que tiver col-badge. Da forma que será apresentada a seguir, não resultará em nenhum problema e você terá a coluna destacada da mesma forma. Acompanhe os próximos passos:

*Serão apresentadas duas formas diferentes de utilizar a `col-badge` na Interactive Grid, sendo elas a opção 1 e a opção 2;*

##### Opção 1 - Usando value e type

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/UIfimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/UIfimage.png)

**1.1 ➝** Primeiro pegue a coluna que será apresentada a informação em sua grid (no caso exemplo é a coluna Origem) e crie na SQL uma coluna TYPE dela. Essa coluna do tipo TYPE poderá ser do tipo *HIDDEN*. Código exemplo abaixo:

```pl/sql
case when origem = 1 then 'danger'
     when origem = 2 then 'success'
     when origem = 3 then 'warning'
end origem_type
```

**Obs: <span class="ql-bg-red">danger = vermelho</span> | <span class="ql-bg-green">success = verde</span> | <span class="ql-bg-yellow">warning = amarelo</span>;**

Também poderão ser colocadas cores hexadecimais, mas dependendo do contexto, dê preferência para as cores padrão.

**1.2 ➝** No Page Designer, selecione a sua coluna que aparecerá na grid e vá na opção Javascript Initialization Code dela. O seguinte código será inserido nessa parte:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/yxyimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/yxyimage.png)

```javascript
(config) => setBadgeColumnExpression(config, {
  value: 'ORIGEM_DESC',
  type: 'ORIGEM_TYPE',
})
```

- **value**: será a sua coluna que aparecerá na grid;
- **type**: é a coluna TYPE que você criou anteriormente;

##### Opção 2 - Usando value, backgroundColor e fontColor

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/zJPimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/zJPimage.png)

**2.1 ➝** A criação da coluna type será igual, respeitando as condicionais de sua SQL;

**2.2 ➝** Os mesmos passos serão seguidos até a parte do Javascript Initialization Code;

**2.3 ➝** No Javascript Initialization Code da coluna, será inserido um código levemente diferente:

<p class="callout info">**👀 Obs:** Para utilizar a opção com value, backgroundColor e fontColor, utilize **apenas cores hexadecimais**.</p>

```javascript
(config) => setBadgeColumnExpression(config, {
  value: 'TIPO_AFAST',
  backgroundColor: 'TIPO_AFAST_BG_COLOR',
  fontColor: '#000000',
})
```

- **value**: será a sua coluna que aparecerá na grid;
- **backgroundColor**: a sua coluna type que foi criada (no caso exemplo ela se chama *TIPO\_AFAST\_BG\_COLOR*;
- **fontColor**: será a cor da fonte escrita;

# Configuração de Grupo de Colunas em Interactive Grids (IG)

#### **Função - Guia de Uso**

---

Esta função `setCustomConfigIGColumns` foi criada para facilitar a configuração de grupos de colunas em Interactive Grids (IG) no Oracle APEX, permitindo uma organização mais eficiente e personalizada das colunas.

#### **Como Utilizar** 

---

**Sintaxe Básica:** `setCustomConfigIGColumns(config, options);`

##### **Parâmetros**

<table border="1" id="bkmrk-par%C3%A2metro-tipo-descr" style="border-collapse: collapse; width: 100%;"><colgroup><col style="width: 15.3754%;"></col><col style="width: 15.2991%;"></col><col style="width: 69.3254%;"></col></colgroup><thead><tr><td style="height: 29.7969px;">**Parâmetro**</td><td style="height: 29.7969px;">**Tipo**</td><td style="height: 29.7969px;">**Descrição**</td></tr></thead><tbody><tr><td style="height: 30.1094px;">`config` </td><td style="height: 30.1094px;">Object</td><td style="height: 30.1094px;">Objeto de configuração existente do IG (opcional)</td></tr><tr><td style="height: 29.7969px;">`options`</td><td style="height: 29.7969px;">Object</td><td style="height: 29.7969px;">Configurações personalizadas para grupos e colunas</td></tr></tbody></table>

#####  **Estrutura do Options**

```
{
  groups: [
    {
      name: "Nome do Grupo",                               // Nome visível do grupo
      id: "id-do-grupo",                                  // ID único (opcional - será gerado automaticamente se não informado)
      label: "Rótulo",                                   // Rótulo alternativo (opcional)
      columns: [
        {
          name: "Nome da Coluna",                 // Nome da coluna no IG
          hideHeader: true/false                 // Oculta o cabeçalho da coluna (opcional)
        }
      ]
    }
  ]
}
```

#### **Funcionamento Interno**

---

1. **Identificação da Grid**
2. **Criação/Atualização de Grupos**
3. **Configuração de Colunas:**
    - Para cada coluna dentro de um grupo: 
        - Vincula a coluna ao grupo pai
        - Aplica configurações adicionais (como ocultar cabeçalho)
    - Para cada grupo definido em `options.groups`, a função: 
        - Cria um novo grupo (se não existir)
        - Atualiza grupos existentes com as novas configurações
    - A função tenta obter o ID do IG automaticamente se não for fornecido no `config`.
4. **Retorno:**
    - Retorna o objeto `config` atualizado com os novos grupos e configurações.

##### **Exemplo Prático**

```
(originalConfig) => setCustomConfigIGColumns(originalConfig, {
  context: this,                   // opcional (elemento de contexto)
  groups: [
    {
      name: "Dados do Pneu",
      columns: [
        { name: "Sulco"},
        { name: "Pneu", hideHeader: true }
      ]
    }
  ]
})
```

##### **Observações Importantes**

1. A função **não substitui** configurações existentes - apenas as complementa
2. Se o ID do grid não for encontrado automaticamente, será necessário fornecer `config.regionStaticId`
3. Use `console.log` para verificar a configuração gerada antes de aplicar ao IG

##### **Benefícios**

✔ Organização visual de colunas em grupos temáticos

✔ Facilidade de manutenção das configurações

✔ Compatível com grids existentes

✔ Personalização flexível de cabeçalhos

#### **Aplicando a chamada**

---

Aplicar a chamada no "**Javascript Inicialization Code**" presente dentro da Interactive Grid para poder apontar as colunas que irão receber o GrupoPai

<p class="callout info">**💡** Lembrando que a **utilização é só recomendada quando precisa-se de um nível acima do grupo que o Apex já disponibiliza.**</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/LmKimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/LmKimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/yZUimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/yZUimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/Pqjimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/Pqjimage.png)

# Extrair Valor de uma Coluna

Para extrair o valor de uma determinada coluna utilize a função `getIGColumnValue`, que está disponível em todas aplicações baseadas no nosso template.

Existem **duas formas** de utilizar a função: Extrair o valor da coluna ao navegar nos registros da grid ou a partir de eventos independentes da grid.

#### **Navegando nos Registros da Grid** 

---

Utilize o evento "**onSelectionChange**" da grid, para executar um "**setValue**"em um item de página.

Quando chamada a partir desse evento, a função pode receber diretamente o objeto **"data"**.

```
getIGColumnValue(this.data, 'COD_EXEMPLO')
```

<p class="callout info"> 👀 **Observação:** O set type deve ser "JavaScript Expression".</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/1Itimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/1Itimage.png)

#### **Eventos Independentes da Grid** 

---

Faça a chamada da função passando o Static ID da grid, e a coluna cujo deseja extrair o valor.

```
getIGColumnValue('ig-exemplo', 'COD_EXEMPLO')
```

#### **Extras** 

---

Para **ambos os casos**, caso a intenção seja **determinar o índice do registro (e não somente o primeiro registro selecionado)**, é possível passar esse índice como o último parâmetro.

```
// numa grid com 4 registros selecionados [10,20,30,40]

let igStaticID = 'ig-exemplo';

apex.region(igStaticID).call('getSelectedRecords').forEach((reg, index) {
  apex.item('P30_EXEMPLO').setValue(getIGColumnValue(igStaticID , 'COD_EXEMPLO', index));
});

// volta 1 = P30_EXEMPLO receberá = 10
// volta 2 = P30_EXEMPLO receberá = 20
// volta 3 = P30_EXEMPLO receberá = 30
// volta 4 = P30_EXEMPLO receberá = 40

// para cada volta o evento onChange do item será disparado.
```

# Forçar o Evento Select onChange

Em páginas cujo existem elementos dependentes da seleção de registros em grid, precisamos forçar a chamada do evento SelectionChange da grid logo que a página é carregada.

Para isso crie uma **Dynamic Action** de "**onPageLoad**" que executará o seguinte JavaScript code:

```javascript
forceIGSelectionChange('ig-exemplo');
```

Para garantir que o método seja chamado após a população da grid, o Atributo "**Lazy Loading**" da mesma deve estar desligado.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/ddXimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/ddXimage.png)

<p class="callout warning">Para não criar alertar de padrão por falta do **Lazy Load**, devemos colocar no final do título da grid o **"...-nolazy"**.</p>

##### **Exemplo**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/QBaimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/QBaimage.png)

Agora crie uma **Dynamic Action** na grid pai, com o tipo de evento **Selection Change**, executando uma **True Action JS** do mesmo código JavaScript:

```javascript
forceIGSelectionChange('ig-exemplo');
```

É importante que as colunas **PK** da grid filha (dependente) estejam marcadas com a ***Flag*** de ***Primary Key***.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/m9Oimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/m9Oimage.png)

Também é importante manter ativo o atributo "**Select First Row**", pois é justamente através dele que o método consegue retornar o foco para o primeiro registro da grid.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/ZJ6image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/ZJ6image.png)

# Hide Column

Em algumas telas é necessário que de acordo com o filtro ou opção de visualização do usuário seja possível aparecer apenas algumas colunas da grid, para essa dinâmica utilizamos o Javascript.

Para preparar essa dinâmica devemos colocar um **Static ID na grid** que recebe a ação.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/gKOimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/gKOimage.png)

<p class="callout info">💡 **Não precisa ser o mesmo nome** da grid.</p>

Quando for devido a opção de visualização do usuário, por exemplo com uma **Select List** ou um **CheckBox**, devemos colocar um evento **onChange** e uma ação **Execute JavaScript Code** no item que faz a alteração.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/3Daimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/3Daimage.png)

Dentro da ação no ***Code Editor*** devemos colocar o seguinte código para estabelecermos a grid:

```
let gridView = apex.region('ig-contrato').call('getViews').grid;
```

<p class="callout success">⭐ O `'ig-contrato'` seria o **Static-ID** de sua grid</p>

Depois devemos validar se a o retorno do Page Item é o esperado para mostrar ou esconder determinada coluna

```
if (apex.item('P80_TODAS_FILIAIS').getValue() == 'N') {
  gridView.view$.grid('hideColumn', 'GEF');
} else {
  gridView.view$.grid('showColumn', 'GEF');
}
```

<p class="callout info">💡 `'hideColumn'` para esconder e `'showColumn'` para mostrar a visualização da coluna na grid.  
Onde está '**COD\_GRUPOEMPRESA**' é o nome da coluna(da maneira que está na Column Name dentro da grid) a qual deseja esconder ou mostrar em sua grid.</p>

---

**Tela exemplo ➝** [40255:80](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-ifrs-16/contrato?session=9214413713697)

# IG - Interactive Grids

#### **Utilização do Template Interactive Grid no Wizard de Criação de Páginas**

---

É permitido utilizar o template "Interactive Grid" do APEX durante a criação de página.

<p class="callout success">⭐ As duas colunas que o Apex cria por padrão: `APEX$ROW_SELECTOR e APEX$ROW_ACTION` **devem ser removidas.**</p>

####  **Padronização do Nome**

---

Utilizamos a nomenclatura `ig-(nome-da-grid)` para o **Identification &gt; Title** das grids.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/7Tnimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/7Tnimage.png) [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/9eoimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/9eoimage.png)

#### **Configuração do Layout**

---

##### **Tamanho**

A distribuição das colunas e seus tamanhos deve ser feita no tempo de execução da página durante o desenvolvimento.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/ymyimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/ymyimage.png) [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/VRIimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/VRIimage.png)

<p class="callout info">**💡** Atente-se para a largura dos campos de código. <u>Em campos numéricos</u>, recomenda-se definir a largura da coluna para **80px**. Em campos de descrição recomenda-se não definir tamanho fixo, para o APEX efetuar a responsividade usando ele.</p>

<p class="callout danger">**Não** **capitalize os textos** da descrição, assim o usuário pode escolher como escrever a descrição da maneira que melhor lhe atenda.</p>

##### **Ordenação**

A **ordenação padrão** deve ser feita de forma que ao inserirmos um novo registro, o mesmo permaneça no topo da tela logo após o *refresh* da grid.

Caso a tabela tenha **CODIGO ou ID (auto incremento)**, ordene esse **campo em ordem decrescente.** Esse procedimento foi adotado para que o usuário possa identificar prontamente/visualmente que o registro foi inserido.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/RpDimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/RpDimage.png)

Em colunas do tipo "texto" na grid, altear type ( **Identification &gt; Type** ) de TEXTAREA para TEXTFIELD.

<p class="callout info">Após definir o layout desejado, vá em **Actions &gt; Report &gt; Save Report** para salvar o layout como o layout padrão para os usuários.  
[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/3Naimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/3Naimage.png)  
</p>

#### **Painel Padrão**

---

Toda grid terá a seguinte chamada no **JavaScript Initialization Code**

**Region &gt; Attributes &gt; JavaScript Initialization Code**

```
setCustomConfig
```

Este código deverá ser inserido após a configuração do layout padrão.

**Exemplo:**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/Gkqimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/Gkqimage.png)

#### **Lazy Loading**

---

Sempre ativar o Lazy Loading da Grid

**Region &gt; Attributes &gt; Performance**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/GW1image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/GW1image.png)

Sempre desative o Add Row If Empty

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/wzTimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/wzTimage.png)

#### **Configuração de Impressão**

---

As configurações padrão de impressão são definidas na aba **Printing** das propriedades da Interactive Grid.

As seguintes propriedades devem ser definidas:

- **Page &gt; Size** = A4;
- **Page Header &gt; Page Header Text** = título da grid.

<p class="callout warning">O título da grid deve ser um **nome para o conteúdo** da grid e **não '`ig-exemplo`'**</p>

# Manter Linhas Selecionadas (Submit e Fila de Execução)

Está funcionalidade permite que a Interactive Grid mantenha salva a seleção de várias linhas após processos de submit na página ou após a Fila de execução.

#### **Como Utilizar**

---

Para utilizar a funcionalidade, é necessário chamar a função `"keepSelectionIG(ig_static_id);"` passando o ID da grid específica como parâmetro através no **Execute when Page Loads.**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/cqLimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/cqLimage.png)

```
keepSelectionIG(ig_static_id);
```

#### **Fila de Execução**

---

Para **funcionar com a Fila de Execução** é necessário criar na D.A (*Dynamic Action*) do “Dialog Closed” da Fila de execução desejada, uma action de "Execute JavaScript code" com o código `“keepDialogSelectionIG(ig_static_id)”:`

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/Uutimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/Uutimage.png)

```
keepDialogSelectionIG(ig_static_id);
```

#### **Tela Exemplo com o Resultado Esperado (40104:1771)**

---

[![gif-demo-manter-selecao.gif](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/gif-demo-manter-selecao.gif)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/gif-demo-manter-selecao.gif)

# Menu de Ação Customizável (Actions Menu)

Em casos bem específicos, pode ser necessário criar um menu de ação customizável para executar algum processo ou ação única para a linha da grid. Para isso, podemos utilizar o **"Actions Menu"**.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/4ZJimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/4ZJimage.png)

Para utilizar o menu de ações é necessário **adicionar uma nova coluna do tipo Actions Menu** na grid que irá utilizar o menu.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/fMpimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/fMpimage.png)

Depois de adicionada a coluna, agora iremos configurar as opções no campo "Javascript Initialization Code" nos atributos da GRID.

**Exemplo:**

```javascript
(config) => setCustomConfig(config, {
  contextMenu: 'S',
  rowActions: [{
    label: 'Ativar Conta', icon: 'fa-check', action: (model, records) => {
      $('#BTN_CHAMA_ATIVA').trigger('click');
       apex.item('P140_COD_FORNECEDOR_AUX').setValue(model.getValue(records[0], 'COD_FORNECEDOR'));
       apex.item('P140_COD_BANCO_AUX').setValue(model.getValue(records[0], 'COD_BANCO').v);
    }
  },
  {
    label: 'Desativar Conta', icon: 'fa-ban', action: (model, records) => {
      $('#BTN_CHAMA_FECHAMENTO').trigger('click');
      apex.item('P140_COD_FORNECEDOR_AUX').setValue(model.getValue(records[0], 'COD_FORNECEDOR'));
      apex.item('P140_COD_BANCO_AUX').setValue(model.getValue(records[0], 'COD_BANCO').v);
    }
  },
  {
    label: 'Visualizar Histórico', icon: 'fa-search', action: (model, records) => {
      console.log('act model', model);
      console.log('act records', records);
      console.log('field', model.getValue(records[0], 'COD_FORNECEDOR'));
    }
  }]
})
```

<p class="callout success">⭐ O atributo `"contextMenu"` deverá ser **setado como 'S'.**</p>

As opções deverão ser montadas de acordo com a necessidade da tela, para cada "nova opção", deverá ser incluída uma nova label, bem como qual ação esta opção realizará (executar um processo, abrir uma nova página, etc...).

<p class="callout warning">**IMPORTANTE:** Como é possível notar, o menu de ações é montado por javascript, no entanto, devido a assincronicidade do javascript com os componentes do apex, especialmente com a interactive grid, devemos evitar ao máximo escrever códigos javascript complexos.</p>

<span class="ql-bg-yellow">Caso o botão do menu de ação precise executar um processo. O ideal é fazer com que um botão (escondido) execute todo o processo, e por javascript "forçar" o click neste botão. Fazendo com que o processo execute de forma "nativa" no apex.</span>

---

**Tela de Exemplo:** [40104:140](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-folha-de-pagamento/cadastro-de-pensionistas?session=9214413713697) - Cadastro de Pensionistas - 7272

# Popular Collection sem Rodar a Query da Grid Novamente (Scroll e Paginada)

O código a seguir foi feito por conta da necessidade de popular uma collection no process rows onde os dados vem de uma query que é pesada e demora para carregar.

O modo convencial onde criamos as DAs de criação de collection depois populamos a mesma com o evento Process Rows realiza um "refresh" na query da grid de origem, como a query é pesada acabava travando e demorando demais.

**O código é simples:**

1. Percorre os registros marcados da grid e **popula um JSON** que é salvo em um item da página;
2. Cria a collection e faz o insert na mesma utilizando o JSON como **fonte de dados e não o process Rows**;

---

Para utilizar crie os seguintes eventos na ordem no **onClick do botão ou onde você teria a lógica de popular a collection**.

##### **Popular JSON com registros selecionados (Execute JavaScript Code)**

```javascript
var ig$ = apex.region("ig-AnimaisConsumo").widget();
var grid = ig$.interactiveGrid("getViews", "grid");
var model = grid.model;
var selectedRecords = grid.getSelectedRecords();

var data = [];

selectedRecords.forEach(function(record) {
    data.push({
        c001: model.getValue(record, "SEQUENCIAANIMAL"),
        c002: model.getValue(record, "NOMEANIMAL"),
        c003: model.getValue(record, "DATANASCIMENTO"),
        c004: model.getValue(record, "ERA"),
        c005: model.getValue(record, "PESO"),
        c006: model.getValue(record, "RGD"),
        c007: model.getValue(record, "RGN"),
        c008: model.getValue(record, "SIGLAUSUAL"),
        c009: model.getValue(record, "NRSISBOV"),
        c010: model.getValue(record, "SEXO"),
        c011: model.getValue(record, "NOME_PROPRIETARIO"),
        c012: model.getValue(record, "COD_FAZENDA"),
        c013: model.getValue(record, "DESCRICAOFAZENDA"),
        c014: model.getValue(record, "ZONA"),
        c015: model.getValue(record, "PASTO"),
        c016: model.getValue(record, "DESCRICAOPASTO"),
        c017: model.getValue(record, "DESCRICAORACA"),
        c018: model.getValue(record, "DESCRICAOCATEGORIA"),
        c019: model.getValue(record, "DESCRICAOFINALIDADE"),
        c020: model.getValue(record, "DESCRICAOGRPSANGUINEO"),
        c021: model.getValue(record, "COD_FORNECEDOR"),
        c022: model.getValue(record, "SEQUENCIARACA"),
        c023: model.getValue(record, "SEQUENCIACATEGORIA"),
        c024: model.getValue(record, "SEQUENCIAFINALIDADE"),
        c025: model.getValue(record, "SEQUENCIAGRPSANGUINEO")
    });
});

// store JSON
apex.item("P1670_JSON").setValue(JSON.stringify(data));
```

##### **Criar collection (Execute Server-Side Code)**

```javascript
csweb.pkg_apex_collection.pr_create_collection(p_collection_name => 'CONFIRMA_CONSUMO_ANIMAL');
```

##### **Popular Collection utilizando JSON (Execute Server-Side Code)**

```javascript
declare
    l_json clob := :P1670_JSON;
begin

    delete csagropecuaria.apex_tmp_animalmarcado
    where idlogon = :G_ID_LOGON;

    for rec in (
        select *
        from json_table(l_json, '$[*]'
            columns (
                c001 number path '$.c001',
                c002 varchar2(200) path '$.c002',
                c003 date path '$.c003',
                c004 varchar2(50) path '$.c004',
                c005 number path '$.c005',
                c006 varchar2(50) path '$.c006',
                c007 varchar2(50) path '$.c007',
                c008 varchar2(50) path '$.c008',
                c009 varchar2(50) path '$.c009',
                c010 varchar2(10) path '$.c010',
                c011 varchar2(200) path '$.c011',
                c012 number path '$.c012',
                c013 varchar2(200) path '$.c013',
                c014 varchar2(50) path '$.c014',
                c015 varchar2(50) path '$.c015',
                c016 varchar2(200) path '$.c016',
                c017 varchar2(200) path '$.c017',
                c018 varchar2(200) path '$.c018',
                c019 varchar2(200) path '$.c019',
                c020 varchar2(200) path '$.c020',
                c021 number path '$.c021',
                c022 number path '$.c022',
                c023 number path '$.c023',
                c024 number path '$.c024',
                c025 number path '$.c025'
            )
        )
    ) loop
        csweb.pkg_apex_collection.pr_add_member(
            p_collection_name => 'CONFIRMA_CONSUMO_ANIMAL',
            p_c001 => rec.c001,
            p_c002 => rec.c002,
            p_c003 => rec.c003,
            p_c004 => rec.c004,
            p_c005 => rec.c005,
            p_c006 => rec.c006,
            p_c007 => rec.c007,
            p_c008 => rec.c008,
            p_c009 => rec.c009,
            p_c010 => rec.c010,
            p_c011 => rec.c011,
            p_c012 => rec.c012,
            p_c013 => rec.c013,
            p_c014 => rec.c014,
            p_c015 => rec.c015,
            p_c016 => rec.c016,
            p_c017 => rec.c017,
            p_c018 => rec.c018,
            p_c019 => rec.c019,
            p_c020 => rec.c020,
            p_c021 => rec.c021,
            p_c022 => rec.c022,
            p_c023 => rec.c023,
            p_c024 => rec.c024,
            p_c025 => rec.c025,
            p_c026 => :G_ID_LOGON,
            p_c027 => :P1670_DATA_CONSUMO
        );
    end loop;
end;
```

**Página de exemplo:** Aplicação 40851 &gt; Página 1670 &gt; onClick btn-RealizarConsumo

<p class="callout warning">**Atenção:**  
Evite depender de lógica em JavaScript para **regras críticas**, pois ela pode ser afetada por outros erros na página. Utilize apenas quando **não for possível melhorar a performance da query no backend.**</p>

<div class="codeContainer__75297" id="bkmrk--1">  
</div><div class="codeContainer__75297" id="bkmrk--2">  
</div><div class="codeContainer__75297" id="bkmrk--3">  
</div>

# Read Only em Célula Específica

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/f7nimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/f7nimage.png)

Assim como está nessa imagem, segue o passo a passo de como marcar um campo/célula específica como read only, baseando-se em um client-side condition, que será definido na condição do valor de outra coluna:

Selecionar a coluna que deseja aplicar o Read Only, criar uma Dynamic Action nela com as seguintes propriedades:

- **Event:** Click;
- **Advanced ➝ Event Scope:** Dynamic;
- **Static Container (jQuery Selector):** body;

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/Qcgimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/Qcgimage.png)

Essa Dynamic Action terá uma True Action "Disable" com "Fire on Initialization" ativado.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/Irrimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/Irrimage.png)

Na propriedade **"Affected Elements"** selecione a própria coluna na qual foi criada a **Dynamic Action**. Essa True Action terá um **Client-side Condition do tipo "Item/Column = Value"**, sendo o **Component Type: Column** e, posteriormente, selecionando a coluna de onde virá o seu valor base para definir se sua cédula será read only ou não.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/GS3image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/GS3image.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/1SFimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/1SFimage.png)

---

**Tela exemplo ➝** [40111:120](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-ponto-eletronico/layout-import-export-coletor?session=9214413713697)

# Somente Ativos (Input Header)

Nas telas que listam um histórico ou que possuem dados que possuem uma data final utilizamos normalmente um **Checkbox** para mostrar os dados que já encerraram caso seja desejo do usuário. Para isso colocamos no H*eader da Grid* para ser de uma acessibilidade maior para o usuário

#### **Header da Grid**

---

Para fazermos isso vamos primeiro colocar um **Static ID** na região com o header que irá receber os itens dentro dele - no exemplo abaixo o ID é colocado na **região container da grid**:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/sY3image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/sY3image.png) [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/lDcimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/lDcimage.png)

<p class="callout info">👀 O ID dado deve ser **de acordo com a decisão do desenvolvedor**.</p>

No Page Item vamos colocar um ID para ele também, lembrando que não importa onde o item foi criado pois ele irá para o Header desejado.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/Jpvimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/Jpvimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/UVqimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/UVqimage.png)

<p class="callout info">👀 Seu **ID deve ser único para o Page Item**, o comando possui `'style="padding-inline-end: 5px"'` para ficar centralizado e ao final do Header.</p>

```
<div id="checkbox-ativo" style="padding-inline-end: 5px">
```

#### **Posição do Item**

---

Para posicionarmos o item agora devemos colocar um código no **Execute when Page Loads** da página na área de *JavaScript.*

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/UYuimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/UYuimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/fAQimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/fAQimage.png)

```
setHeaderInputBefore('ocorrencias', 'checkbox-ativo');
```

<p class="callout warning">**Atenção:** no lugar de "**ocorrencias" deve ser o ID de sua Região** e no lugar de "**checkbox-ativo" deve ser o ID do seu Page Item**.</p>

#### **Somente Ativos**

---

Agora para fazer a lógica dos registros **Somente ativos** você precisa criar dentro da grid um case para isso.

```
where  case when :P81_SOMENTE_ATIVOS  = 'N' then 1
            when data_fim is null or data_fim >= sysdate  then 1
       end = 1 
```

<p class="callout info">**👀 Observação:** o `':P81_SOMENTE_ATIVOS'` deve ser o seu page item e a `'data_fim'` deve ser a coluna de sua grid que armazena a data final.</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/esvimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/esvimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/NVeimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/NVeimage.png)

<p class="callout info">💡 Lembrar de colocar o seu <u>Page Item</u> como **Page Items to Submit.**</p>

Agora só falta colocar uma *Dynamic Action* no *Page Item*, no evento **onChange** colocar uma ação de **Refresh** na grid.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/3kWimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/3kWimage.png) [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/oJbimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/oJbimage.png)

---

**Tela exemplo ➝** 40255:81

# Totalizadores - IG

### Visão Geral

O componente permite exibir totalizadores sempre visíveis para uma *Interactive Grid* do Oracle APEX.

Existem duas formas principais de uso:

- **Totalizador configurado:** usa a função `initIGTotalizer` e calcula as colunas informadas manualmente.
- **Totalizador nativo:** usa a função `inicializarTotalizadoresIgNativos` e reaproveita automaticamente as agregações nativas configuradas na própria grid.

#### Pré-requisitos

1. Defina um **Static ID** para a região da Interactive Grid.
2. Para o modo nativo, configure as agregações diretamente pela Interactive Grid.
3. Para o modo configurado, informe as colunas desejadas na chamada da função.

### Totalizador Configurado

Use `initIGTotalizer` quando a intenção for passar estaticamente quais colunas devem ser totalizadas.

#### Chamada básica

```
initIGTotalizer({
    regionId: "ig-ajuste-pis",
    columns: [
        {
            field: "VL_AJ",
            label: "Valor"
        },
        {
            field: "VL_AJ",
            label: "Valor selecionado",
            selectedTotal: true
        },
        {
            field: "ALIQ_PIS",
            label: "Alíquota",
            highlightStatus: true
        }
    ]
});
```

#### Parâmetros principais

<table id="bkmrk-atributo-tipo-padr%C3%A3o"><thead><tr><th>Atributo</th><th>Tipo</th><th>Padrão</th><th>Descrição</th></tr></thead><tbody><tr><td>`regionId`</td><td>String</td><td>-</td><td>Static ID da Interactive Grid usada pelo totalizador configurado.</td></tr><tr><td>`columns`</td><td>Array</td><td>-</td><td>Lista de colunas que serão totalizadas.</td></tr></tbody></table>

#### Parâmetros das colunas

<table id="bkmrk-atributo-tipo-padr%C3%A3o-1" style="width: 100%;"><thead><tr><th style="width: 16.6826%;">Atributo</th><th style="width: 8.10534%;">Tipo</th><th style="width: 16.3227%;">Padrão</th><th style="width: 58.8656%;">Descrição</th></tr></thead><tbody><tr><td style="width: 16.6826%;">`field`</td><td style="width: 8.10534%;">String</td><td style="width: 16.3227%;">-</td><td style="width: 58.8656%;">Nome da coluna da Interactive Grid.</td></tr><tr><td style="width: 16.6826%;">`label`</td><td style="width: 8.10534%;">String</td><td style="width: 16.3227%;">Nome da coluna</td><td style="width: 58.8656%;">Rótulo exibido antes do valor.</td></tr><tr><td style="width: 16.6826%;">`selectedTotal`</td><td style="width: 8.10534%;">Boolean</td><td style="width: 16.3227%;">`false`</td><td style="width: 58.8656%;">Quando `true`, soma apenas as linhas selecionadas.</td></tr><tr><td style="width: 16.6826%;">`highlightStatus`</td><td style="width: 8.10534%;">Boolean</td><td style="width: 16.3227%;">`false`</td><td style="width: 58.8656%;">Quando `true`, aplica destaque visual para valor positivo ou negativo.</td></tr><tr><td style="width: 16.6826%;">`format`</td><td style="width: 8.10534%;">String</td><td style="width: 16.3227%;">Número com 2 casas</td><td style="width: 58.8656%;">Use `"number"`, `"numero"` ou `"número"` para número simples; use `"currency"`, `"moeda"`, `"monetario"`, `"monetário"` ou `"brl"` para moeda.</td></tr></tbody></table>

### Totalizador Nativo

Use `inicializarTotalizadoresIgNativos` quando a intenção for reaproveitar automaticamente os totalizadores nativos configurados na Interactive Grid.

- **Leitura automática:** Não é necessário informar manualmente as colunas.
- **Compatível com paginação:** Pode buscar todas as páginas do model para manter o total global correto.
- **Atualização automática:** Recalcula após paginação, refresh, filtros, mudanças de relatório e ajustes estruturais da grid.
- **Exibição na própria grid:** Mantém os totalizadores visíveis dentro da área da Interactive Grid.

#### Chamada básica

```
inicializarTotalizadoresIgNativos({
    igId: "ig-ajuste-pis"
});
```

Nesse formato, a função usa o **Static ID** da grid, identifica as agregações nativas configuradas e exibe os totalizadores junto da própria Interactive Grid.

#### Parâmetros principais

<table id="bkmrk-atributo-tipo-padr%C3%A3o-2" style="width: 100%;"><thead><tr><th style="width: 11.2011%;">Atributo</th><th style="width: 12.3928%;">Tipo</th><th style="width: 14.3029%;">Padrão</th><th style="width: 62.0794%;">Descrição</th></tr></thead><tbody><tr><td style="width: 11.2011%;">`igId`</td><td style="width: 12.3928%;">String</td><td style="width: 14.3029%;">-</td><td style="width: 62.0794%;">Static ID da Interactive Grid usada pelo totalizador nativo.</td></tr><tr><td style="width: 11.2011%;">`fetchAll`</td><td style="width: 12.3928%;">Boolean</td><td style="width: 14.3029%;">`true`</td><td style="width: 62.0794%;">Permite carregar todas as páginas do model para encontrar ou recalcular os totalizadores globais. Em grids muito grandes, pode ser definido como `false`.</td></tr></tbody></table>

#### Aliases aceitos

<table id="bkmrk-uso-recomendado-alia"><thead><tr><th>Uso recomendado</th><th>Aliases aceitos</th></tr></thead><tbody><tr><td>`igId`</td><td>`ig`, `grid`, `gridId`, `idGrid`, `gridStaticId`, `idEstaticoGrid`</td></tr><tr><td>`fetchAll`</td><td>`allowFetchAll`, `permitirFetchAll`, `buscarTodasPaginas`, `buscarTodasPáginas`, `carregarTodasPaginas`</td></tr></tbody></table>

### Boas Práticas

- Use sempre o Static ID da Interactive Grid.
- Use `initIGTotalizer` quando quiser informar colunas manualmente.
- Use `inicializarTotalizadoresIgNativos` quando quiser reaproveitar as agregações nativas da grid.
- Se a grid for recriada por refresh ou mudança de relatório, não é necessário chamar a função novamente; a instância já observa esses eventos.

# Introdução ao APEX

#### **Visão Geral Projeto 4.0**

---

No Projeto 4.0, adotamos padrões estruturados para facilitar a manutenção e escalabilidade de todo o projeto.

Adotamos o framework Oracle APEX por ser uma plataforma de desenvolvimento low-code para criar aplicativos web escaláveis e seguros, garantindo a eficiência no código e produtividade.

#### **Scaffold - Estrutura e Motivo de Existência**

---

O Scaffold define a estrutura base do projeto, garantindo padronização e reaproveitamento de código.

- **Subscription:** Permite que temas, plugins e componentes gerais sejam herdados e atualizados centralmente.
- **Arquivos CSS e JS:** O Scaffold estende arquivos globais, garantindo um padrão visual e comportamental.
- **Alterações e Publicação:** Para modificar CSS e JS, é necessário seguir o fluxo de alteração e publicar o tema corretamente.

#### **CS-Template - Estrutura e Motivo de Existência**

---

O CS-Template define padrões de layout e organização, evitando inconsistências visuais e funcionais.

#### **Criação de um Novo Módulo**

---

Para a criar um novo módulo seguiremos um padrão definido no início do projeto quanto aos números de aplicações.

Onde os números para gestão seguiremos uma range de 50 números, A gestão sempre terminará com zero (0), como está explicado no guideline sobre [criação de módulos](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/novo-modulo "Novo Módulo").

#### **Criação de Páginas e seus Padrões**

---

- **Numeração:** Utilizar dezenas para páginas principais e números unitários para modais.
- **Nomenclatura:** Definir títulos e identificadores seguindo um padrão consistente.
- **Itens, Regiões e Botões:** Nomeação estratégica para facilitar manutenção e reutilização.

#### **Detalhes Técnicos do APEX**

---

A partir desta parte é muito importante ter assistido os vídeos da Trust disponibilizados em nosso diretório.

**Diretório**: P:\\Time 4.0\\Curso APEX

##### **Posição dos Botões de Salvar e Excluir**

---

Definir posicionamento fixo para garantir usabilidade e padronização.

Acesse o design system para saber mais sobre [padronização visual](https://wiki.cscompusoftware.com.br/books/erp-guideline-de-uiux "Design System").

##### **Editor para Campo Fórmula (Monaco)**

---

O Monaco Editor é utilizado para edição avançada de fórmulas e expressões no APEX.

Foi criado para que o usuário entenda que é um conteúdo mais avançado a fim de evitar a edição do conteúdo acidentalmente.

Saiba mais informações técnicas em: [Editor para Campo Fórmula](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/chapter/editor-para-campo-formula "Dev Guideline")

Saiba mais sobre os padrões visuais em: [Textos longos](https://wiki.cscompusoftware.com.br/books/erp-guideline-de-uiux/page/textos-longos#bkmrk-markdown-editor---mo "UI/UX Guideline")

##### **CS-Collection**

---

**O que é e para que serve:** Coleções permitem que você capture temporariamente um ou mais valores não escalares. Você pode usar coleções para armazenar linhas e colunas atualmente em estado de sessão para que elas possam ser acessadas, manipuladas ou processadas durante uma sessão específica do usuário. Você pode pensar em uma coleção como um **bucket** no qual você armazena e nomeia temporariamente linhas de informações.

**Comparação com a Collection do APEX:** Melhor performance e flexibilidade.

##### **Tipos de CS-Collection**

##### Normal (coleção padrão):

- Descrição: É o tipo padrão de coleção. Usada na maioria dos casos.
- Capacidade: Pode armazenar até 50 colunas e cerca de 32 mil linhas por sessão (**limite prático, não oficial**).
- Uso ideal: Quando você precisa trabalhar com uma quantidade razoável de dados temporários (como registros de uma grid ou dados de um formulário que ainda não foram persistidos no banco).

**Vantagens:**

- Rápida
- Simples de usar
- Boa performance com volumes comuns

##### Médium Data (coleção para dados médios):

- **Descrição**: Usada quando você precisa trabalhar com coleções que lidam com um volume maior de dados do que o normal.
- **Capacidade**: Suporta mais colunas do que a coleção normal, mantendo uma performance aceitável.
- **Uso ideal**: Quando você precisa carregar milhares de registros em memória para a sessão, mas ainda não atinge o nível de “**Big Data**”

##### Big Data (coleção para grandes volumes):

- **Descrição**: Coleções voltadas para grandes volumes de dados, onde a quantidade de linhas pode ser bem alta (milhares ou até milhões, dependendo da memória disponível).
- **Capacidade**: Suporta um número de colunas bem maior do que o “**Medium Data**”, mas com mais consumo de memória e possivelmente menos performance.
- **Uso ideal**: Situações onde é necessário manipular grandes massas de dados temporariamente, como uploads em massa, análises, pré-processamentos.

##### Principais Diferenças:

<table border="1" id="bkmrk-tipo-performance-vol" style="border-collapse: collapse; width: 100%;"><colgroup><col style="width: 20.0191%;"></col><col style="width: 20.0191%;"></col><col style="width: 20.0191%;"></col><col style="width: 20.0191%;"></col><col style="width: 20.0191%;"></col></colgroup><thead><tr><td class="align-center">**Tipo**

</td><td class="align-center">**Performance**

</td><td class="align-center">**Volume de Dados**

</td><td class="align-center">**Complexidade**

</td><td>**Uso Típico**

</td></tr></thead><tbody><tr><td class="align-center">Normal</td><td class="align-center">Alta</td><td class="align-center">Baixo a Médio</td><td class="align-center">Baixa</td><td>Grids simples, formulários, wizards</td></tr><tr><td class="align-center">Médium</td><td class="align-center">Média</td><td class="align-center">Médio a Alto</td><td class="align-center">Média</td><td>Consultas intermediárias, dados temporários grandes</td></tr><tr><td class="align-center">Big Data</td><td class="align-center">Baixa</td><td class="align-center">Alto a muito Alto</td><td class="align-center">Alta</td><td>Processamentos pesados, uploads grandes</td></tr></tbody></table>

<p class="callout info">**📎 Nota técnica:** No Oracle APEX, essa classificação não é feita com uma opção declarada no código como **NORMAL** ou **BIG DATA**, mas sim pela forma como a coleção é usada, pela quantidade de dados, e como a aplicação trata a memória e o estado da sessão.</p>

 Saiba mais sobre collections em: [Collections](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/chapter/collections "Dev Guideline")

##### **Fila de Execução**

---

- **O que é e para que serve:** A fila de execução no Oracle APEX é a ordem lógica em que os diferentes componentes da aplicação **<u>(como processos, validações, cálculos e ações dinâmicas</u>**) são executados em resposta a um evento, como o clique de um botão ou a submissão de uma página. **Serve para:**
    - Controlar a ordem de execução de processos, ações e validações
    - Evitar conflitos entre ações (**exemplo: tentar usar dados que ainda não foram processados**)
    - Garantir consistência na manipulação de dados
    - Separar responsabilidades (**validação, processamento, navegação**)
    - Gerencia processos assíncronos no APEX
    - Funcionamento**:** Execução em etapas, otimizando o processamento

Saiba mais sobre a Fila de Execução em: [Fila de Execução](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/fila-de-execucao "Dev Guideline")

#####  **Filtros**

---

- **Filtro Simples (LOV):** Componente usado para listar valores dinâmicos ou fixos de simples seleção.
- **Multifiltro**: Componente usado para listar valores dinâmicos ou fixos de múltipla seleção
- **pr\_multifiltro**: Procedimento utilizado para lista um ou vários registros selecionados pelo componente “**multifiltro**”.
- **Filtros GEF**: São componentes de filtro simples geralmente utilizados para listar registro do grupo empresa e componente **multifiltro** para listar registros da empresa e filial podendo ou não selecionar vários registros ao mesmo tempo. Denomina-se “**Filtros GEF**” por listar a **GEF** em si.
- **pr\_GEF:** Procedimento utilizado para listar os registros da GEF.

#### **Conclusão**

---

Este onboarding foi estruturado para oferecer uma visão clara e objetiva sobre o uso do **Oracle APEX** no contexto do **Projeto 4.0**, destacando não apenas a ferramenta em si, mas também as boas práticas, padrões e componentes desenvolvidos para garantir **padronização, desempenho e escalabilidade**.

Tudo isso se conecta diretamente ao princípio que guia este projeto desde o início:

##### **"Código Consciente = Time Alinhado"**

**Quando todos seguem padrões claros, entendem a estrutura e fazem escolhas técnicas com propósito**, o time como um todo ganha em agilidade, coesão e qualidade nos resultados.

Este material serve como base de conhecimento para novos desenvolvedores e também como **referência contínua** ao longo do projeto. Recomendamos a todos os envolvidos que explorem também os vídeos do curso APEX disponíveis em nosso diretório, reforçando o aprendizado prático.

# Libs Externas

# LeaderLine

Essa lib pode ser utilizada de várias maneiras: Como dica visual, como guia de funcionalidade, descritivo de legendas e etc.

<p class="callout info">**👉 Referêcia:** [https://anseki.github.io/leader-line/](https://anseki.github.io/leader-line/)</p>

#### **Requisitos**

---

Adicione o arquivo de script no "**File URLs**" da página

```
#THEME_DB_FILES#scripts/leader-line.min.js
```

####  **Declaração**

---

Crie uma função de controle, no "**Function and Global Variable Declaration**" da página

```
function setLeaderLine(startId, endId) {
  return new LeaderLine({
    start: LeaderLine.pointAnchor(document.getElementById(startId), {
      x: 10,
      y: 15,
    }),
    end: LeaderLine.pointAnchor(document.getElementById(endId), {
      x: -5,
    }),
    path: 'grid',
    color: '#838c91',
    startPlug: 'behind',
    endPlug: 'behind',
    startSocket: 'bottom',
    endSocket: 'left',
    startSocketGravity: 0,
    endSocketGravity: 10,
  });
}
```

<p class="callout info"> Utilize a [documentação oficial](https://anseki.github.io/leader-line/ "Documentação Leaderline - Github") para **customizar a função de controle**.</p>

No Item que deseja destacar, crie uma div no "**Pre Text**"

```
<div id="node1"></div>
```

#### **Utilização**

---

Faça a chamada da função de controle no "**Execute when Page Loads**" ligando os elementos desejados pelo seu id (conforme determinados no pre text)

```
setLeaderLine('node1', 'node2');
```

####  **Resultado**

---

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/8Xaimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/8Xaimage.png)

**Tela de exemplo:** [40501:180](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-seguranca/configuracao-lgpd?session=9214413713697)

# Menu

# Aplicativo por Time

No DevTools, acesse a página [App por Time](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-dev-tools/aplicativo-por-time) (Oracle Apex =&gt; APPs por Time):

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/zpVimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/zpVimage.png)

Selecione seu time e vincule os APPs (Módulos) que são de sua responsabilidade.

<p class="callout info">**👀 Obs:** Esse vinculo é extremamente importante, pois é através dele que **identificamos quais menus serão vinculados** no momento de **geração da Release**.</p>

# Página por Cliente

No DevTools, acesse a página [Página por Cliente](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-dev-tools/pagina-por-cliente) (Oracle Apex =&gt;Página por Cliente):

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/Cfximage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/Cfximage.png)

<p class="callout warning">É importante que as **páginas estejam liberadas corretamente** para cada cliente, pois, é por esse cadastro que a release se orienta para buscar quais páginas/menus de quais apps/módulos tiveram alteração e serão enviados na release.</p>

# Release

Uma vez Aplicativos vinculados ao [time](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/aplicativo-por-time "Aplicativo por Time") e páginas liberadas para os [clientes](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/pagina-por-cliente "Página por Cliente"), , agora basta enviar os menus para os clientes via Release.

Ao gerar a release atente para que a opção **"Menu Apex"** esteja selecionada:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/j5Limage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/j5Limage.png)

Após geração na aba "Menu Apex" temos a visão de todos **menus que serão enviados** para os clientes.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/oaRimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/oaRimage.png)

# Menu Popup

# Botão Popup de Lista

Para criar um botão que abre um popup com uma **lista de opções** como o da imagem a seguir, devemos seguir os seguintes passos.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/rt7image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/rt7image.png)

<p class="callout warning">Para **utilizar em botões dinâmico de Grid** não é necessário criar o botão estático do passo 1. Crie somente o List com template Menu Popup.</p>

#### **Passo a Passo**

---

**1° Passo:** Criar um botão na tela. No **page designer** do apex, devemos criar um botão normalmente, com o ícone "`fa-chevron-down`" e lembrando de deixar o ícone a direita da label do botão.

**2° Passo:** Criar uma r**egião do tipo "List"** na página e na aba **"Attributes"** da região List criada, devemos mudar o atributo "List Template" para "**Menu Popup**". Além disso podemos deixar a aparência da região como **"Blank with attributes"**. Também precisamos criar um id na região da lista, pelo campo **"Static ID".**

<p class="callout info">💡 Lembrando que é interessante que o **ID seja minimamente explicativo** ou siga um contexto pra **auxiliar na manutenção** da tela futuramente.</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/Y2Pimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/Y2Pimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/ttMimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/ttMimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/wk9image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/wk9image.png)

**3° Passo:** Criar uma lista no **Shared Component** do módulo que a tela está sendo criada.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/ns6image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/ns6image.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/tvOimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/tvOimage.png)

Na coluna **"Name"** cadastramos a label de cada opção da lista, na coluna **"Icon"** cadastramos qual ícone está atrelado à essa label, no momento vamos ignorar a coluna **"Target"**.

**4° Passo:** Atrelar a Lista criada pelo **Shared Component** na região List da Página.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/RXgimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/RXgimage.png)

<p class="callout warning">Para **utilizar em botões dinâmico de Grid** não é necessário configurar o botão estático do passo 5.</p>

**5° Passo:** No botão que criamos, precisamos configurar duas coisas. A primeira é fazer com que o botão não execute nada no click. Uma das formas de fazermos isso é mudar o seu behavior (Comportamento) para **"Defined by Dynamic Action"** e não criar nenhuma Dynamic Action atrelada à este botão. Além disso, precisamos passar o atributo, no campo Custom Attributes:

```
data-menu="staticIdDaLista_menu"
```

Devemos substituir os caracteres **\#staticIdDaLista** pelo respectivo ID da lista setado anteriormente. Lembrando de manter o sufixo: "`_menu`". Exemplo:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/9U9image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/9U9image.png)

Após seguir estes passos, o botão já deve estar funcionando corretamente e abrindo a lista que foi criada. Porém ao clicar em alguma opção da lista, nada irá acontecer. Neste momento vamos **utilizar a coluna "target" do cadastro da lista.**

Caso seja necessário **apenas abrir uma página da mesma aplicação da sua página atual**, o processo é mais simples, sendo necessário **apenas passar o ID da página** que a sua opção da lista precise abrir, com isso, o apex abrirá a respectiva página de forma simples, para este caso, devemos passar **o ID da página no campo "Page"** de cada opção da lista, como na imagem:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/hkkimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/hkkimage.png)

<p class="callout info">💡 Lembrando também de alterar o **"Target Type"** para **"Page in this application"**.</p>

Caso seja necessário executar um processo, ou abrir páginas de outras aplicações a partir desta opção da lista, podemos fazer de diversas formas, porém a mais "Comum" é:

- Criar um botão na página que ficará escondido (Utilizar a classe css hidden), e criar um ID para ele;
- Programar toda a lógica necessária neste botão (Execução de uma procedure, ou um redirect para uma página de outra aplicação, entre outros...);

"Forçar" o click neste botão por javascript:

```javascript
javascript:apex.event.trigger('#gera_sel', 'click');
```

O Código acima deverá ser colocado na coluna "target" de cada opção da lista, lembrando novamente de substituir os caracteres "idDoBotao" pelo ID do botão que foi criado na sua página.

Dessa forma, quando a opção for clicada, será executado esse javascript que irá clicar no botão escondido, realizando assim o processo necessário.

#### **Botões Dinâmicos de Grid**

---

- Utilize o **Plugin FOS - Interactive Grid - Add Button** para adicionar o botão à grid.
- O Action em conjunto com o código JavaScript determinam o funcionamento do botão.
- O **Action** deve ser o **Static ID** do List.
- Configure o bloco JS para chamar a seguinte função, levando em conta que o parâmetro também deve ser o **Static ID** do **List**. Ex:

```
setGridButtonAsMenuPopUp('staticIdDaLista_menu');
```

**Exemplo:**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/Lsfimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/Lsfimage.png)

#### **List Dentro de Outra List**

---

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/VOSimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/VOSimage.png)

Para criar níveis dentro do seu List, é bem simples e a seguir serão mostrados os passos para fazer isso.

**Passo 1:** Você já precisa ter o seu **List Shared Component criado.** De acordo com o print acima, será representado o mesmo exemplo, onde o menu "Manutenções" será tratado como pai e a "Pessoa RH" será tratada como filha.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/7Gwimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/7Gwimage.png)

 **Passo 2:** Crie um segundo Entry, que será o filho.

Terá uma opção chamada "Parent List Entry", nela é só selecionar qual List Entry é a pai da que você está criando no momento.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/nFBimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/nFBimage.png)

 Após salvar, já será possível ver o seu list funcionando com níveis de hierarquia. 🙂

# Separador e Habilitar/Desabilitar opções do Menu Popup

Após criar o Menu Popup é possível criar separadores e também habilitar/desabilitar as opções nativamente.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/BPJimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/BPJimage.png)

##### **Separador**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/FzEimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/FzEimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/xQpimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/xQpimage.png)

##### **Habilitar/Desabilitar**

Para controlar a disponibilidade de uma opção, utilize a propriedade **Disabled** em **User Defined Attributes**

- **Desabilitar**: defina o valor como **TRUE**
- **Habilitar**: defina o valor como **FALSE** ou deixe o campo vazio

#### **Referenciando Itens**

---

É possível referenciar outros itens da página usando a sintaxe: `&P100_SEU_ITEM.`

<p class="callout warning">**Importante:** Para que as alterações de habilitação/desabilitação tenham efeito, é necessário realizar um **Submit Page** (envio da página).</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/VvBimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/VvBimage.png)

# Modal

# Mensagem no Dialog Closed

Para casos onde precisamos mostrar para o usuário a mensagem de sucesso partir de um *Dialog Closed* é necessário **informar a mensagem dentro do** ***processes*** que esta fechando a Modal.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/Cgpimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/Cgpimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/rV0image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/rV0image.png)

<p class="callout success">**⭐Padrão:** Fique atento à escrita padrão das mensagens em alertas. Acesse: [Notificações](https://wiki.cscompusoftware.com.br/books/erp-guideline-de-uiux/page/notificacoes#bkmrk-%C2%A0boas-pr%C3%A1ticas-de-es "Boas Práticas de Escrita em Notificações")</p>

# Page as Modal

#### **Modal a partir de um Botão (Submit)**

---

Para chamar uma página normal, como modal, a partir de um botão, utilize a seguinte forma.

- Crie um **item, hidden, com o source.**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/i4jimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/i4jimage.png)

```
csweb.pkg_apex_utils.fn_page_as_modal(150, 40101);
```

Essa forma permite chamar a tela modal informando valor de itens através dos parâmetros:

- **p\_items**
- **p\_values**

**Exemplo:**

```
csweb.pkg_apex_utils.fn_page_as_modal(150, 40101, 'P150_ITEM', 'VALOR');
```

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/GV0image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/GV0image.png)

- **Crie o botão e atribua o evento** para quando o Modal for fechado/cancelado.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/BcMimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/BcMimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/lsGimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/lsGimage.png)

- Por fim, defina o comportamento do click do botão, para **"Redirect do URL"**, e utilize o valor do **Item hidden como o valor da URL.**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/qW9image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/qW9image.png)

#### **Modal a partir de um Botão (Dinâmico)**

---

Quando a página não é submetida, o item de URL **<span class="ql-badge-red">não tem</span>** **o *Source* configurado** e alimentamos ele via ***Dinamyc Action*** da seguinte forma.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/59Aimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/59Aimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/vznimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/vznimage.png)

- Executamos a chamada da página modal via "`eval()`", logo após o **"Set Value"** da URL.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/J9Kimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/J9Kimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/7uCimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/7uCimage.png)

**Tela exemplo:** [40152:400](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-controle-lavoura/fundo-agricola?session=9214413713697)

#### **Atalho para Modal de CRUD a partir de um Filtro/LOV**

---

Para casos onde a intenção é fazer um atalho para o cadastro de um determinado filtro, utilize essa forma.

- Programe a LOV/Filtro e identifique qual será a **página de CRUD**.
- Com o ID de Aplicação e Página em mãos, informe o seguinte **"Help Text" no Item do Filtro/LOV**.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/hREimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/hREimage.png)

<p class="callout info">**Observação:** Esse padrão "`crud: APP-PAGE;`" é importante para o funcionamento do atalho.</p>

##### **Resultado**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/kOAimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/kOAimage.png)

# Multi-Filtro / LOV com Botões

Quando existe um **Multi-filtro/ LOV** com um botão logo ao lado, por conta de colocarmos o botão ocupando o **col-span** em 1, ele acaba ficando um gap, pois o botão não precisaria de um espaço tão grande para ele:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/BFlimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/BFlimage.png)

#### **Como Resolver**

---

1. Ao criar o LOV, Multi-Filtro com o botão geralmente criamos também uma região container em volta deles:
2. No template dele, deixe Itens Spacing: None e também Item Width: Stretch Form Field

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/uHbimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/uHbimage.png)

- Adicione também a classe para aplicarmos o **CSS em Column CSS Classes**: `cs-custom-inline-container`

##### [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/cNMimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/cNMimage.png)

#####  

##### **No filtro de LOV/Multi-Filtro** 

- Adicionamos também outra classe para aplicar o CSS na Column CSS Classes: `cs-inline-field-filter`

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Tv3image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Tv3image.png)

##### **Finalizando o botão**

- Adicionamos também além da classe nossa, a classe de `cs-flex-end` para o botão ficar alinhado: `cs-inline-field-button `

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/0Epimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/0Epimage.png)

# Multifiltro (MultiGEF)

No nosso sistema possuímos muitos filtros que podem ser selecionados mais de uma opção para filtrarem a informação, devido a isso nossa equipe desenvolveu o componente (page item) [CS - Multifiltro \[Plug-In\].](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/cs-multifiltro-apex-cs-40 "Multifiltro")

<p class="callout info">💡 Lembrando que em **raríssimas exceções esse componente pode ser usado para uma seleção simples** devido ao tamanho que ele é exposto facilitando a leitura dos dados.</p>

Para configurarmos o Multifiltro devemos sempre estarmos muito atentos ao funcionamento do filtro no próprio ERP

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/0C5image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/0C5image.png)

Cada configuração do Item é importante e sempre é válido fazer testes para melhorar o entendimento do componente.

Por default o componente não vem apenas com o *<u>Enable option: all</u>* que serve para habilitar o *"Marcar todos"* dentro do componente e a opção *<u>Report Columns Configuration</u>* que serve para configurarmos em formato jSON como gostaríamos que fosse exibido os itens do Multifitro

<p class="callout info">💡 Caso a lista de valores seja um **Shared Components** não devemos, **é** **necessário** utilizar o <u>Report Columns Configuration.</u></p>

<p class="callout warning">Lembrar de nunca utilizar o "**Value Required**" no componente. Desde que **possa selecionar todos.**</p>

O componente se assemelha bastante a um LOV, por tanto é necessário inserir sua lista de valores.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/ZrBimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/ZrBimage.png)

<p class="callout warning">Vale ressaltar que a **lista de valores deve ser baseada na sua necessidade**, ou seja, pode ser um <u>Shared Component</u> ou até mesmo uma <u>SQL Query</u>.  
**NUNCA** marcar o <u>Display Null Value</u>, para mostrar a opção de "--TODOS", ou seja, sem filtrar devemos colocar em seu <u>Value placeholder</u> o label "--TODOS"</p>

 [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/ih0image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/ih0image.png) [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/cuMimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/cuMimage.png)

Devemos voltar as configurações do nosso componente, agora sim vamos configurar o modo de exibição dele com o jSON, devemos entrar no *<u>Report Columns Configuration</u>* e manipular da forma como gostaríamos que fosse exibido.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/fJUimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/fJUimage.png)

```
{
  "defaultSort": {
    "column": "COD_TIPOFOLHA",
    "direction": "asc"
  },
  "columns": {
    "COD_TIPOFOLHA": {
      "visible": true,
      "heading": "Código",
      "thAlign": "left",
      "tdAlign": "right",
      "sort": true,
      "filter": true,
      "width":"90px"
    }, 
    "DESCRICAO": {
      "visible": true,
      "heading": "Descrição",
      "thAlign": "left",
      "tdAlign": "left",
      "sort": true,
      "filter": true
    }
  }
}
```

Este seria um exemplo de código padrão baseado em um LOV simples:

- ***<u>defaultSort</u>*** serviria para ordenar o componente com base na coluna <u>COD\_TIPOFOLHA </u>em ordem ascendente 
    - **Tradução:** Ordenar pela coluna do código em A-Z por padrão.
- ***<u>columns</u>*** serve para exibir as colunas que deseja tratar e a maneira como quer exibir dentro da modal 
    - Tradução: É como se fosse configurar um LOV nos *Shared Components* por jSON: 
        - <span class="ql-color-orange">"visible": </span>Configuração do tipo *<u>booleana</u>* para a funcionalidade de visualizar ou não a coluna
        - <span class="ql-color-orange">"heading": </span>Configuração do tipo *<u>String</u>* do cabeçalho
        - <span class="ql-color-orange">"thAlign": </span>Alinhamento do cabeçalho (*<u>Left, right, center</u>*)
        - <span class="ql-color-orange">"tdAlign": </span>Alinhamento do campo (*<u>Left, right, center</u>*)
        - <span class="ql-color-orange">"sort":</span> Configuração do tipo *<u>booleana</u>* se é ordenável ou não
        - <span class="ql-color-orange">"filter":</span> Configuração do tipo *<u>booleana</u>* se é Filtrável ou não
        - <span class="ql-color-orange">"width":" </span>Configuração do tamanho da largura da coluna em *<u>pixel</u>*

Resultado final da modal de Tipo Folha:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/rGQimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/rGQimage.png)

---

Tela exemplo ➝ [40102:520](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-cargos-salarios/vencimento-do-curso)

#### **MultiGEF**

---

Um caso que usamos muito o multifiltro é o MultiGEF, que é o nosso multifiltro para *Grupo empresa, Empresa e Filial*; Ele serve como base para entendermos o exemplo de multifiltros que se "multifiltram", visto que as escolhas de múltiplas empresas filtram múltiplas filiais.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/dmYimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/dmYimage.png)

Essa será a estrutura normal para esses filtros, visto que Grupo empresa **nunca** será com componente multifiltro.

Como já sabemos que eles se "multifiltram", então é necessário fazer uma relação de <u>cascata</u> ("Cascading List of Values") entre eles para se filtrarem.

Para começarmos o multiGEF fazemos primeiro um LOV para o `<strong>COD_GRUPOEMPRESA</strong>`, sem nenhuma relação de cascata para ele. Utilizando o Shared Component `<strong>F_GRUPOEMPRESA</strong>`

 [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/3QXimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/3QXimage.png) [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/1P2image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/1P2image.png)

<p class="callout success">✅ Não será necessário **<u>Report Columns Configuration</u> nos filtros de Empresa e Filial** já que temos as colunas do Shared Component já configuradas no padrão.</p>

Em seguida fazemos o componente multifiltro para **COD\_EMPRESA**, que será necessário ter a primeira relação em cascata. Utilizando o Shared Component **F\_EMPRESA**

 [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/ITLimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/ITLimage.png) [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/37fimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/37fimage.png)

Onde o componente **COD\_EMPRESA** terá como Parent Item o **COD\_GRUPOEMPRESA** e a opção "Parent Required" marcada, pois é uma informação necessária para o funcionamento do filtro.

<p class="callout info">💡 Vale ressaltar que o nome dos componentes serão o da sua tela, então, atenção ao nome dos itens.</p>

Resultado final da modal de Empresa:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/FQiimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/FQiimage.png)

Agora para fazermos o último componente, que é o **COD\_FILIAL**, que recebe como *<u>Parent Itens</u>* o **COD\_GRUPOEMPRESA** e o **COD\_EMPRESA.** Utilizando o Shared Component **F\_FILIAL**.

 [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Ixhimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Ixhimage.png) [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/eJqimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/eJqimage.png)

<p class="callout info">💡 Lembrando que os Page Itens são o da sua tela, aqui está somente o exemplo para termos uma base de como fazer o componente para novas telas.</p>

Resultado final da modal de Filial:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/v7rimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/v7rimage.png)

---

Tela exemplo ➝ [40102:520](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-cargos-salarios/vencimento-do-curso)

#### **Erros**

---

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/W1Dimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/W1Dimage.png)

 É necessário dar *grant* nas tabelas à serem utilizadas.

```
grant select on juridico.proc_locais to csweb;
```

`juridico.proc_locais` será a sua tabela.

# Nomenclatura

<p class="callout warning">**EM CONSTRUÇÃO...**</p>

Sobre as práticas mais indicadas para nomear páginas, regiões, item, eventos, ações\*, processos e branches.

<table border="1" id="bkmrk-quando-case-do-dont-" style="border-collapse: collapse; width: 100%;"><colgroup><col style="width: 25.0238%;"></col><col style="width: 25.0238%;"></col><col style="width: 25.0238%;"></col><col style="width: 25.0238%;"></col></colgroup><thead><tr><td>**Quando**</td><td>**Case**</td><td>**DO**</td><td>**DONT**</td></tr></thead><tbody><tr><td>Page Alias</td><td>**Página com título:**

Aprovação de Parcelas do Contrato

</td><td>aprovacao-parcela-contrato</td><td>aprovação-de-parcela-do-contrato</td></tr><tr><td>Region Title

Static ID

</td><td>Interactive Grid de Parcelas aprovadas

Interactive Grid de Parcelas aprovadas

</td><td>ig-parcelas-aprovadas

ig-parcelas-aprovadas

</td><td>Aprovadas

ig aprovadas

ig\_aprovadas

IG\_PARCELAS

Ig Aprovadas

</td></tr><tr><td>Page Item Name</td><td>Item de Formulário cujo represente a coluna COD\_FUNCIONARIO da tabela do formulário.

Item da página de Contrato utilizado como parâmetro para filtrar as Parcelas através da coluna NUMERO\_CONTRATO.

Item de página utilizado como filtro, normalmente contendo valores como S/N.

</td><td>P10\_COD\_FUNCIONARIO

P10\_NUMERO\_CONTRATO

P10\_FILTRO\_NUMERO\_CONTRATO

P10\_SOMENTE\_ATIVOS

</td><td>P10\_FUNCIONARIO

P10\_CODFUNC

P10\_CODIGO

P10\_NRCONTRATO

P10\_FILTRO\_GRID

P10\_CHECKBOX

P10\_ATIVOS

</td></tr><tr><td>Dynamic Action</td><td></td><td></td><td></td></tr></tbody></table>

# Nova Página

# Cópia de Página

Devido a validações no ambiente de desenvolvimento, ao copiar uma página, adicione ao ***new page name*** o sufixo `[CSCOPY]`:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/aggimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/aggimage.png)

Retirando o mesmo logo após a página ser criada/copiada:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/QP6image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/QP6image.png)

# Nova Página

#### **Wizard de Criação**

---

##### **Breadcrumb**

Todo módulo já possui breadcrumb global, portanto as novas páginas devem **ser criadas sem a geração de um breadcrumb próprio** (também sem especificar navegação estática, pelo mesmo motivo).

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/image.png)

#### **Módulo**

---

Ao criar uma nova página, verifique o módulo de origem da tela correspondente no Delphi. A página deve ser criada no mesmo módulo de origem.

Para verificar o módulo de origem no Delphi, você pode abrir o arquivo DPR do projeto (`CS_xxxx.dpr`) e buscar o nome do form sem o prefixo `F_` no texto.

##### Exemplo

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/eySimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/eySimage.png)

Alternativamente, se você tiver o plugin que aprimora a busca de form (Shift+F12/Ctrl+F12), você pode ver a pasta do módulo de origem no próprio plugin:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/V3Yimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/V3Yimage.png)

#### **Alias**

---

Ao criar uma nova página revisar o Alias da mesma, para que não contenha caracteres especiais, e cada palavra deve ser separada com hífen. O Alias deve ser sucinto e único em toda a aplicação.

##### **Exemplo**

- **Page**: Atribuição de Parceiros do Usuário
- **Alias**: atribuicao-parceiros-usuario

#### **Help Text**

---

Utilizaremos o Help Text das páginas para controle interno.

Toda página que for criada para refletir à uma, ou várias, telas de Delphi nós vamos referencia-las pela chave-valor (cod\_telas) no Help Text.

##### **Exemplo**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/oI6image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/oI6image.png)

**cod\_telas** é a chave, e o valor é o código da tela do Delphi, separado por vírgula quando for mais de uma, e finalizando a chave-valor com ponto e vírgula.

<p class="callout info">💡 Caso a página seja criada nativamente no APEX sem página no legado, usa-se o <span class="ql-bg-red">**cod\_telas: 0**;</span></p>

#### **<span class="ql-bg-red">Page Tree</span>**

---

A propriedade page\_tree identifica a página de menu que serve como referência para uma página dependente.

Toda página modal ou página normal que não esteja cadastrada no menu e dependa de outra página para ser acessada deve possuir essa configuração no campo Help Text.

Para referenciar uma página da mesma aplicação: **`page_tree: PAGE_ID;`**

**Exemplo:**

- Estando as páginas na mesma aplicação, na página 21, que é um formulário modal/página normal dependente da página 20, eu aponto a página 20 como base da árvore. ![page_tree_img.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-07/scaled-1680-/page-tree-img.png)
- Para referenciar uma página de outra aplicação: **`page_tree: APP_ID-PAGE_ID;`**
    
    **Exemplo: `page_tree: 40010-20;`**.

#### **<span class="ql-bg-red">Numeração das Páginas</span>**

---

Para manter várias páginas de uma mesma "tela" agrupadas juntas decidimos por reservar números de página em incrementos de 10 ou mais.

**Por exemplo:**

- **Página de cadastro 1** = página 10, não possui nenhum modal mas as páginas 11 a 19 não serão usadas para novas páginas
- **Página de processo 2** = página 20, possui 3 modais nas páginas 21, 22 e 23. 24 a 29 não serão usadas para novas páginas.

#### **Páginas Públicas** 

---

Quando a página for desenvolvida com intuito de ser uma página que não exige direito de acesso.

**Por exemplo:**

Dashboard de um módulo, página de mensagens, modais de Ativa Parâmetro, então usamos o seguinte Help Text:

```
pagina_publica: S;
```

# Novo Módulo

Cada módulo do CS será uma aplicação e todas as aplicações derivam do mesmo *template* (**40001 CS-TEMPLATE**).

Para criar um novo módulo, faça uma cópia do *template*, e atualize os dados básicos da aplicação.

Clique em *Create*, em seguida em ***Copy Application***

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Vdtimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Vdtimage.png)

Ou, acesse o *Template* e clique em ***Copy this Application***

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/fKaimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/fKaimage.png)

**A numeração (*Application ID*) segue a seguinte formatação:**

Para uma nova Gestão acrescentamos 50 (cinquenta) **unidades** ao ultimo APP 40000 existente ( *40050* \[TRIBUTÁRIA\], *40100 \[RH\] etc)* , sendo que, para cada Módulo 1 (uma) **unidade** diferente iniciando sempre pelo 01 ( *40101 - CS Recrutamento e Seleção, 40102 - CS Cargos e Salários).*

<p class="callout warning">**Reforçando:** **Nunca** existirá módulos com final "0" (Zero), pois, o "0" (Zero) representa a **GESTÃO**. Todo módulo, obrigatoriamente, sempre terá início a partir do numeral 1 (um).</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/KYgimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/KYgimage.png)

<p class="callout info">💡 Ao efetuar a copia, o processo pode <span class="ql-bg-red">demorar um pouco</span>, retornando **PROXY ERROR***,* pois, o navegador entende que a aplicação parou de responder, porém, o processo esta sendo executado em *backgroud* normalmente, então, após o erro, basta esperar alguns minutos e o novo APP <span class="ql-bg-green">aparecerá normalmente à lista de APP's.</span></p>

Após a cópia, revisar detalhes/nomes nas propriedades da aplicação.

**App** &gt; **Edit Application Definition.**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/sp5image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/sp5image.png)

<span class="ql-bg-green">Sempre altere o Nome e o Alias para os do módulo correspondente.</span>

<p class="callout info"><span class="ql-bg-green">💡 O ***Name* sempre terá o NOME <u>inteligível por extenso</u> do módulo**, começando por CS. **Exemplo:** CS Operações Financeiras. Já o Alias por ser o que aparecerá na **URL terá o nome todo <u>EM MAIUSCULO</u>** separado por "-" e **SEM** caracteres especiais. **Exemplo:** CS-OPERACOES-FINANCEIRAS.</span></p>

#### **Informar o Grupo da Aplicação**

---

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/muNimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/muNimage.png)

Caso seja necessário criar um novo Grupo de Aplicação ( o que corresponde a `Gestão `no legado) basta acessar: **App Builder &gt; Wokspace Utilities &gt; Application Groups.**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/rSUimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/rSUimage.png)

Sempre altere a <span class="ql-bg-yellow">string de substituição</span> **APP\_NAME** do módulo correspondente para o NOME <u>inteligível por extenso</u> do módulo, começando por CS , Ex.: CS Operações Financeiras.

**SEMPRE** alterar o `OWNER` do *Parsing Schema* para o OWNER do módulo Correspondente.

**APP &gt; Shared Components &gt; Security Attributes &gt; Database Session.**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/QAgimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/QAgimage.png)

<p class="callout warning"><span class="ql-bg-red">Rara</span> serão as vezes que o `OWNER` CSWEB **permanecerá como** ***Parsing Schema**,* o mais comum será o uso dos owners da gestão Ex.: RH, FINANCEIRO, AUTOMOTIVO, GERAL, SEGURANCANOVO e etc.</p>

<p class="callout info">💡 Obs.: Caso o `OWNER` não seja listado, verifique como solucionar em [Owner no APEX](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/owner-apex).</p>

#### **Informar o Código da Gestão/Módulo Correspondente**

---

APP &gt; Shared Components &gt; Application Computations

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/XPlimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/XPlimage.png)

Selecione as *computations* para G\_COD\_GESTAO e G\_COD\_MODULO e em ***Computation* &gt; *Computation*** defina o valor que corresponde ao número da gestão e módulo, respectivamente, que correspondem ao módulo na versão desktop.

<p class="callout warning">**Atenção:** <span class="ql-bg-red">NUNCA</span> usar a formatação de duas casas com "0" (Zero) a esquerda no início dos códigos de Gestão e Módulo (Ex.: **01** <span class="ql-bg-orange">&lt;- Isso é errado</span>), sempre encare essa configuração como um "Número Inteiro" e use sem zero a esquerda (Ex.: **1** <span class="ql-bg-green">&lt;- Isso é Correto</span>). Esse cuidado é necessário, pois, isso pode provocar erros no tratamento desse dado posteriormente.</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/h8Iimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/h8Iimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/MdIimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/MdIimage.png)

Você pode verificar o código da gestão e módulo através do Menu Principal CS.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/qfDimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/qfDimage.png)

#### **Ajustar Página 01 - Home**

---

APP &gt; página 1: Home

Alterar o Título da página 1 para o nome do módulo correspondente.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/hesimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/hesimage.png)

<p class="callout success">**✅ SEMPRE** mantenha o Name / Alias como home.</p>

#### **Controle de Acesso do Módulo**

---

Sempre que criar um novo módulo lembre de configurar seu [Controle de Acesso](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/controle-de-acesso "Controle de Acesso"), além de cadastrar este novo módulo no menu da aplicação 40010, para que apareça na página inicial do usuário.

# Objeto de Custo

A tela de Objeto de Custo é uma página "**Global**", assim como no legado, e para usar ela, basta fazer a chamada, sem necessidade de recriar ou programar a mesma.

A página pode ser usada com seleção **SIMPLES** ou com **MULTI** seleção, a depender do parâmetro "`P10_TIPO`" informado na chamada da página.

<p class="callout success">✅ Página padrão: **40010:10** - **Objeto de Custo** (Componente utilizado - [Fancy Tree](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/apex-fancy-tree "Fancy Tree Plug-in")</p>

Usaremos como exemplo o filtro de objeto de custo da página **40201:500**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/o3Bimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/o3Bimage.png)

- Onde temos um **Multifiltro** de **Objeto de Custo**, acompanhado de um botão para a chamada do **TreeView** de **Objeto de Custo.**
- O Botão que chama a página do **Objeto de Custo** deve ter e seguinte configuração no "**Behavior**", redirecionando para uma página em outra aplicação, no caso a **página 10 da** **Aplicação 40010**:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/PgFimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/PgFimage.png)

Nesse caso usaremos a **Seleção SIMPLES**, portanto, passamos por parâmetro para o item "`P10_TIPO`" a palavra **SIMPLES** (em caso de seleção múltipla usaríamos a palavra **MULTI**).

#### **Seleção Simples**

---

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/eWpimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/eWpimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/SFNimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/SFNimage.png)

#### **Seleção Múltipla**

---

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/ubwimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/ubwimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/x05image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/x05image.png)

- Logo após, criamos uma **D.A** nesse botão, sendo o evento ***Dialog Close*****:**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/tMlimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/tMlimage.png)

- E adicionamos a ela uma***True Action*** de ***Set Value*** do tipo ***Dialog Return** Item* onde esperaremos o retorno no item **P10\_COD\_OBJETOCUSTO** que é o item que será populado na tela de <u>Objeto de Custo com o Código do Objeto de Custo</u> selecionado. E em **Affected Elements**, indicamos o item que representa nosso **Filtro/Multifiltro** na página atual (Ou seja, esse processo é o responsável em fazer o "**De - Para**" entre a página de Objeto de Custo e a página atual. Entenda um pouco mais em Private: **Retorno de Item de Página Modal (link)**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/0uRimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/0uRimage.png)

- Em caso de **Seleção Múltipla**, opte pelo item de retorno **"**`P10_ATIVIDADE`"

##### **Para atender situações específicas, a página já conta com diversos outros itens de retorno:**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/oiFimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/oiFimage.png)

Que podem ser usados de acordo com a necessidade.

Em algumas telas, a regra de negócio da exibição dos objetos de custos podem diferir, com isso, novos parâmetros precisam ser criados na função (**CUSTO.FN\_LISTA\_ARVORE\_OBJCUSTO\_APEX**) e a tela de objeto de custo precisa ser atualizada, criando novos itens de páginas quando necessário.

Dois novos parâmetros foram criados:

- `P10_FILTRA_MAT_RECONDICIONADO` - Responsável trazer os objetos de custos que fazem parte do recondicionamento de material.
- `P10_EXIBE_INATIVO` - Responsável por definir se os objetos de custos inativos devem ou não ser exibidos.

---

**Página de exemplo:** [40201:500](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-acao/adequacao-restritos)

# Objetos

# Objetos

Em algumas telas necessitamos criar objetos, como [Packages](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/packages "Packages"), [Triggers](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/triggers "Triggers") e View para Item ou Página.

Para isso a **CS possui alguns padrões.**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Cepimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Cepimage.png)

Para criarmos um objeto devemos abrir o "Controle de Versão do Oracle" no **.exe**

Logo que abrir já estaremos na parte de **Criar Objeto.**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/HuPimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/HuPimage.png)

Agora devemos seguir de acordo com o objetivo da criação.

<p class="callout info">💡 Dentro das **Packages** criaremos as ***functions e procedures***, não sendo assim necessário criar esses objetos pelo controle de versão.</p>

# Packages

Vale ressaltar que sempre antes de criar uma **Package** seja de bom costume verificar se já não existe uma **Package** que contemple o mesmo motivo.

Em algumas telas necessitamos criar uma **Package** para armazenar as *procedures* e *functions* que precisamos para o funcionamento pleno da tela em conjunto com o módulo, para isso a CS possui alguns padrões.

Para criarmos uma **Package** primeiro criamos a **Package** em si e depois a **Package Body.**

##### Por que? Porque não funciona.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Jvoimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Jvoimage.png)

<p class="callout success">**✅ Criar Body** deve estar desmarcado, se não ocorre erro na criação.</p>

O **Owner** será do módulo que você está fazendo as alterações.

Por padrão como estamos criando para o **APEX**, devemos colocar seu nome como *PKG\_APEX\_('motivo')*.

No **Id Estória** devemos colocar o o módulo referente ao módulo que estamos trabalhando

No **Id Imped** deixamos vazio mesmo

Colocamos uma **Descrição** do que ela fará, como o que armazenará e o módulo que ela estará agrupando os outros objetos.

Em suas **Tag's** sempre é importante colocar *<u>APEX</u>* e o *<u>MOTIVO</u>*, para ser mais fácil sua busca e orientação.

Depois de criar a **Package** faremos o **Package Body** que consiste em selecionar o mesmo *owner* de sua **package** e depois selecionar a **package** que você acabou de criar, depois seu <u>Id Estória</u>, <u>descrição</u> e suas <u>Tag's</u> mantém o mesmo padrão.

# Triggers

Para a criação de Triggers o super **Dev Tools** já possui um script de como faremos a criação dele.

<p class="callout warning">Verifique se **já não existe uma trigger** para a tabela em questão.</p>

Qualquer dúvida chame algum desenvolvedor para auxilia-lo <span class="cu-emoticon cu-emoticon_static" data-emoticon="{"code":"1f9d1-200d-1f4bb","name":"Technologist"}">🧑‍💻</span>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/I7cimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/I7cimage.png)

[https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-dev-tools/home](https://csweb00.cscompusoftware.com.br/csdesenv/r/csords/cs-dev-tools/home)

Assim que entrarmos na página já poderemos ver a informação de **Owner** que devemos colocar o do módulo de onde a tabela que faremos a Trigger está.

Na Tabela colocaremos a devida **Tabela** da validação.

Depois devemos selecionar se a o momento do disparo da Trigger será no **Antes(Before)** ou **Depois(After)** da ação.

Depois está pronto o script para compilarmos no PL e prontinho, sua Trigger está criada <span class="cu-emoticon cu-emoticon_static" data-emoticon="{"code":"1f609","name":"Winking Face"}">😉</span>

# Owner APEX

Em alguma situações o *OWNER* não é listado para ser associar a uma aplicação ou mesmo quando referenciado em uma *Query*, não é encontrado.

Temos então 2 possibilidades:

#### **Grant**

---

Devemos assegurar que o *OWNER* esteja vinculado as seguintes *ROLES*:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/0qQimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/0qQimage.png)

#### **Configuração do *Workspace***

---

A visibilidade do "***parsing schemas***" no APEX pode ser controlado no *workspace*. Então, é possível que *OWNER* não esteja vinculado ao *workspace*.

Nas 2 situações, basta entrar em contato com o INFRA e solicitar os ajustes, que são:

- A equiparação das roles;
- O vínculo / associação do OWNER ao *workspace.*

# Page Groups Coloridos

Nesse guia, será mostrado como fazer com que um Page Group criado no APEX possua cor.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/ZMqimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/ZMqimage.png)

Note que o grupo "Info Bem" está com um tom levemente amarelado. E como isso é feito?

**Passo 1** ➝ Vá na aba principal de sua página.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/HZsimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/HZsimage.png)

**Passo 2** ➝ No menu lateral direito, ir na parte de JavaScript.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/chCimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/chCimage.png)

**Passo 2.1** ➝ em Execute When Page Loads, é onde você executará o seu código.

```
$('.infoBem').parent().parent().css({ "background-color": "#FFF9F2", "color": "black" });
```

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Ggjimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Ggjimage.png)

**Passo 2.2** ➝ Crie um Page Group na Interactive Grid desejada, com o nome dela sendo um `<span></span>` possuindo a classe declarada no código anterior.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/3Ziimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/3Ziimage.png)

Pronto! Agora é só utilizar o Page Group nas colunas desejadas.

<p class="callout warning">Ao escolher as cores para o seu page group leve em consideração a legibilidade do texto em preto. **Evite cores muito fortes ou escuras.** Em caso de dúvida sempre c**ontato o UI/UX ou acesse o guideline sobre [cores](https://wiki.cscompusoftware.com.br/books/erp-guideline-de-uiux/page/cores "Guideline sobre cores").**</p>

# Página "Dados do Funcionário"

Em algumas telas, ao filtrar um funcionário, são exibidas nas telas algumas informações sobre o funcionário filtrado, como seu cargo, departamento, data de admissão, entre outros. No apex, essas "informações adicionais" ocupam muito espaço útil da tela, e por isso, foi criada uma **página modal que exibirá as principais informações do Funcionário filtrado**.

A página pode ser encontrada no módulo Recrutamento e Seleção, com **ID 810 (40101:810).**

Ela espera como parâmetro os campos: `cod_funcionario`, `periodo` e `cod_grupoempresa` (Caso este parâmetro não seja passado, a tela utilizará como default o valor global do `grupoempresa`).

<p class="callout info">Em alguns momentos utilizamos essas informações concatenadas, porém **essa tela recebe cada valor único e sozinho.**</p>

Existem **duas situações comuns** para se chamar essa tela:

1. A primeira é quando estamos **navegando em uma grid**, e conforme selecionamos um funcionário diferente, suas informações vão sendo atualizadas em algum lugar na tela.
2. Já a outra é logo após que utilizamos um **filtro de funcionário**, algumas informações são atualizadas em algum edit na tela do delphi.

#### **Grid**

---

Para a primeira situação, na coluna do nome do funcionário, iremos **criar um link que abrirá a modal** de dados do funcionário (Concatenar o ícone **"*fa-user"* com o nome do funcionário**), como na imagem:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/v75image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/v75image.png)

#### **Filtro**

---

Quando tiver a segunda situação, utilizaremos um **botão ao lado do filtro de funcionário**, sendo este botão responsável por abrir a modal de dados do funcionário. O visual do Botão será como na imagem:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/ogjimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/ogjimage.png)

#### **Resultado Esperado**

---

Por fim, a modal deverá aparecer da seguinte maneira:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Yl9image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Yl9image.png)

# Plug-ins

# APEX Fancy Tree

Em algumas telas do sistema precisaremos utilizar fazer uma **Tree View**, e para isso temos o *Plug-in* do tipo Region chamado **APEX Fancy Tree.**

<p class="callout success">**⭐ Por que não usar a Tree do próprio APEX?**   
Porque o plug-in vem com alguns detalhes configurados automaticamente, **sendo muito mais prático seu uso.**</p>

Quando criamos o componente ele vem com uma SQL de orientação, cada item representa:

- <span class="ql-bg-red">**ID - Obrigatório:** </span>É o ID de cada registro, Normalmente será a PK de sua tabela.

- <span class="ql-bg-red">**PARENT\_ID - Obrigatório:** </span>É o ID do pai do registro, exemplo no Objeto de custo: "objetocusto.objeto\_pai".

- <span class="ql-bg-red">**TITLE - Obrigatório:** </span>Será a descrição de cada registro.

- <span class="ql-bg-yellow">V**ALUE - Quando usar o SELECTED:** </span>É o valor do item que está sendo passado.

- <span class="ql-bg-yellow">**TYPE - Quando usar o SELECTED:** </span>É configurado no JSON, serve para mapear a "altura" que ele seria

- **TOLLTIP:** O que aparecerá quando posicionarmos o mouse nos itens

- **ICON:** O ícone que aparecerá antes do TITLE do item

- **SELECTED:** 1 para o registro carregar selecionado ou 0/null para o registro carregar selecionado

- **EXPANDED:** 1 para o registro aparecer expandido e 0/null para o registro aparecer fechado

- **CHECKBOX:** 1 para registro com checkbox e 0/null para item sem checkbox

- **UNSELECTABLE:** 1 para o registro não poder ser selecionado e 0/null para que seja possível selecionar o registro

Depois na aba de **Attributes** alteraremos**:**

No JSON alteraremos:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/lQnimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/lQnimage.png)

Para aparecer a setinha nos registros que possuem registros filhos dentro deles.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Agcimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Agcimage.png)

Na parte do *`typeSettings`* podemos remover o `<em>storeItem</em>` do JSON e alterar os ícones para ficar mais agradável a tela.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/pBmimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/pBmimage.png)

No **Search Item** colocaremos um Page Item que servirá como filtro.

No **Active Node ID** colocaremos um Page Item que servirá para receber o *<u>value</u>* do registro selecionado.

Depois devemos revisar as mensagens do **When Error ocurred** e também no **When No Data Found** para ter mais contexto com os dados.

#### **Refresh no Click**

---

Caso seja necessário usar a *Tree view* como se fosse um filtro de um grid, deveremos criar uma Dynamic Action com o evento *onClick.*

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Dkjimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Dkjimage.png)

Colocaremos no Refresh a grid que será filtrada de acordo com o click na Tree view.

Colocaremos no **Advanced** do evento o *escopo dinâmico* e seu **jQuery Selector** como **body.**

<p class="callout info">**💡** Isso serve para que quando for clicado **qualquer parte da região da Tree view reconheça o evento.**</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/d8Mimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/d8Mimage.png)

# CS Multifiltro - APEX CS 4.0

#### **Exact Match no CS - Multifiltro** 

---

**Desenvolvimento de nova funcionalidade no** `<strong>cs-multifiltro</strong>`**: Exact Match**

Foi desenvolvida uma nova funcionalidade chamada *Exact Match* para o `cs-multifiltro`. Essa melhoria permite o vínculo de um campo de input que, ao receber a digitação de um código, realiza automaticamente uma consulta no banco de dados. A funcionalidade injeta uma condição específica na query, retornando de forma imediata o valor correspondente ao código informado.

##### **Vantagens**

- Filtro mais direto e performático.
- Retorno mais rápido do registro específico.
- Ideal para pesquisa direta por chave/código.

##### **Quando Utilizar**

**Recomendações de uso do Exact Match**

Recomenda-se o uso do ***Exact Match*** em telas de **alto fluxo**, nas quais o usuário precisa digitar códigos de forma rápida e frequente.  
Também é ideal para casos em que a consulta **SQL** do` multifiltro` é complexa ou pesada, pois reduz a carga de processamento ao retornar apenas o dado exato solicitado, otimizando o desempenho da aplicação.

##### **Como Configurar o Exact Match**

##### 1. Ativar a Funcionalidade

No componente **CS - Multifiltro**, acesse as configurações do item e:

- ✅ Marque o **checkbox Exact Match** (em **General Settings**).
- 🏷️ Em **Column to match**, informe o nome da coluna da tabela a ser filtrada. **Exemplo:** `'material.cod_material'`).
- 🆔 Em **Exact Match Item**, selecione o item da página que receberá o valor do código. **Exemplo:** `'P1_COD_MATERIAL'`

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Qymimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Qymimage.png)

##### 2. Ajustar a SQL da Fonte de Dados

No SQL da fonte de dados (consulta base), adicione o seguinte comentário especial no ponto onde deseja que o filtro seja inserido:

```
 --@!MATCH_EXPRESSION!@
```

- Esse marcador será substituído dinamicamente pelo filtro exato, com base no valor informado no item de código conforme exemplos abaixo:

Para quando houver cláusula **WHERE** no seu código:

```
 select material.cod_material||' - '||material.descricao d
     , material.cod_material r
from   material.material material
where ...
        --@!MATCH_EXPRESSION!@
and   ...
```

Para quando <span style="color: rgb(224, 62, 45);">**NÃO**</span> houver cláusula **WHERE** no seu código, <span style="color: rgb(5, 106, 200);">**a expressão será diferente:**</span>

```
select material.cod_material||' - '||material.descricao d
     , material.cod_material r
from   material.material material
--@!WHERE_MATCH_EXPRESSION!@
```

Para finalizar a configuração no `CS - Multifiltro`, adicione seu item que terá o valor do Código **Exact** Match no *PARENT ITEMS* do `<em>CS - Multifiltro</em>`.

#### **Resultado Esperado**

---

Ao preencher o item de código (como `'P1_COD_MATERIAL'`), o componente `CS<strong> -</strong> Multifiltro` aplicará automaticamente o filtro com `'AND <coluna> = <valor>'`, tornando a consulta mais rápida e assertiva, retornando diretamente o item desejado.

Os objetos para funcionamento do CS - Multifiltro estão disponíveis para visualização em: `csweb.pkg_multifiltro_apex`

#### **Importante** 

---

<p class="callout warning">Ao criar o item auxiliar para o Multifiltro **diminua o nome dele para menos de 30 caracteres**. Pois passando disso ele pode **causar erro no processamento** do plug-in. </p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/efDimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/efDimage.png)

<p class="callout info">**<span class="text-big">Diretório Multifiltro &gt; MULTIFILTRO (MULTIGEF)</span>**</p>

# Format Mask

<p class="callout success">**✅** Para controle de máscara de **formatação de inputs utilizamos a biblioteca [jQuery Mask](https://igorescobar.github.io/jQuery-Mask-Plugin).**</p>

#### **Como Utilizar**

---

##### **Método mais indicado pra Coluna de Grid**

Para configurar a mascara estática informe o **data-mask** na propriedade do **Advanced &gt;** **Custom Attributes** do input/coluna.

```css
data-mask="00.000-000"
```

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/JQwimage.png)Figura 01 - Exemplo de CEP](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/JQwimage.png)

Para configurar a mascara no input de forma dinâmica/condicional, utilize o método "mask" a partir do selector do input em uma chamada JavaScript.

```javascript
let formatMask = $('P00_TIPO_PESSOA') == 'F' ? '000.000.000-00' : 'AA.AAA.AAA/AAAA-00';
$('#P00_CPF_CNPJ').mask(formatMask);
```

O código pode ser declarado no Page Load, ou em uma Dynamic Action.

**Exemplo:**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-06/scaled-1680-/Qo7image.png)Figura 02 - Exemplo de CPF e CNPJ](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-06/Qo7image.png)

Para mais configurações utilize a [documentação](https://igorescobar.github.io/jQuery-Mask-Plugin/docs.html "jQuery-Mask-Plugin").

# Nested Master Detail

Em algumas telas do legado para uma melhor visualização das famílias por registros temos o *Master Detail de Grids*. Utilizaremos na verdade um *Plug-in* que está dentro de uma **Ação dinâmica** para a visualização dos itens por **Master Detail Nested**.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/QhYimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/QhYimage.png)

Para fazermos isso temos que criar um **Interactive Report**. Para configurarmos ele parecido com uma Interactive Grid colocaremos um CSS Inline.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/cs3image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/cs3image.png)

```
.a-IRR-headerLink {
    text-decoration: none;
    cursor: default;
    color: black;
}
```

Depois de colocarmos e alinharmos a SQL para trazer os dados da maneira que gostaríamos adicionaremos uma coluna do tipo Link

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/RtKimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/RtKimage.png)

Deixaremos o Target como URL e colocaremos como "#"

<p class="callout info">💡 Lembrando que para o Interactive report o ideal seria **habilitar o "save public report"** e depois de deixar um padrão desabilitá-lo.</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Wfpimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Wfpimage.png)

Link Text:

```
<span class="PROCESSO hidden">#PROCESSO#</span><span class="fa fa-plus"></span>
```

Link Attributes:

```
class="detail_subprocesso"
```

<p class="callout info">💡 Lembrando que está com a **classe PROCESSO** porque é o que está como "pai" da tree view.</p>

Agora para darmos seguimento a criação da *Master Detail* criaremos uma **Dynamic Action** com evento **Click** e depois uma ação **Pretius APEX Nested Reports \[Plug-In\]**.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/dnEimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/dnEimage.png)

<p class="callout success">✅ Dê preferência por **nomes que identifiquem a ação** de detail.</p>

Colocaremos o <u>Selection Type</u> como <u>JQuery Selector</u> e a classe que foi passada no <u>Link Attributes</u> do *Link*.

<p class="callout info">💡 Lembrar que chamada de classe precisamos do "**.**" antes da classe.</p>

Em **Advanced** colocaremos o escopo como <u>dynamic</u> e o **Static Container** 'body'

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/MEvimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/MEvimage.png)

Dentro da ação colocaremos a Query da "filha", já ajustada conforme os dados que queremos mostrar.

<p class="callout success">✅ **Por que fazer isso?** Porque dentro desse report não conseguimos configurar seu heading e outros dados.</p>

Exemplo:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/1Dpimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/1Dpimage.png)

<p class="callout info">💡 Lembrar de colocar **Strech report** para se adequar a tela e as colunas com o devido tamanho.</p>

```
select '<a href="javascript:void(0)" class="detail_atividade"><span class="SUBPROCESSO hidden">'||vObc.subprocesso||'</span><span class="PROCESSO hidden">'||vObc.Processo||'</span><span class="fa fa-plus"></span></a>' as "<span></span>"
     , vObc.SubProcesso         as "Subprocesso"
     , vObc.Descricao           as "Descrição"
     , vObc.Cod_UnidadeProducao as "Unidade de<br/> Produção"
from   Planejamento.viewObCusto vObc
where  vObc.Negocio     = :P70_NEGOCIO
and    vObc.Processo    = #PROCESSO#
and    vObc.SubProcesso > 0
and    vObc.Atividade   = 0
order  by vObc.Negocio, vObc.Processo, vObc.SubProcesso, vObc.Atividade
```

Nesse exemplo temos outra Master Detail, por isso mais um link, vale ressaltar que deve ser visto de acordo com a necessidade de sua tela. A SQL não ficará como válida devido ao valor que está sendo passado pela "##", mas ela é lida quando salvamos o Page designer.

No ***Affected Elements*** colocaremos o **Interactive report** que foi construído na tela

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Ta3image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Ta3image.png)

E ta pronto a sua **Master Detail Nested** <span class="cu-emoticon cu-emoticon_static" data-emoticon="{"code":"1f37b","name":"Clinking Beer Mugs"}">🍻</span>

---

<span class="cu-emoticon cu-emoticon_static" data-emoticon="{"code":"1f37b","name":"Clinking Beer Mugs"}">**Tela exemplo** ➝ 40352:70</span>

# Plug-ins

<p class="callout warning">**ATENÇÃO:** A Instalação de novos plugins deve ser **analisada previamente** para evitarmos futuros i**mpedimentos de atualização do APEX.**</p>

#### **Sem acesso a um plug-in que já temos no APEX?** 

---

Para resolver isso é simples, basta adicionarmos o **Plug-ins** ao módulo que usaremos trazendo ele do **40000 - SCAFFOLD**

<p class="callout info">**💡 Por que fazer a chamada do SCAFFOLD?**   
Para que quando for feita uma atualização no Plug-in por herança ele também receba a atualização.</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/DDnimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/DDnimage.png)

Vamos no ***Shared Components*** de sua aplicação e vamos na sessão **Other Components ➝ Plug-ins.**

<p class="callout warning">Verifique se na lista **já não esta adicionado** o plug-in **que deseja usar.**</p>

#### **Criação de Plug-in**

---

Criaremos o **Plug-in no *<u>Create</u>***

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/oa7image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/oa7image.png)

Colocaremos como **As a Copy of an Existing Plug-in**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/c5Bimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/c5Bimage.png)

Copiaremos da **40000 CS-SCAFFOLD**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/c3Eimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/c3Eimage.png)

A opção do **Copy** marcaremos como *<u>Copy and Subscribe</u>*.

<p class="callout info">💡 Isso serve para que o plug-in **receba atualizações quando for atualizado no SCAFFOLD.**</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/NEOimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/NEOimage.png)

Caso não queira copiar um ***Plug-in*** marque como **<u>No</u>** no **<u>Copy?</u>**

**E pronto, agora ele aparecerá em sua aplicação!**

# Posição dos Botões (Salvar e Excluir)

Para não deixar os usuários confusos com as posições dos botões (em uma modal), iremos padronizar da seguinte forma:

[![Modal.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/hnWmodal.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/hnWmodal.png)

- Botão excluir na position ***Delete***
- Botão salvar na position ***Next***

Crie uma region *Buttons Container* no *Dialog Footer* com os botões

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/O2qimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/O2qimage.png)

---

**Tela exemplo** ➝ 40103:392

# pr_multifiltro

\[ ===== BUILDING ===== \]

Em algumas telas do sistema em delphi possuímos o componente **csmultifiltro** e ao invés de como normalmente apenas filtrar uma consulta ele pode participar de um procedimento. Quando ocorre esse caso normalmente a solução vista no sistema é popular a tabela *temporária* `geral.csmultifiltro` e dentro da *procedure/function* que eles já utilizam eles fazem a busca diretamente na *tmp*. Para contornarmos a situação e não precisarmos sempre abrir um cursor do item e fazermos o mesmo processo diversas vezes poluindo o código usaremos a procedure:

```
csweb.pkg_apex_utils.pr_multifiltro( ps_valor           => :ps_valor
                                   , pn_pagina          => :pn_pagina
                                   , ps_nomeitem        => :ps_nomeitem
                                   , pv_manter_nomeitem => :pv_manter_nomeitem);
```

Para compreender melhor a estrutura:

- `ps_valor` ➝ será o retorno do input multifiltro do page item no APEX.   
    **Exemplo:** `pn_valor`
- `pn_pagina` ➝ será a sua página do APEX  
    Será passado fixo. **Exemplo:** '570'
- `ps_nomeitem` ➝ será o nome do componente no Delphi  
    **Exemplo:** '' /\* Colocar amanhã o nome corretamente abrindo no projeto \*/
- `pv_manter_nomeitem` ➝ caso o nome seja passado FIXO na procedure/function do legado deve ser utilizado.

<p class="callout info">💡 Por default vem como 'N', entretato é importante ressaltar que caso o nome do componente seja usado dentro do procedimento do legado devemos passar como 'S' para mantermos o nome dele intacto.  
</p>

Dentro da chamada dessa procedure ele já limpará a `geral.csmultifiltro` e populará com os itens para que a procedure do legado consiga realizar os procedimentos.

Assim não sendo necessário sequer criar um cursor para pegar os registros do item, apenas a chamada da procedure já solucionaria a devida demanda.

<p class="callout warning">Lembrando que você ainda precisará entender a estrutura do código para utilizar de maneira correta, como inserir as condições no código. Dessa maneira que está sendo passado a procedure sempre irá receber como se fosse multifiltrada, fazemos assim no APEX porque usamos o componente de multifiltro e assim ele sempre identificará como se fosse mais de apenas 1 selecionado.</p>

Alguns pontos **IMPORTANTES** e adicionais sobre *Delete* da `pr_multifiltro`:

Em momentos específicos, pode ser que seja necessário executar um *delete* na *TMP* `geral.csmultifiltro` ou `geral.tmp_selecionagef`*.*

Quando chegar essa situação, <span style="color: rgb(224, 62, 45);">**NÃO execute um Delete na mão**. </span>

Antes de chamar as procedures de multi-filtro ou de multi-gef, chame as seguintes procedures, de acordo com sua necessidade:

```
csweb.pkg_apex_utils.pr_limpar_multifiltro;    csweb.pkg_apex_utils.pr_limpar_multigef;
```

Essas procedures executarão um delete na tabela de multifiltro ou de multigef. Lembrando que o uso desse recurso será somente em situações bem específicas e previamente analisadas.

---

**Package exemplo** ➝ `rh.pkg_apex_turnover_pessoas`

# Relatórios - Print Server

# Agrupamento Dinâmico

Para as opções de agrupamento dinâmico usaremos o componente **"Shuttle"** com o **"List of Values"** do tipo **"Function Body returning SQL Query".**

#### **Agrupamento**

---

Na opção de agrupamento basta usar a função `fn_agrupamento`, informando todas opções de agrupamento com os valores separados por **":"** como no exemplo:

Nas opções de aparência, adicionar a classe CSS `cs-shuttle-agrupamento` e definir a margem direita com *Large*, como no exemplo:

```
return csweb.pkg_apex_relatorio.fn_agrupamento(pc_itens => 'Negócio:Processo:Sub-Processo:Atividade:Tipo Cobrança:Equipe');
```

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/SQpimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/SQpimage.png)

#### **Totalizador**

---

O totalizador é diretamente dependente do agrupamento, pois só podemos totalizar pelas opções agrupadas, logo basta referenciar a função `fn_totalizador` informando como parâmetro o componente de agrupamento:

```
return csweb.pkg_apex_relatorio.fn_totalizador(pc_itens => :P550_AGRUPAMENTO);
```

Nas opções de aparência, adicionar a classe CSS `cs-shuttle-agrupamento` e definir a margem direita com *Large*, como no exemplo:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Y5himage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Y5himage.png)

e referenciar o componente de agrupamento no **"*Cascading List of Values*"** , como **"*Parent Item*"** e **"*Item to Submit*"**:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/6nnimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/6nnimage.png)

#### **Ordenação**

---

A ordenação também é diretamente dependente do agrupamento, pois **<span class="ql-bg-red">NÃO </span>podemos ordenar pelas opções agrupadas**, logo basta referenciar a função `fn_ordenacao` informando como parâmetro o componente de agrupamento e as opções de agrupamento como **"Item Extra"**, separados por **":"**

```
return csweb.pkg_apex_relatorio.fn_ordenacao( pc_itens_agrupamento => :P550_AGRUPAMENTO
                                               , pc_itens_extras      => 'Negócio:Processo:Sub-Processo:Atividade:Tipo Cobrança:Equipe:Número:Nr. Documento:Código do Empenho:Descrição Empenho:Código do Fornecedor:Nome Fornecedor:Data Entrada:Data Vencimento:Data Pagamento');
```

Nas opções de aparência, adicionar a classe CSS `cs-shuttle-agrupamento` e **<span class="ql-badge-red">NÃO definir a margem direita</span>**, como no exemplo:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/7WYimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/7WYimage.png)

e referenciar o componente de agrupamento no **"*Cascading List of Values*** , como **"*Parent Item*"** e "***Item to Submit*"**:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/cZkimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/cZkimage.png)

<p class="callout info">💡 Lembrar de **<span class="ql-badge-red">desativar </span>o** **"Parent Required"** pois a ordenação **deve aparecer mesmo sem opção de agrupamento** selecionado.</p>

#### **Quebra de Página**

---

Para a quebra de página, usaremos o componente **"Select List"** com o **"List of Values"** do tipo **"Function Body returning SQL Query".**

A quebra de página é diretamente dependente do agrupamento, pois só podemos quebrar as páginas pelas opções agrupadas, logo basta referenciar a função `fn_quebra_pagina` informando como parâmetro o componente de agrupamento:

```
return csweb.pkg_apex_relatorio.fn_quebra_pagina(pc_itens => :P550_AGRUPAMENTO);
```

e referenciar o componente de agrupamento no **"*Cascading List of Values*"** , como **"*Parent Item*"** e **"*Item to Submit*"**:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/AdVimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/AdVimage.png)

<p class="callout info">💡 Lembrar de **<span class="ql-badge-red">desativar </span>o "Parent Required"** pois temos a **opção "Sem quebra", e ela deve aparecer mesmo sem opção de agrupamento** selecionado.</p>

# Ativação da Engine BigPdf para Exportação de Relatórios

1. Sincronize a sua base local JEDI  
    [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/yYAimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/yYAimage.png)

Verifique se as unidades `qrprntr.pas` e `UCSPrinterPDF.pas` estão presentes no projeto e se estão atualizadas.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/0Zzimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/0Zzimage.png)

#### **Preparando um `TQuickRep` ou `TQRCompositeReport` para exportação de relatórios com mais de 15.000 páginas em PDF.**

---

1. Se os seus relatórios não geram mais de 15 mil páginas, você não necessita continuar lendo, os relatórios já estarão atualizados, ou seja, o processo de geração e exportação já estão prontos.
2. Na seção “*implementation*” da unidade contendo o relatório que gerará milhares de páginas, adicione à claúsula “*uses*” a unidade “*UExportaPDF*”, se a mesma não estiver presente.  
    [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/2iNimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/2iNimage.png)
3. Se o formulário contém somente um *TQuickRep*, adicione a linha de instrução abaixo no manipulador do evento *OnBeforePrint* do *TQuickRep.* ```
    Sender.QRPrinter.BigPdf := true;
    ```
    
    [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/MWtimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/MWtimage.png)  
    [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/2PYimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/2PYimage.png)
4. Se o relatório, também, será executado através do menu principal do módulo, adicione a linha de instrução abaixo logo após o *begin* do manipulador de evento do botão de visualização (esta instrução garante que o arquivo PDF temporário de uma ativação do *preview* seja deletado antes do *preview* ser chamado novamente).  
    ```
    Self.ExcluiBigPdf;
    ```
    
    [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/L46image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/L46image.png)
5. Antes da chamada do método *GeraArquivo*, a engine de exportação para PDF deverá ser modificada para *BigPdf.*
    
    [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Lx0image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Lx0image.png)
6. Os passos descritos aplicam-se aos componentes *TQRCompositeReport* também.
7. Realize os processos de “*Clean*” e “*Build*”, através do Project Manager do Delphi.  
    [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/TBPimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/TBPimage.png)
8. Realize os testes necessários para validar a geração do PDF com milhares de páginas.

#### **Configuração de Relatórios com Múltiplos `TQuickRep` ou um `TQRCompositeReport`.**

---

1. Em situações onde há dois ou mais Quick/Composite, você irá configurar cada um deles como apresentado nas instruções abaixo:  
    [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/EgVimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/EgVimage.png)
2. Neste caso há necessidade do uso explícito do nome do arquivo temporário, porque poderá ser ativado um ou outro relatório, a criação do arquivo e o controle do mesmo já foram programados nas classes de base, você necessita somente adicionar a linha abaixo nos manipuladores dos *OnBeforePrint.*   
      
    ```
    ConfigureQRPrinterParaBigPdf(sender.QRPrinter);
    ```
    
    [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/uXtimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/uXtimage.png)
    
    [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/EDXimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/EDXimage.png)
    
      
    <p class="callout info">**👀 Observação**: a verificação se o QRPrinter é válido, evita a exceção “AV”. Em testes, neste ponto (BeforePrint) o atributo QRPrinter sempre continha um endereço de instância válido. Ou seja, a condicional pode ser retirada.</p>
3. A mudança do engine de exportação deve ser realizada para todos os *Quick/Composite* que irão gerar milhares de páginas.  
    [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/N2Rimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/N2Rimage.png)
    
    [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/48qimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/48qimage.png)
4. Não esqueça de adicionar a linha de instrução *self.ExcluiBigPdf,* como já descrito neste documento, no início das instruções do botão associado a visualização do relatório.
5. Realize o processo de “*Clean*” e “*Build*”.
6. Realize os testes em todos os relatórios presentes no formulário.
7. Bom trabalho!

# CSOrdena

#### <span class="text-big">**Substituição do Componente CSOrdena pelo CheckListBox**</span>

---

Como o Componente **CSOrdena foi descontinuado** este guia foi feito para que o desenvolvedor possa **realizar a troca para o novo componente CheckListBox**, mesmo que tenha pouco conhecimento em Delphi.

#### **O Que é o CSOrdena?**

---

O componente atua como um **agrupador dinâmico dentro de uma query SQL**, pois ele permite que o usuário manipule a tela podendo criar a ordenação do seu relatório da forma que preferir dentro das opções dadas, passando o que está a esquerda para a direita.

##### **Exemplo**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/7q0image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/7q0image.png)

#### **Como Funciona?**

---

Cada linha representa uma coluna da query, assim o desenvolvedor faz esta relação dentro das propriedades do componente.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/b3Gimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/b3Gimage.png)

##### **Propriedade aaCampos**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/fqrimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/fqrimage.png)

##### **Propriedade aaValorCampos**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/pEcimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/pEcimage.png)

<p class="callout info">💡 Note que os **nomes legíveis estão na mesma ordem de suas colunas na query**, deste modo "Número Lançamento" representa `num_lancamentobancario` e respectivamente a mesma ordem para os outros campos.</p>

#### **Por que Trocar o Componente?**

---

Ele **não é suportado pelo mapeamento feito pelo Print Server** ao realizar a emissão pelo APEX, e como normalmente usamos o mesmo Form para o sistema desktop e a WEB devemos fazer a troca pelo CheckListBox (suportado pelo mapeamento).

#### **O Que é o CheckListBox?**

---

O componente não é feito internamente pela CS e **vem de uma biblioteca de terceiros** (preferencialmente usar da aba “Additional”), que está mapeado no Print Server.

##### **Exemplo**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Rheimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Rheimage.png)

##### **Como Funciona?**

Da mesma forma que o **CSOrdena** este componente faz o agrupamento dinâmico dentro do **Order by** de uma query, porém a diferença é que em suas propriedades não existe a relação de "**Campos"** e "**Valor"**, sendo feito este link pelo código usando a posição indexada de cada opção, dentro da propriedade "**Itens"**.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/to2image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/to2image.png)

##### Propriedade Itens

Esta ordem de cadastro será a mesma usada mais a frente para criar a junção com os campos da query.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/qAcimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/qAcimage.png)

#### **Pré-Requisitos para Realizar a Troca**

---

- Primeiro capture o formulário pela ferramenta do JEDI.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/eI9image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/eI9image.png)

- Após conectar com o seu usuário encontre o **Form** na listagem dentro da aba "**Project Manage**r".

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/4Qpimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/4Qpimage.png)

- Por padrão geralmente esta aba abrirá com a Unit do formulário selecionada, mas caso não abra, deve ser feita a procura pelas **Units**.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/R67image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/R67image.png)

- Para saber se está na Unit correta, compare o nome do **Form** que está aberto junto da linha selecionada
- Depois clique com o botão direito para realizar a captura da Unit na opção "**Check Out"**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/zmmimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/zmmimage.png)

- A linha ficara em vermelho simbolizando que o formulário e a Unit estarão capturados para edição.

#### **Realizando a Troca** 

---

- Começando de fato a troca de componentes, pesquise na aba inferior direita **"Tool Palette", o componente CheckListBox.**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/04Iimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/04Iimage.png)

- Depois arraste o componente para o **Form** (ainda não remova o **CSOrdena**).
- O **CheckListBox** virá como um quadrado banco, pois ainda não temos campos cadastrados nele.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Uzvimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Uzvimage.png)

- Agora faça o comparativo dos dois, levando o que está na propriedade "**aaCampos"** e "**aaCamposPadrao"** do CSOrdena para a Propriedade "**Items"** do **CheckListBox** (estas opções são para que o nome sugestivo fique aparente).

<p class="callout info">**👀 Obs.**: configure a "**Font"** do novo componente seguindo o padrão apresentado a seguir, pois **esta mudança também terá impactos no legado.**</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/1v3image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/1v3image.png)

#### **Eventos do CheckListBox**

---

Os componentes do Delphi são configurados via eventos que eles suportam, assim no caso desta alteração temos que **modificar 4 eventos** para que tudo funcione corretamente.

- Para o Delphi criar a procedure do evento basta apenas clicar duas vezes em cima da linha em branco referente ao evento requerido.  
    O resultado será semelhante a este, note que o nome do evento é igual ao da procedure (**simbolizando que este é o evento criado/selecionado**).

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/CpYimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/CpYimage.png)

#### **Criando Variáveis Globais para o Funcionamento Correto**

---

No campo de variáveis do **Form** deve-se adicionar estas 3 (três) variáveis que serão usadas no decorrer do programa:

```
  vs_retorno: String;
  iOrigem, iDestino : Integer;
```

##### **Exemplo**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/PX9image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/PX9image.png)

- Estas variáveis estão a nível da Unit podendo ser chamadas de "variáveis globais" a nível do formulário em questão.

#### **Criando Procedures**

---

Neste manual serão usadas **duas procedures criadas pelo desenvolvedor**, sendo elas a **`AutoMoverItem`** e `<strong>PegaOrigem</strong>`. Para criar procedures no Delphi deve-se declara-las na "**type"** do código no **Form** (de preferência deixe no final como no exemplo a seguir).

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/PSwimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/PSwimage.png)

`procedure AutoMoverItem(CkList:TCheckListBox);`

`procedure PegaOrigem(Sender,Source: TObject; X, Y: Integer; State: TDragState; var Accept: Boolean);`

- Após adicionar este trecho, vá para a chamada das procedures (após a palavra "**Implementation"** e preferencialmente crie as procedures no começo do código para facilitar a busca delas caso tenha que fazer alterações).
- Como esta é a chamada de uma procedure que não possui evento de componente devemos cria-la no código também.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/SFgimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/SFgimage.png)

##### **Procedures que Serão Criadas**

```
procedure {CALSSE DO FORM}.AutoMoverItem(CkList: TCheckListBox);
var i, conta, posicao_nova, posicao_antiga : Integer;
    marca_todos : boolean;
begin
   try
      conta := 0;  //Verificar se não foi marcado nenhuma opção de agrupamento

      posicao_antiga := 0;
      for i := 0 to CkList.Items.Count - 1 do
      begin
         if CkList.Checked[i] then
         begin
            conta          := conta + 1;
            posicao_antiga := i;
         end;
      end;

      marca_todos := conta >= CkList.Items.Count;

      posicao_nova := 0;
      for i := 0 to CkList.Items.Count - 1 do
      begin
         if CkList.Checked[i] then
            posicao_nova := i
         else
            break;
      end;

       //move os itens para a Ordem de Seleção na mesma CheckListBox
       //se tem mais que um selecioando e estão todos selecionados
      if ((conta > 0) and (not(marca_todos))) then
         if CkList.Checked[CkList.ItemIndex] then
         begin
            if (conta = 1) and (posicao_nova = 0) then
               CkList.Items.Move(CkList.ItemIndex,0)
            else
            begin
               if posicao_antiga = posicao_nova then
                  CkList.Items.Move(CkList.ItemIndex,posicao_antiga)
               else
               begin
                  posicao_nova := posicao_nova + 1;
                  CkList.Items.Move(CkList.ItemIndex,posicao_nova);
               end;
            end;
         end
         else
         begin
            CkList.Items.Move(CkList.ItemIndex,CkList.Items.Count-1);
         end;

   except
   end;

end;
```

---

```
procedure {CALSSE DO FORM}.PegaOrigem(Sender, Source: TObject; X,
  Y: Integer; State: TDragState; var Accept: Boolean);
begin

  try
     if (Source is TCheckListBox) and (State = dsDragEnter) then
        iOrigem := (Sender as TCheckListBox).ItemIndex;
  except
  end;
end;
```

####  **Evento OnClick do CheckListBox**

---

**Adicione o trecho:** `AutoMoverItem(Sender as TCheckListBox); // agrupamento dinâmico`

##### **Adicionar as Variáveis na Procedure**

```
var i, conta, posicao_nova, posicao_antiga, x : Integer;
    marca_todos : boolean;
```

#####  **Dentro do Bloco BEGIN...END**

```
// Verifica se não foi marcado nenhuma opção de ordenação
   conta          := 0;
   posicao_antiga := 0;
   for i := 0 to {NOME DO ChekListBox}.Items.Count - 1 do
   begin
      if {NOME DO ChekListBox}.Checked[i] then
      begin
         conta          := conta + 1;
         posicao_antiga := i;
      end;
   end;
   posicao_nova := 0;
   for i := 0 to {NOME DO ChekListBox}.Items.Count - 1 do
   begin
      if {NOME DO ChekListBox}.Checked[i] then
         posicao_nova := i
      else
         break;
   end;
   if conta > 0 then
      if not marca_todos then
         if {NOME DO ChekListBox}.Checked[{NOME DO ChekListBox}.ItemIndex] then
            if (conta = 1) and (posicao_nova = 0) then
               {NOME DO ChekListBox}.Items.Move({NOME DO ChekListBox}.ItemIndex,0)
            else
            begin
               if posicao_antiga = posicao_nova then
                  {NOME DO ChekListBox}.Items.Move({NOME DO ChekListBox}.ItemIndex,posicao_antiga)
               else
               begin
                  posicao_nova := posicao_nova + 1;
                  {NOME DO ChekListBox}.Items.Move({NOME DO ChekListBox}.ItemIndex,posicao_nova);
               end;
            end;
```

##### Exemplo

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/ON8image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/ON8image.png)

Evento OnDragOver do CheckListBox: `PegaOrigem(Sender,Source,X,Y,State,Accept); // agrupamento dinâmico`

##### **Evento OnDrawItem do CheckListBox:**

```javascript
with (Control as TCheckListBox) do
    begin
       if Checked[Index] then
          Canvas.Font.Color := clBlack
       else
       begin
          if Selected[Index] then
             Canvas.Font.Color := clNavy
          else
             Canvas.Font.Color := clBlack;
       end;
       Canvas.FillRect(Rect);
       Canvas.TextOut(Rect.Left, Rect.Top, (Control as TCheckListBox).Items[Index]);
    end;
```

#### **No Evento de Visualizar o Relatório**

---

Aqui é onde de fato será feita a logica do agrupador, para segurança, apenas comente as chamadas do **CSOrdena** durante o código e após estar tudo testado (no Projeto de Relatório e no legado), remova as chamadas junto com o componente.

Como já dito antes o **CheckListBox** trabalha usando a posição dos itens cadastrados para fazer ligação com os campos da query, assim devemos usar um “for” nos itens verificando se estão marcados ou não.

**Exemplo:**

Deve-se criar as seguintes variáveis na Procedure do evento:

```
var i:integer; 
vs_macro:  String;
```

#####  **Dentro do bloco BEGIN...END**

<p class="callout info">**👀 Obs.:** colocar os **trechos abaixo antes do OPEN da query referente ao relatório**, pois é durante a abertura dela que será feita a montagem da ordenação dinâmica.</p>

```
for i := 0 to{NOME DO ChekListBox}.Items.Count - 1 do
   begin
    if ({NOME DO ChekListBox}.Items.Strings[i] = 'Número Lançamento') and ({NOME DO ChekListBox}.Checked[i]) then
    begin
      vs_macro := vs_macro + 'num_lancamentobancario,';
    end
    else
    if (({NOME DO ChekListBox}.Items.Strings[i] = 'Cheque') and ({NOME DO ChekListBox}.Checked[i])) then
    begin
      vs_macro := vs_macro +  'documento,';
    end
    else
    if (({NOME DO ChekListBox}.Items.Strings[i] = 'Histórico') and ({NOME DO ChekListBox}.Checked[i])) then
    begin
      vs_macro := vs_macro +  'cod_historico,';
    end
    else
    if (({NOME DO ChekListBox}.Items.Strings[i] = 'Data Movimento') and ({NOME DO ChekListBox}.Checked[i])) then
    begin
      vs_macro := 'case when atualizou_saldocontabancaria = ''N'' then nvl(datavencimento,datamovimento) else datamovimento end,' + vs_macro;

    end
   end;
```

<p class="callout info">**👀 Obs.**: Note que estamos passando tudo para a variável `VS_MACRO` , pois é ela que será usada pela macro (texto dinâmico na SQL) da query depois de montada a ordenação desejada.</p>

- Caso seja preciso usar uma ordenação caso o usuário deixe de marcar as opções pode-se utilizar um "**IF"** comparando se a `VS_MACRO` está vazia ou não, passando para a variável global `VS_RETORNO`.

```
if vs_macro = '' then
    vs_retorno := 'datamovimento'
   else
    vs_ retorno:= copy(vs_macro, 1, (Length(vs_macro))-1);
```

- Por fim a macro da query recebe a variável com a ordenação montada.

```
{Query do QuickReport}.MacroByName('m_ordem').Value  := vs_ retorno;
```

##### **Exemplo**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/lefimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/lefimage.png)

#### **Ponderações Finais**

---

Caso precise deixar opções marcadas no inicializar do formulário, para que fique idêntico ao legado com o **CSOrdena**, utilize este comando no evento **OnShow** do formulário.

```
{NOME DO ChekListBox}.Checked[3] := true;
```

O valor entre os colchetes "\[ \]" é referente a posição dos itens cadastrados no componente, começando sempre do 0.

##### **Exemplo**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/f0bimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/f0bimage.png)

Para liberar o formulário com as suas alterações basta ir ao "**Project Manager"** encontrar a **Unit** do **Form** alterado, clicar com o botão Direito e desta vez ir para a opção "**Check In"**.

##### **Exemplo**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/1gcimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/1gcimage.png)

# Implementação Geral

Em resumo, a implementação do *front-end* de um relatório no APEX é bem simples, basta **adicionar um botão à página, configurar o de ➝ para dos itens e Executar uma *Procedure*.**

#### **Botão Gerar Relatório**

---

O botão `GERAR_RELATORIO` deve ser adicionado a região **"*page-title*"**:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/zMLimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/zMLimage.png)

Ele estará na posição: "*Next*", com o Template: "*Text with Icon*" usando a Classe: `cs-async` com o icone: `fa-print`, como segue:

<p class="callout success">**Padrão:** Os nomes devem ser mantidos, pois, são usados internamente nos processos de Fila de Execução (link)</p>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/PORimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/PORimage.png)

Atribuímos ao botão "GERAR\_RELATORIO" o *Static ID*: "gerar-relatorio" , como segue:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/9ZTimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/9ZTimage.png)

Pós botão configurado, criamos a Ação dinâmica "clickGerarRelatorio" com o "*event"* do tipo "*Click"*

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/EdRimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/EdRimage.png)

E nela adicionamos uma "True Action" com a ação do tipo: "Open Region" e atribuímos a região "Opções de exportação \[Global Page\]", como segue:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Sqgimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Sqgimage.png)

<p class="callout info">As opções de exportação não precisam ser configuradas, pois, já existe em toda página 0 (Zero) das aplicações.</p>

#### **Itens de Página**

---

Uma vez a página desenvolvida no APEX replicando os filtros que existem no Legado, o <span class="ql-background-color ql-bg-blue">de➝para</span> é feito através do "*Help Text"* de cada item:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/abBimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/abBimage.png)

com os seguintes parâmetros:

- <span class="ql-background-color ql-bg-grey">item\_destino </span>
    - Nome do item no Delphi (NAME). Indica qual o item / componente que receberá o valor no formulário do relatório.
    - Ex. de uso: "`item_destino: EDT_Cod_Equipamento;`"
    - Não possui Valor *Default.* Parâmetro Obrigatório.
- <span class="ql-background-color ql-bg-grey"> item\_destino\_aux </span>
    - Nome do item no Delphi (NAME). Indica qual o item / componente que "auxilia" o "item\_destino" no formulário do relatório (comumente usado com e ).
    - Ex. de uso: "`item_destino_aux: CSMF_Equipamento;`"
    - Valor *Default: null*
- <span class="ql-background-color ql-bg-grey"> ordem </span>
    - Similar ao TAB ORDER no Delphi, é a ordem que os itens serão populados pela interface na tela do relatório.
    - Ex. de uso: "`ordem: 1;`"
    - Não possui Valor *Default.* Parâmetro Obrigatório.
- <span class="ql-background-color ql-bg-grey"> manual </span>
    - Caso atribuído o valor "S", indica que o item em questão será tratado manualmente pelo programador na interface na tela do relatório (ignorando o processo padrão automático de tratamento e atribuição de valores), pois existe alguma especificidade.
    - Ex. de uso: "`manual: S;`"
    - Valor *Default*: N

<p class="callout info">Caso não necessite usar o "item auxiliar" ou não ira "tratar manualmente" o item / componente em questão, basta não menciona-los no "*help text"*, como no exemplo abaixo.   
</p>

```
item_destino: EDT_Cod_Equipamento;
ordem: 1; 
```

#### **Procedure de Impressão**

---

Uma vez o botão de impressão criado e itens devidamente configurados, podemos enfim adicionar o procedimento que irá adicionar nosso relatório a fila de impressão.

Para isso basta acessar a **aba "*Processing*"** e criar um **"*process"***: `pr_gerar_relatorio`

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/EbBimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/EbBimage.png)

Como segue:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/msOimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/msOimage.png)

Com as seguintes mensagens de <span class="ql-background-color ql-bg-green"> <span style="color: rgb(45, 194, 107);">**sucesso**</span> </span>e <span class="ql-background-color ql-bg-red"> <span style="color: rgb(224, 62, 45);">**erro**</span></span>:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/KBuimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/KBuimage.png)

<p class="callout success">**Mensagem de Sucesso:** Relatório adicionado com sucesso à fila de impressão.</p>

<p class="callout danger">**Mensagem de Erro:** Erro ao tentar adicionar relatório à fila de impressão.</p>

Com o "*Server-side Condition*" referenciando o botão `ADICIONAR_RELATORIO_FILA`:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/njvimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/njvimage.png)

E parar finalizar, faremos efetivamente a Chamada do Procedimento `csweb.pkg_fila_impressao.pr_gerar_relatorio` no campo **"*PL/SQL Code*" da sessão "*Source*"** como exemplo:

```
 csweb.pkg_fila_impressao.pr_gerar_relatorio;
```

Caso use a **configuração <span class="ql-text-color ql-color-green"> PADRÃO </span> para gerar o relatório**, basta chama-la sem passar parâmetros, porém, caso precise, a procedure lhe dá possibilidade de informar as algumas configurações. Vamos entender então <span class="ql-background-color ql-bg-orange"> TODOS </span>os parâmetros usados na `pr_gerar_relatorio` .

##### **Parâmetros**

<div class="ql-block" data-block-id="block-ba88af97-63b8-4669-9e16-8087ab1a264b" id="bkmrk-pn_app_id-%3D%3E-nv%28%27app">`pn_app_id => nv('APP_ID') `</div><div class="ql-block ql-indent-1" data-block-id="block-8deb537b-003e-4548-b937-994cfac6ea98" id="bkmrk-id-da-aplica%C3%A7%C3%A3o-apex">- ID da aplicação APEX cujo esta gerando o relatório, por padrão atribui o APP em execução.

</div><div class="ql-block" data-block-id="block-51d5844f-6003-4320-8b19-625604741194" id="bkmrk-pn_page_id-%3D%3E-nv%28%27ap">` pn_page_id => nv('APP_PAGE_ID') `</div><div class="ql-block ql-indent-1" data-block-id="block-ede6e9c5-f29d-4885-a316-9e4b0033d572" id="bkmrk-id-da-p%C3%A1gina-apex-cu">- ID da Página APEX cujo esta gerando o relatório, por padrão atribui a Página em execução.

</div><div class="ql-block" data-block-id="block-df490c81-6d09-4b1a-b929-9eac4207828a" id="bkmrk-pv_tipo_arquivo-%3D%3E-v">`pv_tipo_arquivo     => v('FORMATO_ARQUIVO_REL')`</div><div class="ql-block ql-indent-1" data-block-id="block-c18e2f3e-3dc5-4645-99fa-281bf032c85c" id="bkmrk-formato-em-que-o-rel">- Formato em que o relatório será gerado ( Já programado no item GLOBAL "FORMATO\_ARQUIVO\_REL")

</div><div class="ql-block" data-block-id="block-0d1fb7fa-80f8-4552-9a4f-0b3731e7aaf3" id="bkmrk-pv_static_id-%3D%3E-%27ger">`pv_static_id        => 'gerar-relatorio'`</div><div class="ql-block ql-indent-1" data-block-id="block-5b9b3e12-4c95-4947-9324-535a35a704a1" id="bkmrk-static_id-do-bot%C3%A3o-q">- static\_id do botão que ficará com o "*spinning*" ou mesmo a função impeditiva da Fila de Execução em segundo plano. Adotamos o padrão o nome "gerar-relatorio", mas pode ser alterado de acordo com a necessidade.

</div><div class="ql-block" data-block-id="block-5ff62df0-f6d8-4d3e-a59a-45fcf553e931" id="bkmrk-pv_titulo-%3D%3E-%27relat%C3%B3">`pv_titulo           => 'Relatório de Exemplo'`</div><div class="ql-block ql-indent-1" data-block-id="block-3b9d3385-01f9-4334-ab2d-4eb47b1321fe" id="bkmrk-t%C3%ADtulo-da-tarefa-de-">- Título da tarefa de impressão na Fila de Execução em segundo plano.

</div><div class="ql-block ql-indent-1" data-block-id="block-bd320a5c-5a23-40f7-9abb-55a5018a1efe" id="bkmrk--13">  
</div><div class="ql-block" data-block-id="block-fdcf6e9f-0e46-46c2-b637-efac759d7d25" id="bkmrk-pv_titulo_erro-%3D%3E-%27e">`pv_titulo_erro      => 'Erro ao gerar o relatório de Exemplo.'`</div><div class="ql-block ql-indent-1" data-block-id="block-ccc0b46d-f6ec-49d9-a12c-65c51a49ba01" id="bkmrk-t%C3%ADtulo-caso-ocorra-u">- Título caso ocorra um erro na tarefa de impressão na Fila de Execução em segundo plano.

</div><div class="ql-block ql-indent-1" data-block-id="block-9944dfbf-2f0b-4040-b7ba-86fd08ef1a69" id="bkmrk--14">  
</div><div class="ql-block" data-block-id="block-a4fcdde4-eea6-4b6c-8e33-c70f5cdf64e2" id="bkmrk-pv_msg_sucesso-%3D%3E-%27r">`pv_msg_sucesso      => 'Relatório de Exemplo gerado com sucesso.'`</div><div class="ql-block ql-indent-1" data-block-id="block-1faf8754-5cd1-4a62-8efc-7181320cee51" id="bkmrk-mensagem-de-sucesso-">- Mensagem de sucesso da tarefa de impressão na Fila de Execução em segundo plano.

</div><div class="ql-block ql-indent-1" data-block-id="block-32354b3a-f136-4e26-aaf7-a4a7cab8e980" id="bkmrk--15">  
</div><div class="ql-block" data-block-id="block-1f2c7e9f-4746-4766-88ad-a5306ad5a9a8" id="bkmrk-pv_msg_erro-%3D%3E-%27ocor">`pv_msg_erro         => 'Ocorreu um erro ao gerar o relatório de Exemplo.'`</div><div class="ql-block ql-indent-1" data-block-id="block-b3426562-522f-4310-8f82-52996d5a21ec" id="bkmrk-mensagem-de-erro-da-">- Mensagem de erro da tarefa de impressão na Fila de Execução em segundo plano.

</div><div class="ql-block" data-block-id="block-2a010d3f-bfb8-4ad7-b411-6c9315ddce0c" id="bkmrk-pv_impeditivo-%3D%3E-%27n%27">`pv_impeditivo       => 'N'`</div><div class="ql-block ql-indent-1" data-block-id="block-2cef8953-f88a-4865-8ccc-0937f55a112b" id="bkmrk-indica-se-a-fila-de-">- Indica se a Fila de Execução irá "bloquear a tela" ou seja, impedir que outra ação seja feita na tela, até que o relatório seja gerado.

</div><div class="ql-block" data-block-id="block-fdb2bd84-1bf2-44cc-9dd9-c09eeb04bcee" id="bkmrk-pv_notifica_usuario-">`pv_notifica_usuario => 'N' `</div><div class="ql-block ql-indent-1" data-block-id="block-c9ded407-03fb-43cb-bfbf-d95b66ae1859" id="bkmrk-indica-se-a-fila-de--1">- Indica se a Fila de Execução irá notificar ou não ou usuário através do sistema de notificação do CS 4.0 (sininho) ao final do processo em segundo plano. No nosso caso <span class="ql-background-color ql-bg-red">**NUNCA** </span>notificamos o usuário via notificação da , pois, tratamos as notificações de forma específica na fila de impressão, alterando cores, ícones e clicks de botão, de acordo com a nossa necessidade.

</div><div class="ql-block ql-indent-1" data-block-id="block-6af5b9a6-5e91-4ba3-8229-4bc039dcb6ca" id="bkmrk--16">  
</div><div class="ql-block" data-block-id="block-8bf2d925-22ef-4feb-a43e-9436966d5455" id="bkmrk-pn_minutos_limite-%3D%3E">` pn_minutos_limite =>  120  `</div><div class="ql-block ql-indent-1" data-block-id="block-20ddfc17-f5f8-4291-b7ba-609e8fa368c9" id="bkmrk-quantidade-de-minuto">- Quantidade de minutos que o JOB aguardará resposta de conclusão / erro na geração do relatório. Por padrão aguardaremos 120 minutos (2 horas). Essa opção tem a finalidade de liberar o job em situações cujo o robô de impressão esta desligado ou algum item gerado em modo "Debug" foi esquecido no fila.

---

</div>**Páginas de exemplo ➝** 40201:400, 40201:560, 40201:500, 40201:540, 40201:550, 40201:510, 40201:530 e 40201:520.

# Item sem Título/Label

Informe o ***Label* do componente normalmente**, para que possa aparecer de forma inteligível nos filtros do repositório de relatórios.

Para que o *Label* não seja exibido, em **"*Appearance"*** basta atribuir o template: ***Hidden** :*

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/WMwimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/WMwimage.png)

Então, em Layout ajuste o **"*Label Column Span*"** para 0:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/7Foimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/7Foimage.png)

# Multifiltro

Para utilizar Multifiltro, **programamos o Multifiltro no APEX "exatamente" de acordo com o que esta no Delphi** e para fazermos o de ➝ para informaremos **apenas o "edit" referente ao código**, e no item auxiliar o nome do componente `CSmultifiltro`, segue exemplo:

```
item_destino: dbedit_exemplo;
item_destino_aux: CSMF_Exemplo;
```

Onde o item `dbedit_exemplo` receberá o valor e a interface de impressão usará o componente `CSMF_Exemplo` para efetuar a filtragem.

**Os valores no APEX podem ser:**

- Nenhum registro selecionado (NULL) para indicar todos registros (Equivalente ao "0 - TODOS" no Delphi);
- Um único registro selecionado;
- Múltiplos registros selecionados, sendo os múltiplos registros separados por ":".

# Pré-requisitos

Sempre verificar se a aplicação possui os itens:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/KCGimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/KCGimage.png)

Que são computados no "*Before Header*" das páginas:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/rXfimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/rXfimage.png)

Eles são itens de atribuição estática, que fazem referência ao código da Gestão/Módulo dos Executáveis de Relatório. Executáveis esses, que são criados especificamente para uso com o CSPRINTSERVER.

Esse executáveis possuem o nome com o sufixo `_REL` e nunca serão os mesmos das Gestões/Módulos já em uso no ERP legado, pois esses módulos são cadastrados no ato da conversão do projeto para o uso junto ao CSPRINTSERVER.

<p class="callout warning">**Atenção: <span class="ql-background-color ql-bg-red" style="color: rgb(224, 62, 45);">NUNCA</span>** usar a formatação de duas casas com "0" (Zero) a esquerda no início dos códigos de Gestão e Módulo (Ex.: **<span style="color: rgb(224, 62, 45);">01 <span class="ql-background-color ql-bg-orange">&lt;- Isso é errado</span></span>)**, sempre encare essa configuração como um "Número Inteiro" e **NÃO** use zero a esquerda (Ex.: <span style="color: rgb(22, 145, 121);">**1 <span class="ql-background-color ql-bg-green">&lt;- Isso é Correto</span>**</span>). Esse cuidado é necessário, pois, isso pode provocar erros no tratamento desse dado posteriormente.</p>

# Repositório de Relatórios

Repositório temporário, limpo, no mínimo, a **cada 30 dias.**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/5xdimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/5xdimage.png)

# Seleciona GEF

Para utilizar Seleciona GEF, programamos o Seleciona GEF no APEX de acordo com os padrões pé estabelecidos em [Multifiltro](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/multifiltro "Multifiltro") e para fazermos o de ➝ para i**nformaremos o "edit" do Grupo, Empresa e Filial de dentro do Componente**. No item auxiliar informamos o nome do componente `CSSelecionaGEF`, segue exemplo:

```
item_destino: CS_SelecionaGEF1.DBE_CodGrupoEmpresa;
item_destino_aux: CS_SelecionaGEF1;
ordem: 1;
```

#### **Grupo Empresa**

---

Onde o item `CS_SelecionaGEF1.DBE_CodGrupoEmpresa` receberá o valor do **GRUPO EMPRESA** e a interface de impressão usará o componente `CS_SelecionaGEF1` para efetuar a filtragem.

<p class="callout info">👀 **Obs.:** O componente `CS_SelecionaGEF1` **pode ter seu nome alterado de acordo com o desejo do desenvolvedor**, porém, **o "Edit":** `DBE_CodGrupoEmpresa`, **<span class="ql-background-color ql-bg-red">NUNCA </span> mudará de nome**, pois, é um item <span class="ql-background-color ql-bg-purple">FIXO</span> e "imutável" dentro do componente `CS_SelecionaGEF`. Tornando obrigatório o uso desse exato nome para referenciar o GRUPO.</p>

```
item_destino: CS_SelecionaGEF1.DBE_CodEmpresa;
item_destino_aux: CS_SelecionaGEF1;
ordem: 2;
```

#### **Empresa**

---

Onde o item `CS_SelecionaGEF1.DBE_CodEmpresa` receberá o valor da **EMPRESA** e a interface de impressão usará o componente `CS_SelecionaGEF1` para efetuar a filtragem.

<p class="callout info">👀 **Obs.:** O componente` CS_SelecionaGEF1` **pode ter seu nome alterado de acordo com o desejo do desenvolvedor**, porém, o **"Edit":** `DBE_CodEmpresa`, **<span class="ql-background-color ql-bg-red">NUNCA </span> mudará de nome,** pois, é um item <span class="ql-background-color ql-bg-purple">FIXO</span> e "imutável" dentro do componente `CS_SelecionaGEF`. Tornando obrigatório o uso desse exato nome para referenciar a Empresa.</p>

```
item_destino: CS_SelecionaGEF1.DBE_CodFilial;
item_destino_aux: CS_SelecionaGEF1;
ordem: 3;
```

#### **Filial**

---

Onde o item `CS_SelecionaGEF1.DBE_CodFilial` receberá o valor da **FILIAL** e a interface de impressão usará o componente `CS_SelecionaGEF1` para efetuar a filtragem.

<p class="callout info">👀 **Obs.:** O componente `CS_SelecionaGEF1` **pode ter seu nome alterado de acordo com o desejo do desenvolvedor**, porém, o **"Edit":** `DBE_CodFilial`, **<span class="ql-background-color ql-bg-red">NUNCA </span> mudará de nome**, pois, é um item <span class="ql-background-color ql-bg-purple">FIXO</span> e "imutável" dentro do componente `CS_SelecionaGEF`. Tornando obrigatório o uso desse exato nome para referenciar a Filial.</p>

<p class="callout warning">Importante que os componentes de filtro no APEX de **Grupo, Empresa e Filial estejam ordenados em sequencia**. </p>

Os valores no APEX podem ser:

- Nenhum registro selecionado (NULL) para indicar todos registros (Equivalente ao "0 - TODOS" no Delphi);
- Um único registro selecionado;
- Múltiplos registros selecionados, sendo os múltiplos registros separados por ":".

<p class="callout success">**✅ Padrão:** Por convenção, o `CodGrupoEmpresa` **<span class="ql-background-color ql-bg-red">NUNCA </span>poderá ser ZERO ou multi-seleção**. Ele é um campo de seleção unitária e obrigatória.</p>

# Validação de Datas

Certamente, garantir a precisão e a integridade dos dados em relatórios é de extrema importância, e as validações nos campos de datas desempenham um papel crucial nesse processo. Abaixo, descrevo um exemplo mais detalhado de como realizar as validações de campos de datas em relatórios:

<p class="callout success">⭐ Primeiro, é necessário seguir o **padrão de layout conforme a documentação de UX**.  
[Campos de Datas](https://wiki.cscompusoftware.com.br/books/erp-guideline-de-uiux/page/campos-de-data "Campos de Datas - Boas Práticas") e [Campos Obrigatórios](https://wiki.cscompusoftware.com.br/books/erp-guideline-de-uiux/page/campos-de-formulario#bkmrk-campos-obrigat%C3%B3rios "Campos Obrigatórios - Formulário")</p>

Na aba Processing criar as seguintes Validating

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/2MCimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/2MCimage.png)

#### **Data Inicial**

---

Na primeira validação, na seção "Data inicial is not null" em "Validação" e "PL/SQL Expression", insira o seguinte código:

```
:P870_DATA_INICIAL IS NOT NULL
```

Logo em seguida, na opção **Data inicial is not null ➝ Validação ➝ Erro**, adicione a seguinte mensagem: <span style="background-color: rgb(191, 237, 210);">**Data inicial deve ser informada.**</span>

**Na opção Data inicial is not null ➝ Validação ➝ Associated Item, associe o item da sua página.**

##### **Exemplo Completo do Procedimento**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/cZFimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/cZFimage.png)

#### **Data Final**

---

Na segunda validação, na seção "Data final is not null" em "Validação" e "PL/SQL Expression", insira o seguinte código:

```
:P870_DATA_FINAL IS NOT NULL
```

 Logo em seguida, na opção **Data final is not null ➝ Validação ➝ Erro**, adicione a seguinte mensagem: <span style="background-color: rgb(191, 237, 210);">**Data final deve ser informada.**</span>

Na opção **Data final is not null ➝ Validação ➝ Associated Item,** associe o item da sua página.

##### **Exemplo Completo do Procedimento**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/fDUimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/fDUimage.png)

#### **Data Final maior que a Data Inicial**

---

Na terceira validação, na seção "Data final maior data inicial" em "Validação" e "PL/SQL Expression", insira o seguinte código:

```
to_date(:P870_DATA_FINAL,'dd/mm/rrrr') >= to_date(:P870_DATA_INICIAL,'dd/mm/rrrr')
```

<div class="ql-block" data-block-id="block-fad9aa75-6444-4958-be5f-4ce8a8820abe" id="bkmrk-logo-em-seguida%2C-na--1">Logo em seguida, na opção **Data final maior data inicial ➝ Validação ➝ Erro**, adicione a seguinte mensagem: <span style="background-color: rgb(191, 237, 210);">**A data inicial não pode ser maior que a data final.**</span>  
</div><div class="ql-block" data-block-id="block-fad9aa75-6444-4958-be5f-4ce8a8820abe" id="bkmrk--6"></div><div class="ql-block" data-block-id="block-1724b724-d4bd-4b59-a685-835c434ba9e1" id="bkmrk-na-op%C3%A7%C3%A3o%C2%A0data-final-">Na opção **Data final maior data inicial ➝ Validação ➝ Associated Item**, associe o item da sua página.</div><div class="ql-block" data-block-id="block-1724b724-d4bd-4b59-a685-835c434ba9e1" id="bkmrk--7"></div>##### **Exemplo Completo do Procedimento**

<div class="ql-block" data-block-id="block-1724b724-d4bd-4b59-a685-835c434ba9e1" id="bkmrk--8"></div>[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Q8Vimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Q8Vimage.png)

---

Aqui está um exemplo de uso do código [40112:870](40112:870).

# Report Read Only (Contextual Info)

Neste guideline, será explicado como fazer quando devemos trazer informações em um **bloco read only nos padrões adotados UI/UX.** Segue um exemplo abaixo de como deve ficar visualmente:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/6RXimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/6RXimage.png)

Como o nome sugere, a região deverá ser um **Classic Report;**

1. Na aba Region, o Appearence terá o Template Standard e, caso necessário, removendo o Header (quando o título da região não for importante);
2. Colocar a classe `cs-contextual-info` em CSS Classes;  
      
    [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/nHXimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/nHXimage.png)
3. Ainda no Classic Report, selecionar a aba Atributes e manter as seguintes configurações: 
    - no Layout, manter Number of Rows em 1, mudar se necessário;
    - Template Type: Theme | Template: Contextual Info;
    - Show Null Values as: "-"
    - No Pagination;
    - Template Options: Selecionar a opção "Stacked" para o Display Labels e "Hide when all rows displayed para a última opção;  
        [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/NO3image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/NO3image.png)
        
        [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/tKGimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/tKGimage.png)

# Retorno de Item de Página Modal

#### **Configuração na Página de Origem (Principal)**

---

Na página principal, crie um botão com a ação do tipo *"Redirect to Page in this Application"* ou *"Redirect to Page in* a different *Application"* (a depender da necessidade) e faça a chamada para a página modal previamente criada.

**Exemplo:**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/tjJimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/tjJimage.png)

No mesmo botão que está chamando o modal, crie uma ação dinâmica com as seguintes configurações:

- **Name:** *DialogClosed*
- **Event:** *DialogClosed*

 Edite a ação "True" padrão da seguinte maneira.

**Settings:**

- **Action:** *Set Value*
- **Set Type:** *Dialog return Item*
- **Return Item:** `Seu item da página modal a qual retornará o valor`

<p class="callout info">**💡 Observação:** esse é o item da página MODAL e não da página "atual/origem".</p>

Affected Elements:

- **Selection Type:** item(s)
- **Itens:** `Seu item de página que recebera o valor`

Caso tenha mais de um item para retorno, crie uma "True action" para cada item.

**Exemplo:**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/zmRimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/zmRimage.png)

#### **Configuração na Página Modal**

---

Crie um botão com a action do tipo: `Submit page`. Esse botão será responsável por executar o processo de "close dialog", e assim fechar a tela.

Crie um processo de `Close Dialog` com as seguintes configurações.

- **Identification:**
    
    
    - Name: OnCloseDialog (alterar conforme necessário)
    - Type: Close Dialog
- **Settings:**
    
    
    - Itens to return: `Os itens que retornarão valor`
- **Server-Side Condition:**
    
    
    - Type: Request = Value
    - Value: `Botão responsável pelo Submit da página.`
- **Server-Side Condition:**

**Exemplo:**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/yWhimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/yWhimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/kj6image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/kj6image.png)

# RTF to HTML

Em nossas aplicações temos campos que estão no componente Rich Text do Delphi que são guardados geralmente em formato *RTF.*

No APEX normalmente trataremos o dado em **HTML** pois é uma das opções que temos nativo do componente Rich Text no APEX.

Para fazermos essa alteração devemos pedir ao time da gestão encarregada do módulo que estamos fazendo para na tabela que possui o RTF criar uma coluna do tipo CLOB na tabela com o mesmo nome da coluna RTF, porém com o final "`_HTML`".

**Exemplo:** "TEXTO" ➝ "TEXTO\_HTML"

Após o time criar a nova coluna, utilizaremos a o seguinte bloco anônimo no PL/SQL para fazermos a passagem do RTF para HTML.

```
declare
  clob_rtf  clob;
  clob_html clob;
begin
  for x in (select coluna_origem, PK
              from tabela
             where coluna_origem is not null) loop
    csweb.pkg_apex_rtf.pr_rtf_to_html(x.coluna_origem, clob_html);
  
    update tabela
       set coluna_destino= clob_html
     where PK= x.PK;
  end loop;

end;
```

<p class="callout info">**💡 Vale lembrar que:**  
coluna\_origem ➝ É a coluna da tabela que possui o RTF.  
PK ➝ É a PK da tabela, quando for várias PKs adicionar elas também.  
tabela ➝ É a tabela que está sendo alterada.  
coluna\_destino ➝ É a coluna da tabela que irá receber o HTML.</p>

Após isso é necessário fazer o **commit** para validar o <u>update</u>.

Depois na tela que estiver fazendo as alterações deve trazer a coluna destino para o usuário visualizar em HTML e poder fazer as alterações que quiser no registro.

# Sidebar Buttons

##### Durante a migração do sistema legado em Delphi para o APEX, era de certa forma comum existir botões laterais de ações ou "facilitadores" que devido a certas circunstancias da regra de negócio, eles se habilitam ou desabilitam.

<details id="bkmrk-imagem-exemplar"><summary>Imagem exemplar</summary>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-07/scaled-1680-/67himage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-07/67himage.png)

</details>##### Para isso, foi desenvolvido a funcionalidade de criar uma sidebar a esquerda ou direita na qual é possível adicionar botões de forma nativa. Podendo ser expandida ou colapsável.


#####  Para isso, seguiremos os seguintes passos:

Primeiramente iremos adicionar uma region que será o **container** da nossa sidebar e ao lado dela adicionaremos outra region que dentro dela ficará os conteúdos da nossa página.  
  
*Obs: siga de uma forma onde seguirá essa estrutura*

- *Container  
      
    Sidebar Container - Conteúdo Container*

<details id="bkmrk-imagem-exemplar-1"><summary>Imagem exemplar</summary>

[![Untitled-2026-06-26-1133.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-07/scaled-1680-/untitled-2026-06-26-1133.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-07/untitled-2026-06-26-1133.png)

</details><details id="bkmrk-imagem-exemplar-apex"><summary>Imagem exemplar APEX - Page Designer</summary>

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-07/scaled-1680-/ijcimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-07/ijcimage.png)

</details>[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-07/scaled-1680-/mu1image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-07/mu1image.png)

Após ter adicionado a region de sidebar, iremos para opção **Column Span** na sessão **Layout** da region e colocaremos o valor como **2.**

Após ter informado o Column Span da region sidebar, iremos adicionar ás seguintes **Classes CSS**:

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-07/scaled-1680-/jPEimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-07/jPEimage.png)

**cs-sidebar-buttons** (obrigatório) - Será responsável por informar que é uma region do tipo sidebar-buttons.

**cs-sidebar-left** ou **cs-sidebar-right** (obrigatório) - Será respónsável por informar que nossa region sidebar buttons esta alinhada para a esquerda ou para a direita.

**cs-fixed-to-top** (opcional) - será responsável por fazer com que a nossa region do tipo sidebar buttons fique totalmente no topo sem espaçamento.

  
  
Feito isso, iremos adicionar mais duas regions, a primeira seria a **region controller**. Na qual ficará o nosso botão controlador, que será responsável por alterar o estado da nossa sidebar de entre expandido e colapsádo. Dentro da region, iremos adicionar o nosso botão controlador.

Após adicionarmos o botão controlador, passaremos os seguintes valores em seus respectivos atributos:

<table border="1" id="bkmrk-atributo-valor-obser" style="border-collapse: collapse; width: 100.002%;"><colgroup><col style="width: 33.3333%;"></col><col style="width: 33.3333%;"></col><col style="width: 33.3333%;"></col></colgroup><thead><tr><td>**Atributo**  
</td><td>**Valor**  
</td><td>**Observação**

</td></tr></thead><tbody><tr><td>Label</td><td>Expandir</td><td>Ao iniciar a tela, esse será o tooltip inicial do botão.

</td></tr><tr><td>Button Template</td><td>Icon</td><td>O botão controlador deverá possuir apenas o ícone

</td></tr><tr><td>CSS Classes</td><td>cs-sidebar-button--controller</td><td>Será a classe CSS para indicar o botão controlador da sidebar

</td></tr><tr><td>Icon</td><td>fa-layout-nav-left | fa-layout-nav-right</td><td>Caso a sidebar esteja a esquerda, devermos passar fa-layout-nav-left, se caso estiver a direita, passaremos fa-layout-nav-right.

</td></tr></tbody></table>

Após termos passado os atributos para o botão controlador, iremos adicionar uma Dynamic Action do tipo **click** no botão. Dentro da Dynamic Action, iremos adicionar uma action do tipo **Execute JavaScript Code**. E faremos a chamada da função que alterará o estado da sidebar passando o valor **this** ou o **Static ID** do botão.

```javascript
// Exemplo passando this como valor
alterSidebarState(this);

// Exemplo passando o Static ID do botão
alterSidebarState('b-controller-left');
```

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-07/scaled-1680-/QTPimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-07/QTPimage.png)

Após isso, iremos adicionar a nossa segunda region dentro da region sidebar. Essa será a **region buttons**, na qual será o container de todos os botões da nossa sidebar.

Em todos os botões é **obrigatório** adicionar um ícone e um texto ao botão, exceto no botão controlador. Caso contrário ao recolher o sidebar, não ficará nenhum ícone a ser visualizado no botão.

🥳 Seguindo os passos corretamente, está pronto a sua sidebar expandivel e colapsável.

*Tela de Exemplo: 40754:970*

# TAB por ENTER

# Boas Práticas do Uso do TAB por ENTER

Nesse contexto vamos demonstrar boas práticas no uso da funcionalidade **TAB por Enter e na separação dos código e descrições.**

- Configure os campos de código e descrição para que eles **fiquem perto um do outro**.
- Deixe o **código alinhado à direita** no input.
- Sempre que a tela tiver **botões de ação principal**, como botões de "Gerar relatório" em relatórios e botões de "Filtrar", **inclua eles na configuração do TAB por Enter**.
- No **campo descrição não repita o código**, deixe somente a descrição.
- Caso seu campo aceite a filtragem de todos os registros, **não coloque o placeholder** "**--TODOS**" **no campo do código**, penas deixe o campo vazio.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/fDcimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/fDcimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/j3limage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/j3limage.png)

🔗 [Saiba como configurar o espaçamento entre os campos de código e descrição](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/configuracao-de-espacamento-entre-itens "Espaçamento entre Itens")

🔗 [Saiba como configurar a funcionalidade "TAB por "ENTER"](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/navegacao-tab-por-enter-novo "Nova Navegação por Enter nos Itens de Tela")

#### **Quais Campos Devem ser Separados?**

---

Em telas de Manutenção, Relatório e Consulta, os campos abaixo ***sempre*** devem ter seu código separado da descrição:

- **Material**
- **Fornecedor**
- **Funcionário/Pessoa**
- **Produto**

Nas **telas de Processo e telas de alto fluxo** TODOS os campos devem ter seus códigos e suas descrições separados.

<p class="callout warning"> Sempre que tiver **campos com código e descrição separados**, deve-se configurar o **TAB por ENTER**.</p>

#### **Campos Multiseleção**

---

- No campo do **código** não coloque o placeholder "**--TODOS** ", apenas deixe o campo vazio.
- O placeholder `<M>` irá **aparecer automaticamente** quando houver diversas seleções.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/z7Jimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/z7Jimage.png)

 [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Oojimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Oojimage.png)

<p class="callout info">**👀 Obs:** A funcionalidade **TAB por ENTER ainda está em desenvolvimento para campos multiseleção**.</p>

#### **Campos Obrigatórios**

---

- Se o campo é obrigatório, ele deve estar indicado com o **asterisco (\*) vermelho em ambos campos**.
- No back-end, coloque somente o **required no campo da descrição**.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/ttRimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/ttRimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/f9aimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/f9aimage.png)

# Configuração de Espaçamento entre Itens

Essa configuração remete para quando nas telas tem **separadamente os campos de código e descrição**.

#### **Separação entre os Itens**

---

**Item Spacing: None**

[![BRhimage.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/brhimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/brhimage.png)

#### **Item do Código** 

---

**Right Margin: Small**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/YXQimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/YXQimage.png)

# Configuração de Grupo de Colunas em Interactive Grids (IG)

Esta função `setCustomConfigIGColumns` foi criada para facilitar a **configuração de grupos de colunas** em **Interactive Grids (IG)** no Oracle APEX, permitindo uma organização mais eficiente e personalizada das colunas.

#### **Como Utilizar** 

---

##### **Sintaxe Básica**

`setCustomConfigIGColumns(config, options);`

##### **Parâmetros**

<table border="1" id="bkmrk-par%C3%A2metro-tipo-descr" style="border-collapse: collapse; width: 100%; height: 90.0157px;"><colgroup><col style="width: 16.0906%;"></col><col style="width: 19.9227%;"></col><col style="width: 63.9867%;"></col></colgroup><thead><tr style="height: 29.7969px;"><td style="height: 29.7969px;">**Parâmetro**</td><td style="height: 29.7969px;">**Tipo**</td><td style="height: 29.7969px;">**Descrição**</td></tr></thead><tbody><tr style="height: 30.1094px;"><td style="height: 30.1094px;">`config`</td><td style="height: 30.1094px;">Object</td><td style="height: 30.1094px;">Objeto de configuração existente do IG (opcional) </td></tr><tr style="height: 30.1094px;"><td style="height: 30.1094px;">`options`</td><td style="height: 30.1094px;">Object</td><td style="height: 30.1094px;">Configurações personalizadas para grupos e colunas</td></tr></tbody></table>

##### **Estrutura do** `<strong>options</strong>`

```
{
  groups: [
    {
      name: "Nome do Grupo",                               // Nome visível do grupo
      id: "id-do-grupo",                                  // ID único (opcional - será gerado automaticamente se não informado)
      label: "Rótulo",                                   // Rótulo alternativo (opcional)
      columns: [
        {
          name: "Nome da Coluna",                 // Nome da coluna no IG
          hideHeader: true/false                 // Oculta o cabeçalho da coluna (opcional)
        }
      ]
    }
  ]
}
```

#### **Funcionamento Interno**

---

1. **Identificação do Grid:**
2. **Criação/Atualização de Grupos:**
3. **Configuração de Colunas:**
    - Para cada coluna dentro de um grupo: 
        - Vincula a coluna ao grupo pai
        - Aplica configurações adicionais (como ocultar cabeçalho)
    - Para cada grupo definido em `options.groups`, a função: 
        - Cria um novo grupo (se não existir)
        - Atualiza grupos existentes com as novas configurações
    - A função tenta obter o ID do IG automaticamente se não for fornecido no `config`.
4. **Retorno:**
    - Retorna o objeto `config` atualizado com os novos grupos e configurações

#####  **Exemplo Prático**

```
(originalConfig) => setCustomConfigIGColumns(originalConfig, {
  context: this,                   // opcional (elemento de contexto)
  groups: [
    {
      name: "Dados do Pneu",
      columns: [
        { name: "Sulco"},
        { name: "Pneu", hideHeader: true }
      ]
    }
  ]
})
```

#### **Observações Importantes**

---

1. A função **não substitui** configurações existentes - apenas as complementa
2. Se o ID do grid não for encontrado automaticamente, será necessário fornecer `config.regionStaticId`
3. Use `console.log` para verificar a configuração gerada antes de aplicar ao IG

#####  **Benefícios**

✅ Organização visual de colunas em grupos temáticos

✅ Facilidade de manutenção das configurações

✅ Compatível com grids existentes

✅ Personalização flexível de cabeçalhos

#### **Aplicando a Chamada**

---

Aplicar a chamada no "**Javascript Inicialization Code**" presente dentro da interactive grid para poder apontar as colunas que irão receber o GrupoPai

- Lembrando que a utilização é só recomendada quando precisa-se de um nível acima do grupo que o Apex já disponibiliza

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/fgeimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/fgeimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/iJ7image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/iJ7image.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/FR5image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/FR5image.png)

# Navegação Tab Interactive Grid

###### Explicação detalhada da Função `'setupGridNavigationWithTab'`

Esta função configura uma navegação avançada por teclado (especialmente com a tecla Tab) em uma Interactive Grid do Oracle APEX, além de adicionar atalhos úteis para operações comuns.

#### **Funcionalidades Principais**

---

1. **Navegação com Tab:**
    - Permite navegar entre células usando **Tab (avança) e Shift+Tab (volta).**
    - Ao chegar na última célula de uma linha, vai para a **primeira célula da próxima linha.**
    - Na última célula da última linha, **volta para a primeira célula da primeira linha.**
2. **Atalhos de teclado:**
    - `Alt+C:` Copia o valor da célula atual (opcional)
    - `Alt+S:` Aciona o botão de salvar (opcional)
    - `Alt+X:` Aciona o botão de excluir
    - `Ctrl+Alt+N:` Aciona o botão de adicionar novo registro
    - `Ctrl+E:` Exporta a grid para CSV

#### **Como Utilizar**

---

**Sintaxe Básica**

```
setupGridNavigationWithTab(staticId, enableCopy, enableSave);
```

#### **Parâmetros**

---

<table border="1" id="bkmrk-par%C3%A2metro-tipo-obrig" style="border-collapse: collapse; width: 100%;"><colgroup><col style="width: 16.2098%;"></col><col style="width: 10.7271%;"></col><col style="width: 12.9917%;"></col><col style="width: 46.2437%;"></col><col style="width: 13.8278%;"></col></colgroup><thead><tr><td>**Parâmetro**</td><td>**Tipo**</td><td class="align-center">**Obrigatório**</td><td>**Descrição**</td><td>**Valor Padrão**</td></tr></thead><tbody><tr><td>`'staticId'`</td><td>string</td><td class="align-center"><span style="color: rgb(45, 194, 107);">✅ **Sim**</span></td><td>O static ID da Interactive Grid (definido nas propriedades da região)</td><td>------</td></tr><tr><td>`'enableCopy'`</td><td>boolean</td><td class="align-center">❌ **<span style="color: rgb(224, 62, 45);">Não</span>**</td><td>Habilita o atalho Ctrl+C para copiar valores de células</td><td>`'false'`</td></tr><tr><td>`'enableCopy' `</td><td>boolean

</td><td class="align-center">❌ **<span style="color: rgb(224, 62, 45);">Não</span>**</td><td>Habilita os atalhos `Ctrl+S `(salvar) e `Ctrl+X` (excluir</td><td>`'false'`</td></tr></tbody></table>

####  **Exemplos de Uso**

---

##### **Exemplo 01: Configuração Básica**

// Configura apenas a navegação por Tab

```javascript
setupGridNavigationWithTab('minhaGrid');
```

##### **Exemplo 2: Com cópia de células**

// Habilita navegação por Tab + Alt+C para copiar valores

```javascript
setupGridNavigationWithTab('produtosGrid', true);
```

##### **Exemplo 3: Com todos os recursos**

// Habilita todos os atalhos (Tab, Alt+C, Alt+S, Alt+X, Ctrl+Alt+N, Ctrl+E)

```javascript
setupGridNavigationWithTab('clientesGrid', true, true);
```

#### **Detalhes de Implementação** 

---

##### **Seleção da Grid**

- A função localiza a grid usando o **static ID** fornecido
- Verifica se a grid existe antes de prosseguir

##### **Navegação**

- Usa **jQuery** para encontrar células visíveis e linhas
- Implementa lógica para navegação cíclica (volta ao início quando chega no final)

##### **Atalhos**

- Remove **event listeners** antigos para evitar duplicação
- Adiciona novos **listeners** para os eventos de teclado
- Os atalhos só funcionam quando uma célula da grid está em foco

##### **Funções auxiliares**

- `<strong>'copyCellValue'</strong>`: Copia texto da célula para área de transferência
- **`'clickSaveButton'`**: Simula clique no botão de salvar
- `<strong>'clickDeleteButton'</strong>`: Simula clique no botão de excluir
- `<strong>'clickAddButton'</strong>`: Simula clique no botão de adicionar
- `<strong>'</strong><strong>exportarRelatorioGrid'</strong>`: Exporta dados para CSV

#### **Requisitos e Considerações**

---

##### **Pré-requisitos**

- **jQuery** deve estar carregado na página.
- O **APEX** deve estar na versão 5.0 ou superior (que introduziu Interactive Grids).

##### **Configuração da Grid**

- A grid deve ter um **static ID** definido.
- Os botões de salvar/excluir/adicionar devem ter os **IDs** padrão do APEX (se forem usados os atalhos).

##### **Compatibilidade**

- A função de copiar (**Ctrl+C**) usa a API moderna `'navigator.clipboard'` com **fallback** para `'<strong>document.execCommand'</strong>`
- Deve funcionar na maioria dos navegadores modernos.

##### **Customização**

- Você pode modificar os seletores de botões no início da função se estiver usando **IDs** customizados.
- Pode adicionar mais atalhos conforme necessidade.

#### **Exemplo Completo de Implementação**

---

- Na página do APEX, vá para a seção "**JavaScript**" &gt; "**Função e Variáveis Globais**"
- Cole o código da função `'<strong>setupGridNavigationWithTab'</strong>`
- Adicione um "**Dynamic Action**" que execute quando a página carregar.

# Navegação TAB por ENTER (Depreciado)

#### **Análise da Função configEnterTab**

---

A função **configEnterTab** é um utilitário JavaScript para navegação inteligente entre campos em formulários APEX usando **Enter** e **ESC**, com tratamento especial para componentes como **multifiltros** e campos de **data**. Ela permite:

1. **Navegação por Enter**:
2. **Saída do Multifiltro com ESC**:
3. **Tratamento Especial para Campos de Data**:
4. **Busca Automática ou Manual**:
5. **Exclusão de Campos**:
6. **Controle de Foco**: 
    - Mantém o estado do campo atual (`currentFocusedIndex`).
    - Gerencia o foco visual em **multifiltros** (adicionando/removendo a classe `focused`).
    - Permite definir uma lista de IDs para **ignorar** durante a navegação.
    - Se **nenhum ID** for passado, ela busca automaticamente todos os campos visíveis na página (**inputs, selects, textareas,** etc.).
    - Se **IDs forem fornecidos**, navega apenas entre eles.
    - Se o **APEX** for versão **24+**, ajusta o seletor para focar no campo de data corretamente.
    - Se o campo atual for um **multifiltro**, pressionar **ESC** fecha o componente e move o foco para o próximo campo (sem voltar ao início).
    - Pressionar **Enter** move o foco para o próximo campo.
    - **Shift + Enter** volta para o campo anterior.
    - No último campo, se houver um botão de submit definido, pressionar Enter aciona o clique nele.

#### **Exemplos de Uso**

---

##### **1. Uso Básico (Busca Automática)**

// Navega por todos os campos visíveis da página (P1\_\*)

```javascript
configEnterTab();
```

##### **2. Definindo um Botão de Submit**

// Navega por todos os campos e define "P1\_BTN\_SUBMIT" como botão de submit

```javascript
configEnterTab([], "P1_BTN_SUBMIT");
```

##### **3. Navegação Apenas Entre Campos Específicos**

// Navega apenas entre esses 3 campos + botão de submit

```javascript
configEnterTab(
  ["P1_NOME", "P1_EMAIL", "P1_MULTIFILTRO"],
  "P1_BTN_ENVIAR"
);
```

##### **4. Ignorando Campos (Exclusão)**

// Navega por todos os campos, exceto "P1\_CAMPO\_IGNORADO"

```javascript
configEnterTab([], "P1_BTN_SUBMIT", ["P1_CAMPO_IGNORADO"]);
```

##### **5. Uso em Páginas com Prefixo Diferente (ex: P2\_)**

// Força a navegação em campos de P2\_\*

```javascript
configEnterTab(
  ["P2_NOME", "P2_EMAIL", "P2_DATA"],
  "P2_BTN_CONFIRMAR"
);
```

#### **Novo Parâmetro**

---

Novo parâmetro na função **enter/tab**, os itens que tiverem esse atributo serão ignorados pela função do **Tab/Enter**, sendo possível colocar em uma região, e todos os itens dessa região não serão acessados.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/scaled-1680-/F9Nimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-10/F9Nimage.png)

```
apex_tab_ignore="true"
```

Tendo também um parâmetro novo que pode ser passado na função que **define em qual item você quer começar o foco**, podendo ser qualquer item visível, em tela.

```
configEnterTab(
                ['P1_FIELD1', 'P1_FIELD2', 'P1_FIELD3'],      // IDs dos elementos (Não Obrigatório)
               'P1_SUBMIT',                                  // ID do botão de submit (Não Obrigatório)
                [ 'P1_FIELD4' ],                            // IDs a excluir (Não Obrigatório declarar)
               'P1_FIELD2'                                 // Foco inicial no segundo campo, podendo seguir e retroceder para P1_FIELD1
                                                                                                           (Não Obrigatório declarar) );
```

##### **Em uma lista \[array\] declarada**

```
configEnterTab(
               ['P1_FIELD1', 'P1_FIELD2', 'P1_FIELD3'],    // IDs dos elementos (Não Obrigatório)
               null,                                      // ID do botão de submit (Não Obrigatório)
               null,                                     // IDs a excluir (Não Obrigatório declarar)
              'P1_FIELD2'                               // Foco inicial no segundo campo, podendo seguir e retroceder para P1_FIELD1
                                                                                                        (Não Obrigatório declarar) );
```

##### **Em uma lista \[array\] não declarada**

```
configEnterTab(
                null,                           // IDs dos elementos (Não Obrigatório)
                null,                          // ID do botão de submit (Não Obrigatório)
                null,                         // IDs a excluir (Não Obrigatório declarar)
               'P1_FIELD2'                   // Foco inicial no segundo campo, podendo seguir e retroceder para P1_FIELD1
                                                                                             (Não Obrigatório declarar) );
```

##### Ou

```
configEnterTab(null, null, null, 'SEU_CAMPO_ID');      // Foco inicial no campo, podendo seguir e retroceder
                                                                           (Não sendo Obrigatório declarar) );
```

Sendo esperado que nessa atualização o **`apex_disabled`** e o **disabled** não receba mais foco, quem estava com esses problemas pode me avisar qualquer coisa pois não é para ser mais apresentado esse mesmo problema.

#### **Fluxo de Funcionamento**

---

1. - **Inicialização**: 
        - Detecta campos visíveis ou usa a lista fornecida.
        - Ordena os campos pela posição no DOM.
        - Configura eventos de **Enter** e **ESC**.
2. **Navegação**: 
    - **Enter** → Próximo campo.
    - **Shift + Enter** → Campo anterior.
    - **ESC (em multifiltro)** → Sai e vai para o próximo campo.
3. **Submit**: 
    - Se o último campo for um botão de submit, pressionar Enter o aciona.
4. **Tratamento de Erros**: 
    - Se um campo não existir, ele é ignorado.
    - Logs no console ajudam no debug (`console.log`).

####  **Observações Importantes**

---

##### <span style="color: rgb(45, 194, 107);">**✅ Funciona com**</span>

- Inputs, selects, textareas, multifiltros e botões.
- **APEX 23+** (com tratamento especial para campos de data).

##### <span style="color: rgb(224, 62, 45);">**❌ Não funciona com**</span>

- Campos ocultos (`display: none`, `hidden`).
- Elementos sem ID.

##### <span style="color: rgb(53, 152, 219);">**📝 Personalização**:</span>

- Se a navegação não estiver na ordem desejada, forneça os IDs manualmente.
- Use `excludeIds` para pular campos indesejados.

#### **Resumo Final**

---

Essa função é útil para:

✅ **Formulários complexos** com muitos campos.  
**✅ Melhorar a usabilidade** (navegação sem usar mouse).  
✅ **Evitar problemas** com multi-filtro e campos de data.

<p class="callout info">💡 Se precisar de ajustes, basta modificar os parâmetros (`itemIds`, `submitButtonId`, `excludeIds`). </p>

# Navegação TAB por ENTER (Novo)

<p class="callout success">✅ O novo controle de navegação do **Enter** já está disponível por todo sistema**<u> CS 4.0 automaticamente</u>**.</p>

#### **Teclas**

---

- `ENTER:` avança para o próximo campo
- `(CONTROL ou SHIFT)+ENTER:` volta para o campo anterior  
    <p class="callout info">**Select/Shuttle e TextArea não aceitam o shift** para voltar somente o control)</p>
- `SHIFT+ENTER:` quebra linha em uma TextArea ou abre o select
- `ESPAÇO:` abre o select

#### **Modificar Comportamento**

---

Automaticamente todos os itens que permitem ENTER já estão incluídos, exceto na interactive grid. Também os campos de descrição após o código e botões são automaticamente excluídos da navegação. Porém se precisar modificar esse efeito você poderá aplicar as classes abaixo no Page Designer no Apex.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Hb3image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Hb3image.png)

##### **Appearance → CSS Classes**

- `apex-enter-key-nav--include:` para incluir o elemento na navegação com ENTER.
- `apex-enter-key-nav--exclude:` para excluir o elemento da navegação com ENTER.
- `apex-enter-key-nav--submit-button:` indica o botão que deverá receber o foco após o último elemento.

#### **Ordem de Navegação**

---

Essa nova versão da navegação por Enter, **não é possível definir ordem aleatória.** Ele **segue a ordem de navegação nativa** **do navegador** **idêntica da tecla "tab"**, que é da esquerda para direita dentro da região (DIV), então quando os elementos da página são colocados em regiões (DIV), a ordem de navegação acontece primeiro dentro da região, depois que irá para a próxima região, então para manipular a ordem de navegação em colunas você precisa entender a dica abaixo.

##### **Modelo de Ordenação 1**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/kLTimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/kLTimage.png)

##### **Modelo de Ordenação 2**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/WLbimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/WLbimage.png)

# Text Messages

Verificar se a aplicação em questão possui idiomas definidos

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/KKmimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/KKmimage.png)

#### **Textos Estáticos**

---

Dentro da Aplicação ➝ Shared Components ➝ Text Messages

Clique em Create Text Messages

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/MQ3image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/MQ3image.png)

 [![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/MAsimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/MAsimage.png)

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/c77image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/c77image.png)

Coloque um nome adequado para a Text Messages (ideal porque como uma "constante" essa text message será chamada dentro do código substituindo o texto estático)

1. Selecione o Idioma (pt-br)
2. Habilite o Used in JavaScript
3. Escreva o texto estático no idioma selecionado

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/i39image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/i39image.png)

Crie outras duas Text Messages com o mesmo nome da anterior porém para os idiomas (es) e (en), traduza os textos para os respectivos idiomas.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/MOCimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/MOCimage.png)

Gere o Seed e Publique.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Nc4image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Nc4image.png)

#### **Label Estático: `&APP_TEXT$NOME_TEXT_MSG.`**

---

**Exemplo:**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/BX4image.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/BX4image.png)

Se você quiser usar comandos HTML dentro da Text message usamos o ***RAW*** no final da chamada.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/W1fimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/W1fimage.png)

####  **Em JS**

---

Chamar a função apex.lang.getMessage('NOME\_TEXT\_MSG')

#### **Em SQL**

---

Chamar a função apex*lang.get\_message*('NOME\_TEXT\_MSG')

#### **Maiores Informações sobre as Funções**

---

##### **JS**

[https://docs.oracle.com/en/database/oracle/apex/22.2/aexjs/apex.lang.html](https://docs.oracle.com/en/database/oracle/apex/22.2/aexjs/apex.lang.html)

##### **SQL**

[https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/APEX\_LANG.GET\_MESSAGE-Function.html?source=%3Aow%3Ams%3Apt%3A%3A#GUID-0E4ED6B6-64E7-4043-9DC9-9C746E595357](https://docs.oracle.com/en/database/oracle/apex/24.2/aeapi/APEX_LANG.GET_MESSAGE-Function.html?source=%3Aow%3Ams%3Apt%3A%3A#GUID-0E4ED6B6-64E7-4043-9DC9-9C746E595357)

# Validações Back-end (APEX)

Nesta aba, será citado algumas regras sobre como estamos executando validações no back-end.

No primeiro exemplo será mostrado uma regra importante e que não costuma acontecer no Delphi: Telas do tipo CRUD simples que possuem só Código e Descrição.

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/scaled-1680-/Gecimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2025-11/Gecimage.png)

Nesse tipo de tela, no Delphi, o campo Descrição não costuma ser um campo OBRIGATÓRIO.

Aqui no nosso ambiente de desenvolvimento APEX, este campo **passa a ser obrigatório**.

Mas qual o motivo?

<p class="callout warning">Não faz sentido uma tabela/grid onde a única informação mostrada ser a Descrição e ela poder ser nula (caso ela não esteja como valor obrigatório, o usuário poderá salvar o registro sem nada nela).</p>

<p class="callout info">**Obs.:** Sempre analisem a tela que estão desenvolvendo. Não serão somente os casos de telas Código/Descrição que isso será uma regra, mas todo o contexto envolvido dela mesma. Exemplo: pode ser que haja uma tela com 10 colunas diferentes e uma delas ser Descrição... DEPENDENDO DO CONTEXTO, ela também será obrigatória, mesmo no delphi não sendo.</p>

#### **Triggers**

---

<p class="callout warning">A validação também não será realizada somente no front-end (APEX). Será necessário **criar uma trigger para que as validações se façam presentes no back-end**, em nosso banco de dados.</p>

Poxa vida, mas qual o motivo disso também?

Um usuário que tiver as manhas de programação e for "espertinho", poderá mexer no front-end e alterar o que quiser, caso as validações não estejam acontecendo no back-end. Por isso a importância de ter nossas queridas Validations de Insert, Update, Delete no back-end.

<p class="callout info">**💡 Obs.:** Citei casos mais genéricos, mas haverão situações (e muitas) em que as validações não só serão realizadas somente por Triggers, mas também dentro de Procedures.</p>

Poxa... Não sei criar uma trigger... E agora?

[🔗 Saiba mais como criar triggers](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/triggers "Triggers")

# View para Item ou Página

Devido a limitação de 4000 carácteres do apex no shared component, em alguns momentos precisaremos criar uma view específica para uma determinada página ou para um determinado item. Para isso, seguimos um padrão, tanto para a nomenclatura da view quanto a estrutura da sua SQL.

A nomenclatura deve ter como prefixo a seguinte sintaxe: "*`vw_apex_(Número da aplicação)_(Número da página no apex)_(Assunto da View`)*".

Por exemplo: `vw_apex_40107_580_dtefetiva`.

Caso a sua view necessite utilizar os próprios itens de página do Apex na sua SQL, fazemos uma select retornando os itens que serão utilizados from dual, em uma with, para depois utilizar estes campos na select principal da view (Sempre que necessário tratar os itens de página, fazemos isso neste passo, como "to\_date()" ou até mesmo "nvl()").

**Exemplo:**

```
with vw_page_params as (
select nv('G_COD_GRUPOEMPRESA') cod_grupoempresa
     , nv('G_COD_EMPRESA') cod_empresa
     , nv('G_COD_FILIAL') cod_fial
     , nv('G_ID_LOGON') id_logon
     , nv('P580_CODIGO') codigo
     , nvl(v('P500_CODIGO'), '0') codigo_com_default
     , to_date(v('P500_DATA'), 'DD/MM/YYYY') data_referencia
     , v('P500_TEXTO') texto
from dual)

select tabela_exemplo.campo1
     , tabela_exemplo.campo2
from   csexemplo.tabela_exemplo
     , vw_page_params
where  tabela_exemplo.texto  = vw_page_params.texto
and    tabela_exemplo.codigo = vw_page_params.codigo
and    tabela_exemplo.data  >= vw_page_params.data_referencia;
```

<span class="ql-bg-blue">O alias deste with também foi padronizado, sendo este definido como: `VW_PAGE_PARAMS`</span>

<span class="ql-bg-blue">Por fim, pode se utilizar como exemplo a seguinte view: </span>

`<span class="ql-bg-blue">vw_apex_40107_580_dtefetiva. </span>`

<span class="ql-bg-blue">Sendo esta, utilizada na página **Empréstimo por Parcela (40107:580)** como LOV do campo `P580_DATA_PARCELA`.</span>

# Telas de Auto Fluxo

### Separa código da descrição conforme visual abaixo

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-08/scaled-1680-/hwoimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-08/hwoimage.png)

#### <span style="text-decoration: underline;">Criar uma região para receber o itens de " **Código** " e " **Descrição** " :</span>

Template**: Black With Attibutes** Template Options **=&gt;** Item Spacing**: None**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-08/scaled-1680-/g8Yimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-08/g8Yimage.png)

#### <span style="text-decoration: underline;">Adicionar dentro da região um item para o código :</span>

Type: **Number Field** ( ou "**Text**" dependendo do conteúdo )  
Template Options =&gt; Right Margin: **Small**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-08/scaled-1680-/vmEimage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-08/vmEimage.png)

#### <span style="text-decoration: underline;">Adicionar dentro da região um item para " **descrição** ":</span>  


Type: **CS-MultiFiltro**

[![image.png](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-08/scaled-1680-/baximage.png)](https://wiki.cscompusoftware.com.br/uploads/images/gallery/2026-08/baximage.png)

<p class="callout info">Como configurar o item "**descrição** " para ler o campo código :   
</p>

[https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/cs-multifiltro-apex-cs-40](https://wiki.cscompusoftware.com.br/books/guidelines-de-apex/page/cs-multifiltro-apex-cs-40)