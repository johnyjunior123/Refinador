import sys
sys.path.insert(0,"../")
from src.atualizarbd import atualizarCrimes, atualizarEnderecos
from models.ConectorMySql import Conector

class Controller:
    
    def __init__(self, config, crimes):
        self.conector = Conector(config)
        self.crimes = crimes

    def atualizarCrimes(self):
        atualizarCrimes(self.conector, self.crimes)

    def conectarNoticiaEmEndereco(self):
        atualizarEnderecos(self.conector)