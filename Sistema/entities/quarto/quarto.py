from abc import ABC, abstractmethod
from entities import status

class Quarto(ABC):
    #construtor
    def __init__(self, numeroQuarto, dias):
        self._numeroQuarto = numeroQuarto
        self._statusQuarto = "LIVRE"
        self._dias = dias


    #encapsulamento
    #definindo somente visualização
    @property
    def numeroQuarto(self):
        return self.__numeroQuarto

    @property
    def statusQuarto(self):
        return self.__statusQuarto

    @property
    def dias(self):
        return self.__dias

    #métodos
    #cada tipo de quarto terá seu próprio calculo de diária
    @abstractmethod
    def calcular_diaria(self) -> float:
        pass

    def enviar_limpeza(self):
        self.__statusQuarto = "LIMPEZA"

    def ocupar(self):
        self.__statusQuarto = "OCUPAR"

    def concluir_limpeza(self):
        self.__statusQuarto = "LIVRE"


