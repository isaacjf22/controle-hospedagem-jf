from entities.comprovante_hospedagem import ComprovanteHospedagem
from entities.extrato_conta import ExtratoConta
from entities.gasto import Gasto

from datetime import datetime


from entities.hospedagem import Hospedagem
from dao.hospedagem_dao import HospedagemDAO
from dao.gasto_dao import GastoDAO



class ControladorHospedagem:
    #construtor
    def __init__(self, ctlCliente, ctlQuarto, hospedagem_dao : HospedagemDAO, gasto_dao : GastoDAO):
        self.__hospedagem_dao = hospedagem_dao
        self.__gasto_dao = gasto_dao
        self.__ctlCliente = ctlCliente
        self.__ctlQuarto = ctlQuarto

    #métodos
    def realizar_checkin(self, idCliente, numeroQuarto, saidaPrevista) ->  ComprovanteHospedagem:
        entrada = datetime.now() #a entrada é registrada toda vez q for fzr o login
        if entrada >= saidaPrevista :
            raise ValueError("A data de saída deve ser após a data de entrada.")

        cliente = self.__ctlCliente.buscar_cliente(idCliente)
        quarto = self.__ctlQuarto.buscar_quarto(numeroQuarto)
        hospedagem = Hospedagem(entrada,saidaPrevista, cliente, quarto)

       
        self.__hospedagem_dao.check_in(hospedagem)      #1° marca e dps ocupa
        self.__ctlQuarto.ocupar_quarto(numeroQuarto)

        return hospedagem.gerar_comprovante()

    def realizar_checkout(self, idHospedagem) -> ExtratoConta:
        hospedagem = self.__buscar_hospedagem(idHospedagem)
        quarto = hospedagem.quarto #pegar o tipo de quarto 
        dias = hospedagem.finalizar()
        total = self.__calcular_total(idHospedagem,quarto, dias)
        hospedagem.definir_total(total)
        self.__hospedagem_dao.check_out(idHospedagem,hospedagem.saida,hospedagem.valor_total) #segue a ordem do caso de uso
        self.__ctlQuarto.realizar_limpeza(quarto.numeroQuarto)
        return hospedagem.gerar_extrato()
    
        #consumo 
    def adicionar_consumo(self, idHospedagem ,nome, quantidade , valorUnitario):
        hospedagem = self.__buscar_hospedagem(idHospedagem)
        gasto = Gasto(nome,idHospedagem,valorUnitario,quantidade)
        self.__gasto_dao.inserir(gasto)

    def __calcular_total(self, idHospedagem, quarto, dias):
        total = 0 
        total += float(self.__gasto_dao.calcular_total(idHospedagem)) #itens
        total += quarto.calcular_diaria(dias)
        return total

    def listar_hospedagens_ativas(self):
        return list(self.__hospedagem_dao.listar()) #copia inves da original
        #for hospedagem in self.__hospedagensAtivas:
         #   print(f"{hospedagem.id}) QUARTO: {hospedagem.quarto.numeroQuarto} / CLIENTE: {hospedagem.cliente.nome}")

    def __buscar_hospedagem(self, idHospedagem):
        for hospedagem in self.__hospedagem_dao.listar():
            if hospedagem.id == idHospedagem:
                return hospedagem
        raise ValueError("Hospedagem não encontrada.")








        

