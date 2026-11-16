from PySide6.QtWidgets import (
    QDialog, QLabel, QLineEdit, QSpinBox, QDoubleSpinBox, QDialogButtonBox, QFormLayout, QVBoxLayout, QMessageBox
)

from controllers.controlador_hospedagem import ControladorHospedagem


class DialogoConsumo(QDialog):
    def __init__(self, ctl_hospedagem: ControladorHospedagem, id_hospedagem, resumo, parent=None):
        super().__init__(parent)
        self.__ctl_hospedagem = ctl_hospedagem
        self.__id_hospedagem = id_hospedagem          # hospedagem escolhida na lista

        self.setWindowTitle("ADICIONAR CONSUMO")
        self.setModal(True)
        self.setMinimumWidth(380)

        #TOPO: mostra em qual hospedagem o consumo vai entrar
        self.textoTop = QLabel(resumo)                 # ex.: "Maria Souza - Quarto 11"
        self.textoTop.setStyleSheet("font-size: 16px; font-weight: bold;")

        #CAMPOS
        self.campo_produto = QLineEdit()
        self.campo_produto.setPlaceholderText("Ex.: Água, Refrigerante, Lavanderia")
        self.campo_produto.setMaxLength(30)   #mesmo tamanho da coluna no banco

        self.campo_quantidade = QSpinBox()
        self.campo_quantidade.setRange(1, 999)

        self.campo_valor = QDoubleSpinBox()
        self.campo_valor.setPrefix("R$ ")
        self.campo_valor.setDecimals(2)
        self.campo_valor.setRange(0.01, 100000.00)
        self.campo_valor.setSingleStep(1.00)

        #total calculado na hora, só para o usuário conferir
        self.texto_total = QLabel()
        self.texto_total.setStyleSheet("font-weight: bold;")
        self.campo_quantidade.valueChanged.connect(self.atualizar_total)
        self.campo_valor.valueChanged.connect(self.atualizar_total)
        self.atualizar_total()

        formulario = QFormLayout()
        formulario.addRow("Produto:", self.campo_produto)
        formulario.addRow("Quantidade:", self.campo_quantidade)
        formulario.addRow("Valor unitário:", self.campo_valor)
        formulario.addRow("Total:", self.texto_total)

        #BOTÕES
        botoes = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        botoes.button(QDialogButtonBox.StandardButton.Ok).setText("Adicionar")
        botoes.button(QDialogButtonBox.StandardButton.Cancel).setText("Cancelar")
        botoes.accepted.connect(self.salvar)
        botoes.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addWidget(self.textoTop)
        layout.addLayout(formulario)
        layout.addWidget(botoes)

        self.campo_produto.setFocus()

    def atualizar_total(self):
        total = self.campo_quantidade.value() * self.campo_valor.value()
        self.texto_total.setText(f"R$ {total:.2f}")

    def salvar(self):
        try:
            self.__ctl_hospedagem.adicionar_consumo(
                self.__id_hospedagem,
                self.campo_produto.text().strip(),
                self.campo_quantidade.value(),
                self.campo_valor.value(),
            )
        except ValueError as e:
            QMessageBox.critical(self, "Erro", str(e))
            return                                      # continua aberto para corrigir
        self.accept()