from entities.quarto.quarto import Quarto

class QuartoDuplo(Quarto):
    def __init__(self, numeroQuarto):
        super().__init__(numeroQuarto)

    #métodos
    def calcular_diaria(self, dias) -> float:
        return 500*dias