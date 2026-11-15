from PySide6.QtWidgets import QWidget , QTableWidget , QLabel, QAbstractItemView, QPushButton , QHBoxLayout, QVBoxLayout, QHeaderView, QDialog, QLineEdit, QCheckBox, QFormLayout, QDialogButtonBox, QMessageBox
from controllers.controlador_funcionario import ControladorFuncionario
from entities.pessoas.cliente import Cliente
from controllers.controlador_cliente import ControladorCliente


class DialogoCliente(QDialog):
    def __init__(self, ctl_cliente : ControladorCliente , parent=None, cliente: Cliente | None = None):
        super().__init__(parent) #vai puxar caracteristicas da tela q abriu
        self.__ctl_cliente = ctl_cliente
        self.__cliente = cliente
        self.__editando = cliente is not None #condição de existencia 

        self.setWindowTitle("ATUALIZANDO" if self.__editando else "REGISTRANDO")
        self.setModal(True) #pausa a janela anterior
        self.setFixedSize(340, 140)

        #entradas
        self.linha_nome = QLineEdit()

        self.linha_cpf = QLineEdit()
        self.linha_cpf.setMaxLength(11)

        if cliente is not None:
            self.linha_nome.setText(cliente.nome)
            self.linha_cpf.setText(cliente.cpf)
            self.linha_cpf.setReadOnly(True) 

        formulario = QFormLayout()
        formulario.addRow("Nome:", self.linha_nome)
        formulario.addRow("CPF (sem formatação):", self.linha_cpf)

        botoes = QDialogButtonBox(QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel) #criando botoes do dialogue box

        botoes.button(QDialogButtonBox.StandardButton.Save).setText("Salvar")
        botoes.button(QDialogButtonBox.StandardButton.Cancel).setText("Cancelar")
        botoes.accepted.connect(self.salvar)
        botoes.rejected.connect(self.reject)

        layoutPrincipal = QVBoxLayout(self)
        layoutPrincipal.addLayout(formulario)
        layoutPrincipal.addWidget(botoes)

    def salvar(self):
        nome = self.linha_nome.text().strip() #retirando espaços da entrada
        cpf = self.linha_cpf.text().strip()
        try:
            if self.__editando and self.__cliente is not None:
                self.__ctl_cliente.atualizar_cliente(self.__cliente.id, nome=nome)
            else:
                self.__ctl_cliente.cadastrar_cliente(nome, cpf)
        except ValueError as e:
            QMessageBox.critical(self, "Erro", str(e))
            return
        self.accept() #finaliza a função accept do salvar botao


    