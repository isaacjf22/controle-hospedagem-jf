from quarto import quarto

class QuartoSimples(quarto.Quarto):
    def __init__(self, numeroQuarto):
        super().__init__(numeroQuarto)

    #métodos
    def calcular_diaria(self, dias) -> float:
        return 250*dias


