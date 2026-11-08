from entities.quarto.quarto import Quarto

class QuartoDuplo(Quarto):
    def __init__(self, numeroQuarto, status, id):
        super().__init__(numeroQuarto, status, id)

    #métodos
    def calcular_diaria(self, dias) -> float:
        return 500*dias