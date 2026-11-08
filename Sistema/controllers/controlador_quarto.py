from entities.quarto.quarto_simples import QuartoSimples
from entities.quarto.quarto_duplo import QuartoDuplo
from entities.status import Status
from dao.quarto_dao import QuartoDAO



class ControladorQuarto:
    #construtor
    def __init__(self, quarto_dao : QuartoDAO):
       self.__quarto_dao = quarto_dao


    #métodos
    def listar_quartos(self):
        return list(self.__quarto_dao.listar())  # copia
        #for quarto in self.__quartos:
            #print(f"Quarto n° {quarto.numeroQuarto} - STATUS: {quarto.statusQuarto}")

    def buscar_quarto(self, numeroQuarto): #retonar um quarto
        quarto = self.__quarto_dao.buscar_quarto(numeroQuarto)
        if quarto is None:
             raise ValueError("Quarto não encontrado.")
        return quarto

    def __verificarLivre(self) -> bool: #verificar se tem quartos livres
        for quarto in self.__quarto_dao.listar():
            if quarto.statusQuarto == Status.LIVRE:
                return True
            else :
                continue #continua procurando
        return False #passou pela lista toda e nao achou , logo false

    def ocupar_quarto(self, numeroQuarto):
        if not self.__verificarLivre():
            raise ValueError("Não tem quarto disponível.")
        quarto = self.buscar_quarto(numeroQuarto)
        if quarto.statusQuarto != Status.LIVRE: #se o quarto ja estiver ocupado
            raise ValueError("Não pode ocupar esse quarto.")
        self.__quarto_dao.ocupar(numeroQuarto)

    def realizar_limpeza(self, numeroQuarto):
        quarto = self.buscar_quarto(numeroQuarto)
        if quarto.statusQuarto == Status.LIVRE:
            raise ValueError("Quarto não necessita de limpeza.")
        self.__quarto_dao.limpar(numeroQuarto)
        
    def concluir_limpeza(self, numeroQuarto):
        quarto = self.buscar_quarto(numeroQuarto)
        if not quarto.statusQuarto == Status.LIMPEZA:
            raise ValueError("O quarto precisa estar em LIMPEZA para concluir limpeza.")
        self.__quarto_dao.concluir_limpeza(numeroQuarto)









