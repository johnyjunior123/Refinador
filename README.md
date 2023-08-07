<h1 style="text-align: center;">Raspador de Dados</h1>

![a versão atual do projeto é 1.0](https://img.shields.io/badge/Versão-1.0-279)
![feito em python](https://img.shields.io/badge/Linguagem-Python-321)
![utilizado banco mysql](https://img.shields.io/badge/SGBD-MySQL-244)

 Continuação do projeto de atividade curricular, esse programa se utiliza dos dados recolhidos no programa de Scraping, com objetivo de retirar informações sobre crime e local ocorridos.

 [Programa de Raspagem](https://github.com/johnyjunior123/ScrapingACE4)

<h2>Primeiros passos</h2>

Primeiro será necessário a instalação das bibliotecas do python utilizado no programa:

```pip install urllib3```

> importar o Schema com as tabelas atuais no mysql 

<div style="text-align: center"><a src="https://drive.google.com/file/d/1uS8QgsvJmK_qcSgdoWqDV3IomUJxpRdm/view?usp=drive_link">Banco de Dados</a></div>
<br>

> adicionar na pasta config, um arquivo mysql.py com a config de acesso com o banco de dados, exemplo:

```
    config = {
    "user" : "root",
    "password" : "qualqueruma",
    "host" : "127.0.0.1",
    "database" : "noticias"
}
```
___

<h2>Utilizando o programa</h2>

>No momento o programa não possuí GUI ou utilização de API, então a utilização é através do controller no arquivo app.py

~~~python 
from models.Controller import Controller
from config.mysql import config
from data.crimes import crimes

controller = Controller(config, crimes)
~~~

O refinador tem como objetivo retirar informações recolhidas pelo  [Programa de Raspagem](https://github.com/johnyjunior123/ScrapingACE4) sendo as principais funções do controller:


`controller.atualizarCrimes()`

- Nesse comando será analisado a descrição da noticia e retirado uma chave/token que indica o crime cometido adicionando-o na tabela caso o campo crime seja nulo.

`controller.conectarNoticiaEmEndereco()`

- Com base na tabela **enderecos** será analisado na descrição das noticias as ruas que foram cometidos os crimes e atualizado o campo **ID_Endereco (Chave Estrangeira)** na tabela **noticia**.

___

<h2>Tarefas em desenvolvimento</h2>

- [ x ] Criar equivalencia nos tokens do arquivo crimes.py reduzindo a quantidade de tokens semelhantes.

> Foi criado os dados de equivalencia na diretorio ./data/crimes.py

- [ ] Criar função de atualização de campo crimes no banco de dados com base na equivalencia
- [ ] Melhorar o grau de acerto no tratamento da função conectarNoticiaEmEndereco.
