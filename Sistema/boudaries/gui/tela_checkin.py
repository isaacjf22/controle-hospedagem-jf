from PySide6.QtWidgets import QWidget , QTableWidget , QLabel, QAbstractItemView, QPushButton , QHBoxLayout, QVBoxLayout, QHeaderView, QMessageBox , QTableWidgetItem, QDateEdit, QFormLayout
from PySide6.QtCore import Qt, Signal, QDate
from datetime import datetime, time

from controllers.controlador_cliente import ControladorCliente
from controllers.controlador_quarto import ControladorQuarto
from controllers.controlador_hospedagem import ControladorHospedagem

from boudaries.gui.dialogo_comprovante import DialogoComprovante

from entities.status import Status

class TelaCheckin(QWidget):
    voltar = Signal()

    def __init__(self, ctl_hospedagem : ControladorHospedagem, ctl_quarto : ControladorQuarto, ctl_cliente: ControladorCliente):
        super().__init__()
        self.__ctl_hospedagem = ctl_hospedagem
        self.__ctl_quarto = ctl_quarto
        self.__ctl_cliente = ctl_cliente

        self.resize(1100,650)
        self.setMinimumSize(900,550)
        self.setWindowTitle("HOSPEDAGEM JF - CHECK-IN")

        #TOP 
        self.textoTop = QLabel("CHECK-IN")
        self.textoTop.setStyleSheet("font-size: 22px; font-weight: bold;")
        self.textoTop.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #LISTAS 
        #CLIENTE 
        layoutCliente = QVBoxLayout()

        self.textoCliente = QLabel("Cliente") 
        self.textoCliente.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.textoCliente.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.listaCliente = QTableWidget(0, 2) # quantidade de linhas e colunas ao criar 
        self.listaCliente.setHorizontalHeaderLabels(["Nome", "CPF"])
        self.listaCliente.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers) #só visualização
        self.listaCliente.verticalHeader().hide() #esconde o numero das linhas 
        self.listaCliente.setAlternatingRowColors(True) #linhas alternadas 
        self.listaCliente.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows) #seleciona linha inteira
        self.listaCliente.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection) #seleciona um de cada vez 
        self.listaCliente.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        layoutCliente.addWidget(self.textoCliente)
        layoutCliente.addWidget(self.listaCliente)

        #QUARTOS
        layoutQuarto = QVBoxLayout()

        self.textoQuarto = QLabel("Quarto") 
        self.textoQuarto.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.textoQuarto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.listaQuarto = QTableWidget(0, 2) # quantidade de linhas e colunas ao criar 
        self.listaQuarto.setHorizontalHeaderLabels(["N° Quarto", "Status"])
        self.listaQuarto.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers) #só visualização
        self.listaQuarto.verticalHeader().hide() #esconde o numero das linhas 
        self.listaQuarto.setAlternatingRowColors(True) #linhas alternadas 
        self.listaQuarto.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows) #seleciona linha inteira
        self.listaQuarto.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection) #seleciona um de cada vez
        self.listaQuarto.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        layoutQuarto.addWidget(self.textoQuarto)
        layoutQuarto.addWidget(self.listaQuarto)

        #JUNTANDO LISTAS 
        layoutListas = QHBoxLayout()
        layoutListas.addLayout(layoutCliente)
        layoutListas.addLayout(layoutQuarto)


        #OPÇÕES
        layoutBotoes = QHBoxLayout()
            #REALIZAR
        realizar = QHBoxLayout()
        self.botao_realizar = QPushButton("Realizar")
        self.botao_realizar.clicked.connect(self.realizar_checkin)

        data = QFormLayout()
        self.linha_realizar = QDateEdit(QDate.currentDate().addDays(1)) #ja tem um valor padrao
        self.linha_realizar.setCalendarPopup(True) #permite a alteração da data por meio do calendario 
        self.linha_realizar.setDisplayFormat("dd/MM/yyyy") #mostra a data com barras
        self.linha_realizar.setMinimumDate(QDate.currentDate().addDays(1)) #minimo de 1 dia 
        data.addRow("Saida prevista:", self.linha_realizar)

        realizar.addWidget(self.botao_realizar)
        realizar.addLayout(data) 
       
            #SAIDA
        self.botao_sair = QPushButton("Sair")
        self.botao_sair.clicked.connect(self.close)

            #JUNTANDO
        layoutBotoes.addLayout(realizar)
        layoutBotoes.addWidget(self.botao_sair)

        #JUNTANDO TUDO
        layoutPrincipal = QVBoxLayout(self)
        layoutPrincipal.addWidget(self.textoTop)
        layoutPrincipal.addLayout(layoutListas)
        layoutPrincipal.addLayout(layoutBotoes)

        self.preparar()


    def preparar(self):
        amanha = QDate.currentDate().addDays(1) #recalcula toda vez que a tela abre
        self.linha_realizar.setMinimumDate(amanha)
        self.linha_realizar.setDate(amanha)
        self.atualizar_clientes()
        self.atualizar_quarto()


    def closeEvent(self, event) -> None:
        self.voltar.emit()
        return super().closeEvent(event)

    def realizar_checkin(self):
        nQ = self.id_selecionado_quarto()
        idC = self.id_selecionado_cliente()
        if idC is None:
            QMessageBox.warning(self, "Aviso","Selecione um cliente")
            return
       
        if nQ is None:
            QMessageBox.warning(self, "Aviso","Selecione um quarto")
            return
        try:
            #date (só o dia) + horario de saida = datetime, o mesmo tipo da entrada
            saida = datetime.combine(self.linha_realizar.date().toPython(), time(12, 0))
            comprovante = self.__ctl_hospedagem.realizar_checkin(idC, nQ, saida)
        except ValueError as e:
            QMessageBox.critical(self, "Erro", str(e))
            return
        DialogoComprovante(str(comprovante), "COMPROVANTE HOSPEDAGEM", self).exec() #str() transforma o objeto em texto
        self.preparar()



    def atualizar_clientes(self):
        clientes = self.__ctl_cliente.listar_clientes()
        self.listaCliente.setRowCount(len(clientes)) #defininco a quantidade de linhas da tabela 
        for linha, c in enumerate(clientes):
            item_nome = QTableWidgetItem(c.nome)
            item_nome.setData(Qt.ItemDataRole.UserRole, c.id)
            self.listaCliente.setItem(linha, 0 , item_nome)
            self.listaCliente.setItem(linha, 1, QTableWidgetItem(c.cpf_formatado))

    def atualizar_quarto(self):
        livres = [q for q in self.__ctl_quarto.listar_quartos()
                if q.statusQuarto == Status.LIVRE]
        self.listaQuarto.setRowCount(len(livres))
        for linha, q in enumerate(livres):
            item_numero = QTableWidgetItem(str(q.numeroQuarto))
            item_numero.setData(Qt.ItemDataRole.UserRole, q.numeroQuarto)
            self.listaQuarto.setItem(linha, 0, item_numero)
            self.listaQuarto.setItem(linha, 1, QTableWidgetItem(q.statusQuarto.value))

    def id_selecionado_cliente(self):
        linha = self.listaCliente.currentRow()
        if linha < 0:
            return None
        item = self.listaCliente.item(linha, 0)
        if item is not None:
            return item.data(Qt.ItemDataRole.UserRole)

    def id_selecionado_quarto(self):
        linha = self.listaQuarto.currentRow() 
        if linha < 0:
            return None
        item = self.listaQuarto.item(linha, 0)
        if item is not None:
            return item.data(Qt.ItemDataRole.UserRole)