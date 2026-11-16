from PySide6.QtGui import QFontDatabase, QGuiApplication
from PySide6.QtWidgets import QDialog, QPlainTextEdit, QPushButton, QHBoxLayout, QVBoxLayout


class DialogoComprovante(QDialog):
    def __init__(self, texto, titulo="COMPROVANTE", parent=None):
        super().__init__(parent)
        self.setWindowTitle(titulo)
        self.setModal(True)
        self.resize(480, 420)

        self.caixa = QPlainTextEdit(texto)
        self.caixa.setReadOnly(True)
        self.caixa.setFont(QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont))

        botao_copiar = QPushButton("Copiar")
        botao_copiar.clicked.connect(self.copiar)
        botao_fechar = QPushButton("Fechar")
        botao_fechar.setDefault(True)
        botao_fechar.clicked.connect(self.accept)

        botoes = QHBoxLayout()
        botoes.addStretch()
        botoes.addWidget(botao_copiar)
        botoes.addWidget(botao_fechar)

        layout = QVBoxLayout(self)
        layout.addWidget(self.caixa)
        layout.addLayout(botoes)

    def copiar(self):
        QGuiApplication.clipboard().setText(self.caixa.toPlainText())