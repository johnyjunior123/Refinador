from models.Controller import Controller
from config.config import config
from data.crimes import crimes

controller = Controller(config, crimes)

controller.atualizarCrimes()
controller.conectarNoticiaEmEndereco()