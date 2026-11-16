from PySide6.QtWidgets import QWidget , QTableWidget , QLabel, QAbstractItemView, QPushButton , QHBoxLayout, QVBoxLayout, QHeaderView, QMessageBox , QTableWidgetItem
from PySide6.QtCore import Qt, Signal

from boudaries.gui.dialogo_cliente import DialogoCliente

from controllers.controlador_cliente import ControladorCliente




class TelaCliente(QWidget):
    voltar = Signal() #sinais do q ocorre nessa janela , criação de um connect 

    def __init__(self, ctl_cliente : ControladorCliente):
        super().__init__()
        self.__ctl_cliente = ctl_cliente
        self.resize(1100,650)
        self.setMinimumSize(900,550)
        self.setWindowTitle("HOSPEDAGEM JF - GERENCIAMENTO CLIENTES")
        
        #TOP
        self.textoTop = QLabel("GERENCIAMENTO CLIENTES")
        self.textoTop.setStyleSheet("font-size: 22px; font-weight: bold;")
        self.textoTop.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        #LISTA
        self.lista = QTableWidget(0, 2) # quantidade de linhas e colunas ao criar 
        self.lista.setHorizontalHeaderLabels(["Nome", "CPF"])
        self.lista.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers) #só visualização
        self.lista.verticalHeader().hide() #esconde o numero das linhas 
        self.lista.setAlternatingRowColors(True) #linhas alternadas 
        self.lista.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch) #expande a lista 
        self.lista.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows) #seleciona linha inteira
        self.lista.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection) #seleciona um de cada vez 

        #MEIO
        self.textoPergunta = QLabel("O que deseja fazer?")
        #OPÇÕES 
        self.botao_registrar = QPushButton("Registrar")
        self.botao_registrar.clicked.connect(self.registrar_cliente)

        self.botao_remover = QPushButton("Remover")
        self.botao_remover.clicked.connect(self.remover_cliente)


        self.botao_atualizar = QPushButton("Atualizar")
        self.botao_atualizar.clicked.connect(self.atualizar_cliente)

        self.botao_sair = QPushButton("Sair")
        self.botao_sair.clicked.connect(self.close)


        opcoes = QHBoxLayout()
        for o in (self.botao_registrar, self.botao_remover,self.botao_atualizar, self.botao_sair) :
            opcoes.addWidget(o)

        
        layoutPrincipal = QVBoxLayout(self) # referencia a classe
        layoutPrincipal.addWidget(self.textoTop)
        layoutPrincipal.addWidget(self.lista)
        layoutPrincipal.addWidget(self.textoPergunta)
        layoutPrincipal.addLayout(opcoes)

        self.atualizar_lista() 

    def registrar_cliente(self):
        diagolo = DialogoCliente(self.__ctl_cliente, self)
        if diagolo.exec(): #faz e ve condição
            self.atualizar_lista()

    def atualizar_cliente(self):
        id = self.id_selecionado()
        if id is None:
            QMessageBox.warning(self,"Aviso","Selecione um cliente")
            return
        try:
            cliente = self.__ctl_cliente.buscar_cliente(id)
        except ValueError as e:
            QMessageBox.critical(self, "Erro", str(e))
            return
        dialogo = DialogoCliente(self.__ctl_cliente,self,cliente=cliente)
        if dialogo.exec():
            self.atualizar_lista()

    def remover_cliente(self):
        id = self.id_selecionado()
        if id is None:
            QMessageBox.warning(self,"Aviso","Selecione um cliente")
            return
        resposta = QMessageBox.question(self, "Confirmar", "Remover esse cliente?")
        if resposta != QMessageBox.StandardButton.Yes:
            return
        try:
            self.__ctl_cliente.remover_cliente(id)
        except ValueError as e:
            QMessageBox.critical(self, "Erro", str(e))
            return
        self.atualizar_lista()

    def closeEvent(self, evento): #roda sempre q a janela for fechada no X e etc  #função do Qt que tornasse possivel modificar 
        self.voltar.emit()
        evento.accept() #essa função esta personalizada 


    def atualizar_lista(self):
        clientes = self.__ctl_cliente.listar_clientes()
        self.lista.setRowCount(len(clientes)) #defininco a quantidade de linhas da tabela 
        for linha, c in enumerate(clientes):
            item_nome = QTableWidgetItem(c.nome)
            item_nome.setData(Qt.ItemDataRole.UserRole, c.id)
            self.lista.setItem(linha, 0 , item_nome)
            self.lista.setItem(linha, 1, QTableWidgetItem(c.cpf_formatado))

    def id_selecionado(self):
        linha = self.lista.currentRow()
        if linha < 0:
            return None
        item = self.lista.item(linha, 0)
        if item is not None:
            return item.data(Qt.ItemDataRole.UserRole)
    




        



