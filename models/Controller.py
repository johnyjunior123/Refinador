import sys
sys.path.insert(0,"C:\\Users\\GAMEPLAI\\Documents\\Faculdade\\ACE4\\Refinador")
from src.atualizarbd import atualizarCrimes, atualizarEnderecos, equivalenciaCrimes
from data.queries.consults import consultCrimeBruto, consultEnderecoBruto, consultEnderecos, consultEnderecoLograd
from data.queries.update import updateCrime, updateEndereco, updateEquivalence
from models.Conector import Conector

class Controller:
    
    def __init__(self, config, crimes):
        self.conector = Conector(config)
        self.crimes = crimes
    
    def atualizarCrimes(self, crimes): #O(n²)
        print('\nEfetuando atualizações...')
        for crime in crimes: 
            itens = self.conector.consulta(consultCrimeBruto(crime))
            for item in itens:
                self.conector.inserir(updateCrime(crime, item[0]))
        print('Concluido com sucesso\n')

    def atualizarEnderecos(self): #O(n²)
        enderecos = self.conector.consulta(consultEnderecos())
        for endereco in enderecos: 
            itens = self.conector.consulta(consultEnderecoBruto(endereco[1], endereco[2]))
            for item in itens:
                self.conector.inserir(updateEndereco(endereco[0],item[0]))
        print('\nsucesso - relacionamento entre endereços e noticia efetuado\n')

    def equivalencia(self, tabelaEquivalencia, keys):
        print("\nIniciando equivalencia...")
        i = 0
        for key in keys: 
            itens = tabelaEquivalencia[i][key]
            for item in itens:
                self.conector.inserir(updateEquivalence(key, item))
            i += 1
        print("Encerrado equivalencia de crimes\n")