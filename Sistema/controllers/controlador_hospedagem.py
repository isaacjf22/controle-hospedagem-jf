from itertools import count

from controllers.controlador_cliente import ControladorCliente
from controllers.controlador_quarto import ControladorQuarto

from entities.hospedagem import Hospedagem
from entities.comprovante_hospedagem import ComprovanteHospedagem

from datetime import datetime, time , timedelta



class ControladorHospedagem:
    tempoAtual = datetime.now()
    #construtor
    def __init__(self):
        self.__contador = count(1)
        self.__hospedagensAtivas = []
        self.__entrada = self.tempoAtual
        self.__ctlCliente = ControladorCliente()
        self.__ctlQuarto = ControladorQuarto()

    #métodos
    def realizar_checkin(self, idCliente, numeroQuarto, saidaPrevista) -> None :
        if self.__entrada >= saidaPrevista :
            raise ValueError("A data de saída deve ser após a data de entrada.")

        cliente = self.__ctlCliente.buscar(idCliente)
        quarto = self.__ctlQuarto.buscar_quarto(numeroQuarto)

        hospedagem = Hospedagem(next(self.__contador), self.__entrada, saidaPrevista, cliente, quarto)
        self.__hospedagensAtivas.append(hospedagem)



    def __buscar_hospedagem(self, idHospedagem):
        for hospedagem in self.__hospedagensAtivas:
            if hospedagem.idHospedagem == idHospedagem:
                return hospedagem
        raise ValueError("Hospedagem não encontrada.")






    def __gerar_comprovante(self, idHospedagem) -> ComprovanteHospedagem:
        hospedagem = self.__buscarHospedagem(idHospedagem)
        return ComprovanteHospedagem(hospedagem.cliente.nome, hospedagem.cliente.cpf, hospedagem.e )










        

