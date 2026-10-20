from quarto import quarto

class QuartoDuplo(quarto.Quarto):
    def __init__(self, numeroQuarto, dias):
        super().__init__(numeroQuarto, dias)

    #métodos
    def calcular_diaria(self) -> float:
        return 500*self.__dias