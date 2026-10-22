from quarto import quarto

class QuartoDuplo(quarto.Quarto):
    def __init__(self, numeroQuarto):
        super().__init__(numeroQuarto)

    #métodos
    def calcular_diaria(self, dias) -> float:
        return 500*self.dias