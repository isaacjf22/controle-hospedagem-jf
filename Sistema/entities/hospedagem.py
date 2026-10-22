from datetime import datetime
from entities.comprovante_hospedagem import ComprovanteHospedagem
from entities.extrato_conta import ExtratoConta
from entities.gasto import Gasto

class Hospedagem:
    def __init__(self, id, entrada : datetime, saidaPrevista : datetime, cliente , quarto ):
        self.__id = id
        self.__entrada = entrada
        self.__saidaPrevista = saidaPrevista
        self.__valorTotal = 0
        self.__saida = None


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
    def saida(self):
        return self.__saida

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
    def adicionar_gasto(self, nome, quantidade, valorUnitario) -> None:
        gasto =  Gasto(nome, quantidade, valorUnitario)
        self.__gastos.append(gasto)

    def __calcular_total(self, dias) -> float:
        total = 0
        total += self.__quarto.calcular_diaria(dias)
        for gasto in self.__gastos:
            total += gasto.calcular_total()
        return total

    def gerar_comprovante(self) -> ComprovanteHospedagem:
        return ComprovanteHospedagem(self.__cliente.nome,self.__cliente.cpf,self.__entrada,self.__saidaPrevista, self.__quarto.numeroQuarto)

    def gerar_extrato(self) -> ExtratoConta:
        extrato = ExtratoConta(self.__cliente.nome, self.__cliente.cpf, self.__saida, self.__valorTotal)
        return extrato

    def finalizar(self) -> None:
        if self.__saida is not None:
            raise ValueError("A hospedagem já foi finalizada")

        self.__saida = datetime.now()
        dias = max(1, (self.__saida - self.__entrada).days)
        self.__valorTotal = self.__calcular_total(dias)
        self.__quarto.enviar_limpeza()




