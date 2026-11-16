from PySide6.QtWidgets import QWidget, QTableWidget, QLabel, QAbstractItemView, QPushButton, QHBoxLayout, QVBoxLayout, QHeaderView, QMessageBox, QTableWidgetItem
from PySide6.QtCore import Qt, Signal

from controllers.controlador_quarto import ControladorQuarto

from entities.status import Status


class TelaLimpeza(QWidget):
    voltar = Signal()

    def __init__(self, ctl_quarto: ControladorQuarto):
        super().__init__()
        self.__ctl_quarto = ctl_quarto
        self.resize(1100, 650)
        self.setMinimumSize(900, 550)
        self.setWindowTitle("HOSPEDAGEM JF - LIMPEZA")

        #TOP
        self.textoTop = QLabel("LIMPEZA DE QUARTOS")
        self.textoTop.setStyleSheet("font-size: 22px; font-weight: bold;")
        self.textoTop.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #LISTA
        self.lista = QTableWidget(0, 2)
        self.lista.setHorizontalHeaderLabels(["N° Quarto", "Status"])
        self.lista.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)  #só visualização
        self.lista.verticalHeader().hide()
        self.lista.setAlternatingRowColors(True)
        self.lista.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.lista.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.lista.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        #MEIO
        self.textoPergunta = QLabel("Selecione o quarto que foi limpo")

        #OPÇÕES
        self.botao_concluir = QPushButton("Concluir limpeza")
        self.botao_concluir.clicked.connect(self.concluir_limpeza)

        self.botao_sair = QPushButton("Sair")
        self.botao_sair.clicked.connect(self.close)

        opcoes = QHBoxLayout()
        for o in (self.botao_concluir, self.botao_sair):
            opcoes.addWidget(o)

        layoutPrincipal = QVBoxLayout(self)
        layoutPrincipal.addWidget(self.textoTop)
        layoutPrincipal.addWidget(self.lista)
        layoutPrincipal.addWidget(self.textoPergunta)
        layoutPrincipal.addLayout(opcoes)

        self.atualizar_lista()

    def concluir_limpeza(self):
        numero = self.numero_selecionado()
        if numero is None:
            QMessageBox.warning(self, "Aviso", "Selecione um quarto")
            return
        try:
            self.__ctl_quarto.concluir_limpeza(numero)
        except ValueError as e:
            QMessageBox.critical(self, "Erro", str(e))
            return
        self.atualizar_lista()

    def closeEvent(self, evento):
        self.voltar.emit()
        evento.accept()

    def atualizar_lista(self):
        em_limpeza = [q for q in self.__ctl_quarto.listar_quartos()
                      if q.statusQuarto == Status.LIMPEZA]
        self.lista.setRowCount(len(em_limpeza))
        for linha, q in enumerate(em_limpeza):
            item_numero = QTableWidgetItem(str(q.numeroQuarto))
            item_numero.setData(Qt.ItemDataRole.UserRole, q.numeroQuarto)
            self.lista.setItem(linha, 0, item_numero)
            self.lista.setItem(linha, 1, QTableWidgetItem(q.statusQuarto.value))

    def numero_selecionado(self):
        linha = self.lista.currentRow()
        if linha < 0:
            return None
        item = self.lista.item(linha, 0)
        if item is not None:
            return item.data(Qt.ItemDataRole.UserRole)