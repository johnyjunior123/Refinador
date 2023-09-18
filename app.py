from models.Controller import Controller
from config.config import config
from data.crimes import crimes, keys, equivalencia

controller = Controller(config, crimes)

# controller.atualizarCrimes(crimes)
controller.atualizarEnderecos()
controller.atualizarEnderecosParte2()
# controller.equivalencia(equivalencia, keys)