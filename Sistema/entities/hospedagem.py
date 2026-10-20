class Hospedagem:
    def __init__(self, id, entrada, saidaPrevista, cliente , quarto ):
        self.__id = id
        self.__entrada = entrada
        self.__saidaPrevista = saidaPrevista
        self.__valorTotal = 0

        #relações
        self.__gastos = []
        self.__quarto = quarto
        self.__cliente = cliente


    def adicionar_gasto(self, gasto) -> None:
        self.__gastos.append(gasto)

