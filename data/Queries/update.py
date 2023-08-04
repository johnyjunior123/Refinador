import sys
sys.path.insert(0,"../../")
from data.Queries.consults import consultCrimeBruto, consultEnderecoBruto, consultEnderecos, consultEnderecoLograd

def updateCrime(crime, url):
    return f"UPDATE NOTICIA SET CRIME = '{crime}' WHERE CRIME IS NULL AND URL = '{url}'"

def updateEndereco(id_endereco, url):
    return f"UPDATE NOTICIA SET ID_ENDERECO = {id_endereco} WHERE ID_ENDERECO IS NULL AND URL = '{url}'"

def atualizarCrimes(conector, crimes): #O(n²)
    print('Efetuando atualizações...')
    for crime in crimes: 
        itens = conector.consulta(consultCrimeBruto(crime))
        for item in itens:
            conector.inserir(updateCrime(crime, item[0]))
    print('Concluido com sucesso')

def atualizarEnderecos(conector): #O(n²)
    enderecos = conector.consulta(consultEnderecos())
    for endereco in enderecos: 
        itens = conector.consulta(consultEnderecoBruto(endereco[1], endereco[2]))
        for item in itens:
            conector.inserir(updateEndereco(endereco[0],item[0]))
    print('sucesso - relacionamento entre endereços e noticia efetuado')

def atualizarEnderecosRestantes(conector): #O(n²)
    enderecos = conector.consulta(consultEnderecos())
    for endereco in enderecos:
        itens2 = conector.consulta(consultEnderecoLograd(endereco[2]))
        for item in itens2:
            conector.inserir(updateEndereco(endereco[0],item[0]))
