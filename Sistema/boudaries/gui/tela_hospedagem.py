from PySide6.QtWidgets import QWidget , QTableWidget , QLabel, QAbstractItemView, QPushButton , QHBoxLayout, QVBoxLayout, QHeaderView, QMessageBox , QTableWidgetItem
from PySide6.QtCore import Qt, Signal

from controllers.controlador_hospedagem import ControladorHospedagem

from boudaries.gui.tela_cliente import TelaCliente
from boudaries.gui.tela_funcionarios import TelaFuncionario
from boudaries.gui.tela_checkin import TelaCheckin
from boudaries.gui.tela_limpeza import TelaLimpeza
from boudaries.gui.dialogo_comprovante import DialogoComprovante

class TelaHospedagem(QWidget):
    def __init__(self, ctl_hospedagem : ControladorHospedagem, tela_cliente : TelaCliente, tela_funcionario : TelaFuncionario, tela_checkin : TelaCheckin, tela_limpeza : TelaLimpeza):
        self.__ctl_hospedagem = ctl_hospedagem
        self.__tela_cliente = tela_cliente
        self.__tela_funcionario = tela_funcionario
        self.__tela_checkin = tela_checkin
        self.__tela_limpeza = tela_limpeza

        self.__tela_cliente.voltar.connect(self.show)
        self.__tela_funcionario.voltar.connect(self.show)
        self.__tela_checkin.voltar.connect(self.show)
        self.__tela_limpeza.voltar.connect(self.show)

        self.resize(1100,650)
        self.setMinimumSize(900,550)
        self.setWindowTitle("HOSPEDAGEM JF - GERENCIAMENTO HOSPEDAGEM")

        #TOP
        self.textoTop = QLabel("GERENCIAMENTO HOSPEDAGEM")
        self.textoTop.setStyleSheet("font-size: 22px; font-weight: bold;")
        self.textoTop.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #LISTA
        layoutLista = QVBoxLayout()
        self.listaNome = QLabel("Hospedagens Ativas")
        self.listaNome.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.listaNome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lista = QTableWidget(0, 4) # quantidade de linhas e colunas ao criar 
        self.lista.setHorizontalHeaderLabels(["Cliente", "Quarto", "Entrada", "Saída prevista"])
        self.lista.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers) #só visualização
        self.lista.verticalHeader().hide() #esconde o numero das linhas 
        self.lista.setAlternatingRowColors(True) #linhas alternadas 
        self.lista.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch) #expande a lista 
        self.lista.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows) #seleciona linha inteira
        self.lista.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection) #seleciona um de cada vez 

        layoutLista.addWidget(self.listaNome)
        layoutLista.addWidget(self.lista)
        
        
        #MEIO
        self.textoPergunta = QLabel("O que deseja fazer?")

        #OPÇÕES
        layoutBotoes = QHBoxLayout()
        self.botao_checkin = QPushButton("Check-in") #Janela
        self.botao_checkin.clicked.connect(self.abrir_checkin)

        self.botao_checkout = QPushButton("Check-out") #Botao
        self.botao_checkout.clicked.connect(self.realizar_checkout)


        self.botao_limpeza = QPushButton("Concluir Limpeza") #DialogueBox
        self.botao_limpeza.clicked.connect(self.abrir_limepeza)

        self.botao_consumo = QPushButton("Adicionar Consumo") #DialogueBox

        self.botao_clientes = QPushButton("Clientes") #Janela 
        self.botao_clientes.clicked.connect(self.abrir_cliente)

        self.botao_funcionarios = QPushButton("Funcionários") #Janela 
        self.botao_funcionarios.clicked.connect(self.abrir_funcionario)

        self.botao_sair = QPushButton("Sair")

        for b in (self.botao_checkin, self.botao_checkout, self.botao_limpeza, self.botao_consumo, self.botao_clientes, self.botao_funcionarios , self.botao_sair):
            layoutBotoes.addWidget(b)

        #JUNTANDO
        layoutPrincipal = QVBoxLayout(self)
        layoutPrincipal.addWidget(self.textoTop)
        layoutPrincipal.addLayout(layoutLista)
        layoutPrincipal.addWidget(self.textoPergunta)
        layoutPrincipal.addLayout(layoutBotoes)




    def atualizar_lista(self):
        hospedagens = self.__ctl_hospedagem.listar_hospedagens_ativas()
        self.lista.setRowCount(len(hospedagens))
        for linha, h in enumerate(hospedagens):
            item_cliente = QTableWidgetItem(h.cliente.nome)
            item_cliente.setData(Qt.ItemDataRole.UserRole, h.id)     # id da hospedagem
            self.lista.setItem(linha, 0, item_cliente)
            self.lista.setItem(linha, 1, QTableWidgetItem(str(h.quarto.numeroQuarto)))
            self.lista.setItem(linha, 2, QTableWidgetItem(h.entrada.strftime("%d/%m/%Y %H:%M")))
            self.lista.setItem(linha, 3, QTableWidgetItem(h.saidaPrevista.strftime("%d/%m/%Y")))

    def realizar_checkout(self):
        id = self.id_selecionado()
        if id is None:
            QMessageBox.warning(self,"Aviso","Selecione uma hospedagem ativa")
        try:
            extrato = self.__ctl_hospedagem.realizar_checkout(id)
            DialogoComprovante(extrato, "EXTRATO DE CONTA", self).exec()
            self.atualizar_lista()
        except ValueError as e:
            QMessageBox.critical(self,"Erro",str(e))
            return

    def abrir_checkin(self):
        self.hide()
        self.__tela_checkin.preparar()
        self.__tela_checkin.show()

    def abrir_limepeza(self):
        self.hide()
        self.__tela_limpeza.atualizar_lista()
        self.__tela_limpeza.show()



    def abrir_cliente(self):
        self.hide()
        self.__tela_cliente.atualizar_lista()
        self.__tela_cliente.show()

    def abrir_funcionario(self):
        self.hide()
        self.__tela_funcionario.atualizar_lista()
        self.__tela_funcionario.show()

    def id_selecionado(self):
        id = self.lista.currentRow()
        if id < 0 : 
            return None
        item = self.lista.item(id, 0)
        if item is not None:
            return item.data(Qt.ItemDataRole.UserRole)

    

    