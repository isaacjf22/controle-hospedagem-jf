from PySide6.QtWidgets import QWidget , QTableWidget , QLabel, QAbstractItemView, QPushButton , QHBoxLayout, QVBoxLayout, QHeaderView, QDialog, QLineEdit, QCheckBox, QFormLayout, QDialogButtonBox, QMessageBox
from controllers.controlador_funcionario import ControladorFuncionario
from entities.pessoas.funcionario import Funcionario


class DialogoFuncionario(QDialog):
    def __init__(self, ctl_funcionario , parent=None, funcionario: Funcionario | None = None):
        super().__init__(parent) #vai puxar caracteristicas da tela q abriu
        self.__ctl_funcionario = ctl_funcionario
        self.__funcionario = funcionario
        self.__editando = funcionario is not None #condição de existencia 

        self.setWindowTitle("ATUALIZANDO" if self.__editando else "REGISTRANDO")
        self.setModal(True) #pausa a janela anterior
        self.setFixedSize(340, 190)

        #entradas
        self.linha_nome = QLineEdit()

        self.linha_cpf = QLineEdit()
        self.linha_cpf.setMaxLength(11)

        self.linha_senha = QLineEdit()
        self.linha_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.check_senha = QCheckBox("Mostrar")
        self.check_senha.toggled.connect(self.mostrar_senha)
        layoutSenha = QHBoxLayout()
        layoutSenha.addWidget(self.linha_senha)
        layoutSenha.addWidget(self.check_senha)

        if funcionario is not None:
            self.linha_nome.setText(funcionario.nome)
            self.linha_cpf.setText(funcionario.cpf)
            self.linha_cpf.setReadOnly(True) 

        formulario = QFormLayout()
        formulario.addRow("Nome:", self.linha_nome)
        formulario.addRow("CPF (sem formatação):", self.linha_cpf)
        formulario.addRow("Senha:",layoutSenha)

        botoes = QDialogButtonBox(QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel) #criando botoes do dialogue box

        botoes.button(QDialogButtonBox.StandardButton.Save).setText("Salvar")
        botoes.button(QDialogButtonBox.StandardButton.Cancel).setText("Cancelar")
        botoes.accepted.connect(self.salvar)
        botoes.rejected.connect(self.rejected)
        


        layoutPrincipal = QVBoxLayout(self)
        layoutPrincipal.addLayout(formulario)
        layoutPrincipal.addWidget(botoes)

    def salvar(self):
        nome = self.linha_nome.text().strip() #retirando espaços da entrada
        cpf = self.linha_cpf.text().strip()
        senha = self.linha_senha.text()
        try:
            if self.__editando and self.__funcionario is not None:
                self.__ctl_funcionario.atualizar_funcionario(self.__funcionario.id ,nome, cpf, senha)
            else:
                self.__ctl_funcionario.cadastrar_funcionario(nome, cpf, senha)
        except ValueError as e:
            QMessageBox.critical(self, "Erro", str(e))
            return
        self.accept() #finaliza a função accept do salvar botao

    def mostrar_senha(self, marcado):
            if marcado:
                self.linha_senha.setEchoMode(QLineEdit.EchoMode.Normal)
            else:
                self.linha_senha.setEchoMode(QLineEdit.EchoMode.Password)



    