from PySide6.QtWidgets import QWidget , QTableWidget , QLabel, QAbstractItemView, QPushButton , QHBoxLayout, QVBoxLayout, QHeaderView, QMessageBox , QTableWidgetItem
from PySide6.QtCore import Qt, Signal

from boudaries.gui.dialogo_funcionario import DialogoFuncionario




class TelaFuncionario(QWidget):
    voltar = Signal() #sinais do q ocorre nessa janela 

    def __init__(self, ctl_funcionario, ctl_login):
        super().__init__()
        self.__ctl_funcionario = ctl_funcionario
        self.__ctl_login = ctl_login #para saber quem esta logado
        self.resize(1100,650)
        self.setMinimumSize(900,550)
        self.setWindowTitle("HOSPEDAGEM JF - GERENCIAMENTO FUNCIONÁRIOS")
        
        #TOP
        self.textoTop = QLabel("GERENCIAMENTO FUNCIONÁRIOS")
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
        self.botao_registrar.clicked.connect(self.registrar_funcionario)

        self.botao_remover = QPushButton("Remover")
        self.botao_remover.clicked.connect(self.remover_funcionario)


        self.botao_atualizar = QPushButton("Atualizar")
        self.botao_atualizar.clicked.connect(self.atualizar_funcionario)

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

    def registrar_funcionario(self):
        diagolo = DialogoFuncionario(self.__ctl_funcionario, self)
        if diagolo.exec(): #faz e ve condição
            self.atualizar_lista()

    def atualizar_funcionario(self):
        id = self.id_selecionado()
        if id is None:
            QMessageBox.warning(self,"Aviso","Selecione um funcionário")
            return
        try:
            funcionario = self.__ctl_funcionario.buscar(id)
        except ValueError as e:
            QMessageBox.critical(self, "Erro", str(e))
            return
        dialogo = DialogoFuncionario(self.__ctl_funcionario,self,funcionario=funcionario)
        if dialogo.exec():
            self.atualizar_lista()

    def remover_funcionario(self):
        id = self.id_selecionado()
        if id is None:
            QMessageBox.warning(self,"Aviso","Selecione um funcionário")
            return
        logado = self.__ctl_login.funcionarioLogado
        if logado is not None and logado.id == id:
            QMessageBox.warning(self, "Aviso", "Você não pode remover o próprio usuário.")
            return
        resposta = QMessageBox.question(self, "Confirmar", "Remover esse funcionário?")
        if resposta != QMessageBox.StandardButton.Yes:
            return
        try:
            self.__ctl_funcionario.remover_funcionario(id)
        except ValueError as e:
            QMessageBox.critical(self, "Erro", str(e))
            return
        self.atualizar_lista()

    def closeEvent(self, evento): #roda sempre q a janela for fechada no X e etc  #função do Qt que tornasse possivel modificar 
        self.voltar.emit()
        evento.accept()


    def atualizar_lista(self):
        funcionarios = self.__ctl_funcionario.listar_funcionarios()
        self.lista.setRowCount(len(funcionarios)) #defininco a quantidade de linhas da tabela 
        for linha, f in enumerate(funcionarios):
            item_nome = QTableWidgetItem(f.nome)
            item_nome.setData(Qt.ItemDataRole.UserRole, f.id)
            self.lista.setItem(linha, 0 , item_nome)
            self.lista.setItem(linha, 1, QTableWidgetItem(f.cpf_formatado))

    def id_selecionado(self):
        linha = self.lista.currentRow()
        if linha < 0:
            return None
        item = self.lista.item(linha, 0)
        if item is not None:
            return item.data(Qt.ItemDataRole.UserRole)
    




        



