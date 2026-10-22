from itertools import count

from entities.comprovante_hospedagem import ComprovanteHospedagem
from extrato_conta import ExtratoConta

from datetime import datetime


from hospedagem import Hospedagem
from pessoas.pessoa import Pessoa


class ControladorHospedagem:
    #construtor
    def __init__(self, ctlCliente, ctlQuarto):
        self.__contador = count(1)
        self.__hospedagensAtivas = []
        self.__ctlCliente = ctlCliente
        self.__ctlQuarto = ctlQuarto

    #métodos
    def realizar_checkin(self, idCliente, numeroQuarto, saidaPrevista) ->  ComprovanteHospedagem:
        entrada = datetime.now() #a entrada é registrada toda vez q for fzr o login
        if entrada >= saidaPrevista :
            raise ValueError("A data de saída deve ser após a data de entrada.")

        cliente = self.__ctlCliente.buscar(idCliente)
        quarto = self.__ctlQuarto.buscar_quarto(numeroQuarto)

        hospedagem = Hospedagem(next(self.__contador), entrada, saidaPrevista, cliente, quarto)
        self.__hospedagensAtivas.append(hospedagem)
        quarto.ocupar()

        comprovante = self.__gerar_comprovante(hospedagem)
        return comprovante

    def realizar_checkout(self, idHospedagem) -> ExtratoConta:
        hospedagem = self.__buscar_hospedagem(idHospedagem)
        total = hospedagem.finalizar()
        self.__hospedagensAtivas.remove(hospedagem)
        extrato = self.__gerar_extrato(idHospedagem)

        return extrato

    def adicionar_consumo(self, idHospedagem ,nome, quantidade , valorUnitario):
        hospedagem = self.__buscar_hospedagem(idHospedagem)
        hospedagem.adicionar_gasto(nome, quantidade, valorUnitario)

    def concluir_limpeza(self, numeroQuarto):
        quarto = self.__ctlQuarto.buscar_quarto(numeroQuarto)
        quarto.concluir_limpeza()

    def listar_hospedagens_ativas(self):
        for hospedagem in self.__hospedagensAtivas:
            print(f"{hospedagem.id}) QUARTO: {hospedagem.numeroQuarto} / CLIENTE: {hospedagem.cliente.nome}")

    def listar_clietes(self):
        self.__ctlCliente.listar_clientes()

    def listar_quartos(self):
        self.__ctlQuarto.listar_quartos()

    def __buscar_hospedagem(self, idHospedagem):
        for hospedagem in self.__hospedagensAtivas:
            if hospedagem.idHospedagem == idHospedagem:
                return hospedagem
        raise ValueError("Hospedagem não encontrada.")




    def __gerar_comprovante(self, idHospedagem) -> ComprovanteHospedagem:
        hospedagem = self.__buscar_hospedagem(idHospedagem)
        return hospedagem.gerar_comprovante()

    def __gerar_extrato(self, idHospedagem):
        hospedagem = self.__buscar_hospedagem(idHospedagem)
        return hospedagem.gerar_extrato()








        

