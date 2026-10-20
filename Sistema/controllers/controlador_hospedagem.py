from itertools import count
from controllers.controlador_cliente import ControladorCliente

class ControladorHospedagem:
    def __init__(self):
        self.__contador = count(1)
        self.__hospedagensAtivas = []
        self.__ctlCliente = ControladorCliente()

        

