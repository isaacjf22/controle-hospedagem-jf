class Gasto:
    def __init__(self, nome , valorUnitario, quantidade):
        self.__nome = nome
        self.__valorUnitario = valorUnitario
        self.__quantidade = quantidade

    #encapsulamento
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo):
        if novo is not None and not novo.strip(): #verica se o nome tem conteudo e se o nome sem espaço tem conteudo
            self.__nome = novo
        else: #se o nome estiver vazio
            raise ValueError("Escolha de nome inválido.")

    @property
    def valorUnitario(self):
        return self.__valorUnitario
    @valorUnitario.setter
    def valorUnitario(self, novo):
        if novo is not None and novo>0:
            self.__valorUnitario = novo
        else:
            raise ValueError("Escolha de valor unitário inválido.")

    @property
    def quantidade(self):
        return self.__quantidade
    @quantidade.setter
    def quantidade(self, valor):
        if valor is not None and valor>0:
            self.__quantidade = valor
        else:
            raise ValueError("Escolha de valor de quantidade inválido.")

    #métodos
    def calcular_total(self) -> float:
        return  self.__valorUnitario*self.__quantidade


