import sys
sys.path.insert(0, "../../")

from script.apigeolocalizacao.tomtom import geocode
from config.mysql import enderecos, config
import pandas as pd
from models.Endereco import Endereco
from models.ConectorMySql import Conector
from data.inserts import insertEndereco

def criarDataFrame(enderecos, conector):
    df = pd.read_excel(enderecos)
    for i in range(0, df.count(0)['Enderecos']):
        endereco = tratarEndereco(df.iloc[i]['Enderecos'])
        conector.inserir(insertEndereco(endereco))
        



def tratarEndereco(endereco):
    tipo, *logradouro = endereco.split(' ')
    logradouro = " ".join(logradouro)
    return criarEndereco(tipo, logradouro)


def criarEndereco(tipo, logradouro):
    dadosComplementares = geocode(tipo + ' ' + logradouro + ' Penedo - AL')
    return Endereco(
        tipo,
        logradouro,
        dadosComplementares[0],
        dadosComplementares[1],
        dadosComplementares[2],
        dadosComplementares[3])

conector = Conector(config)
criarDataFrame(enderecos, conector)