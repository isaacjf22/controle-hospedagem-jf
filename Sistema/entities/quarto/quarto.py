from abc import ABC, abstractmethod
from entities.status import Status

class Quarto(ABC):
    #construtor
    def __init__(self, numeroQuarto):
        self._numeroQuarto = numeroQuarto
        self._statusQuarto = "LIVRE"


    #encapsulamento
    #definindo somente visualização
    @property
    def numeroQuarto(self):
        return self._numeroQuarto

    @property
    def statusQuarto(self):
        return self._statusQuarto

    #métodos
    #cada tipo de quarto terá seu próprio calculo de diária
    @abstractmethod
    def calcular_diaria(self, dias) -> float:
        pass

    def enviar_limpeza(self):
        self._statusQuarto = Status.LIMPEZA

    def ocupar(self):
        self._statusQuarto = Status.OCUPADO

    def concluir_limpeza(self):
        self._statusQuarto = Status.LIVRE


