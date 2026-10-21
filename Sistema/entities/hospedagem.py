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


    #encapsulamento
    @property
    def id(self):
        return self.__id

    @property
    def entrada(self):
        return self.__entrada

    @property
    def saidaPrevista(self):
        return self.__saidaPrevista
    @saidaPrevista.setter
    def saidaPrevista(self, novaSaidaPrevista):
        if novaSaidaPrevista is None or self.__saidaPrevista >= novaSaidaPrevista:
            raise ValueError("Escolha da nova data de saída é inválida.")
        self.__saidaPrevista = novaSaidaPrevista

    @property
    def valorTotal(self):
        return self.__valorTotal

    @property
    def cliente(self):
        return self.__cliente

    @property
    def quarto(self):
        return self.__quarto


    #métodos
    def adicionar_gasto(self, gasto) -> None:
        self.__gastos.append(gasto)

