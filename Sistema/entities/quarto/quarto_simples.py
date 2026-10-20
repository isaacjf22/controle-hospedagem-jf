from quarto import quarto

class QuartoSimples(quarto.Quarto):
    def __init__(self, numeroQuarto, dias):
        super().__init__(numeroQuarto, dias)

    #métodos
    def calcular_status(self) -> float:
        return 250*self.__dias


