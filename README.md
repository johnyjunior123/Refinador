<h1 style="text-align: center;">Refinador</h1>

![a versão atual do projeto é 1.0](https://img.shields.io/badge/Versão-1.0-279)
![feito em python](https://img.shields.io/badge/Linguagem-Python-321)
![utilizado banco postgreSQL](https://img.shields.io/badge/SGBD-PostgreSQL-244)

 Continuação do projeto de atividade curricular, esse programa se utiliza dos dados recolhidos no programa de Scraping, com objetivo de retirar informações sobre crime e local ocorridos.

 [Programa de Raspagem](https://github.com/johnyjunior123/ScrapingACE4)

<h2>Primeiros passos</h2>

Primeiro será necessário a instalação das bibliotecas do python utilizado no programa:

```pip install urllib3```
```pip install pandas```
```pip install psycopg2```

> importar o Schema com as tabelas atuais no postgree 

<div style="text-align: center"><a src="https://drive.google.com/drive/folders/17FiCBgn4QvJjCM0ulZJEz3kRCnrYO5Pa?usp=sharing">Banco de Dados</a></div>
<br>

> adicionar no arquivo refinador/config/config.py, as credencias para acesso ao postgree, exemplo:

```
    config = ["postgres", "demon123", "127.0.0.1", "noticias"]
```
___
<h2>Utilizando o programa</h2>

>No momento o programa não possuí GUI ou utilização de API, então a utilização é através do controller no arquivo app.py

~~~python 
from models.Controller import Controller
from config.config import config
from data.crimes import crimes

controller = Controller(config, crimes)
~~~

O refinador tem como objetivo retirar informações recolhidas pelo  [Programa de Raspagem](https://github.com/johnyjunior123/ScrapingACE4) sendo as principais funções do controller:


`controller.atualizarCrimes()`

- Nesse comando será analisado a descrição da noticia e retirado uma chave/token que indica o crime cometido adicionando-o na tabela caso o campo crime seja nulo.

`controller.conectarNoticiaEmEndereco()`

- Com base na tabela **enderecos** será analisado na descrição das noticias as ruas que foram cometidos os crimes e atualizado o campo **ID_Endereco (Chave Estrangeira)** na tabela **noticia**.

`controller.equivalencia(equivalencia, keys)`
- Com base na tabela de equivalencia em config\config.py é reduzido a quantidade de categorias crimes dos dados do banco.
___

<h2>Tarefas em desenvolvimento</h2>

- [x] Criar equivalencia nos tokens do arquivo crimes.py reduzindo a quantidade de tokens semelhantes.

> Foi criado os dados de equivalencia na diretorio ./data/crimes.py

- [x] Criar função de atualização de campo crimes no banco de dados com base na equivalencia

> Criado metodo no controller chamado equivalencia models\Controller.py

- [ ] Melhorar o grau de acerto no tratamento da função conectarNoticiaEmEndereco.
