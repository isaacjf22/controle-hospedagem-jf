from entities.quarto.quarto_simples import QuartoSimples
from entities.quarto.quarto_duplo import QuartoDuplo
from entities.status import Status



class ControladorQuarto:
    #construtor
    def __init__(self):
        self.__quartos = (
            [QuartoSimples(n) for n in range(1, 11)] + [QuartoDuplo(n) for n in range(11, 21)]
        )


    #métodos
    def listar_quartos(self):
        for quarto in self.__quartos:
            print(f"Quarto n° {quarto.numeroQuarto} - STATUS: {quarto.statusQuarto}")

    def buscar_quarto(self, numeroQuarto): #retonar um quarto
        for quarto in self.__quartos:
            if quarto.numeroQuarto == numeroQuarto:
                return quarto
        raise ValueError("Quarto não encontrado.")

    def __verificarLivre(self) -> bool: #verificar se tem quartos livres
        for quarto in self.__quartos:
            if quarto.statusQuarto == Status.LIVRE:
                return True
            else :
                continue #continua procurando
        return False #passou pela lista toda e nao achou , logo false

    def ocupar_quarto(self, numeroQuarto):
        if not self.__verificarLivre():
            raise ValueError("Não tem quarto disponível.")

        quarto = self.buscar_quarto(numeroQuarto)
        if quarto.statusQuarto == Status.OCUPADO: #se o quarto ja estiver ocupado
            raise ValueError("Não pode ocupar um quarto já ocupado.")
        quarto.ocupar()

    def realizar_limpeza(self, numeroQuarto):
        quarto = self.buscar_quarto(numeroQuarto)
        if quarto.statusQuarto == Status.OCUPADO:
            raise ValueError("Quarto não necessita de limpeza.")
        quarto.enviar_limpeza()

    def concluir_limpeza(self, numeroQuarto):
        quarto = self.buscar_quarto(numeroQuarto)
        if not quarto.statusQuarto == Status.LIMPEZA:
            raise ValueError("O quarto precisa estar em LIMPEZA para concluir limpeza.")
        quarto.concluir_limpeza()









