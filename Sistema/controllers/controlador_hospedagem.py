from itertools import count

from entities.comprovante_hospedagem import ComprovanteHospedagem
from entities.extrato_conta import ExtratoConta

from datetime import datetime


from hospedagem import Hospedagem



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
        quarto.ocupar()
        self.__hospedagensAtivas.append(hospedagem)

        return hospedagem.gerar_comprovante()

    def realizar_checkout(self, idHospedagem) -> ExtratoConta:
        hospedagem = self.__buscar_hospedagem(idHospedagem)
        hospedagem.finalizar()
        self.__hospedagensAtivas.remove(hospedagem)

        return hospedagem.gerar_extrato()

    def adicionar_consumo(self, idHospedagem ,nome, quantidade , valorUnitario):
        hospedagem = self.__buscar_hospedagem(idHospedagem)
        hospedagem.adicionar_gasto(nome, valorUnitario, quantidade)

    def listar_hospedagens_ativas(self):
        return list(self.__hospedagensAtivas) #copia inves da original
        #for hospedagem in self.__hospedagensAtivas:
         #   print(f"{hospedagem.id}) QUARTO: {hospedagem.quarto.numeroQuarto} / CLIENTE: {hospedagem.cliente.nome}")

    def __buscar_hospedagem(self, idHospedagem):
        for hospedagem in self.__hospedagensAtivas:
            if hospedagem.id == idHospedagem:
                return hospedagem
        raise ValueError("Hospedagem não encontrada.")








        

