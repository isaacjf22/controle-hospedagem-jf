from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QHBoxLayout , QFormLayout, QCheckBox, QPushButton, QApplication
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt


from controllers.controlador_login  import ControladorLogin
from boudaries.gui.tela_hospedagem import TelaHospedagem

class TelaLogin(QWidget):
    def __init__(self, ctl_login, tela_hospedagem : TelaHospedagem):
        super().__init__()
        self.__ctl_login = ctl_login
        self.__tela_hospedagem = tela_hospedagem

        self.__tela_hospedagem.voltar.connect(self.reabrir)
        self.setWindowTitle("HOSPEDAGEM JF - LOGIN")
        self.setFixedSize(350,250)

    #criação dos widgets E seus respectivos layouts 
        
        
        #INICIO
        textoSaudacao = QLabel("BEM-VINDO AO HOSPEDAGEM JF")
        textoSaudacao.setStyleSheet("font-size: 15px; font-weight: bold;")
        textoSaudacao.setAlignment(Qt.AlignmentFlag.AlignCenter)
        textoLogin = QLabel("Faça seu login")
        textoLogin.setStyleSheet("font-size: 12px; color: #666;")
        textoLogin.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #MEIO
        self.linha_nome = QLineEdit()
        self.linha_senha = QLineEdit()
        self.linha_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.check_senha = QCheckBox("Mostrar")
        self.check_senha.toggled.connect(self.mostrar_senha)     

        self.linha_nome.returnPressed.connect(self.entrar) #aceitar ENTER 
        self.linha_senha.returnPressed.connect(self.entrar) 
        

        linhaSenha = QVBoxLayout()
        linhaSenha.addWidget(self.linha_senha)
        linhaSenha.addWidget(self.check_senha)
        
        layoutEntrada = QFormLayout()
        layoutEntrada.addRow("Nome:", self.linha_nome)
        layoutEntrada.addRow("Senha:", linhaSenha)

        #SAIDA
        self.entrar_botao = QPushButton("Avançar")
        self.entrar_botao.clicked.connect(self.entrar)
        self.sair_botao = QPushButton("Sair")
        self.sair_botao.clicked.connect(QApplication.quit)        

        layoutSaida = QHBoxLayout()

        layoutSaida.addWidget(self.sair_botao)
        layoutSaida.addWidget(self.entrar_botao)
        

        
        #PRINCIPAL (junta tudo)
        layoutPrincipal = QVBoxLayout(self) #a classe que comanda 
        layoutPrincipal.addWidget(textoSaudacao)
        layoutPrincipal.addWidget(textoLogin)
        layoutPrincipal.addLayout(layoutEntrada)
        layoutPrincipal.addLayout(layoutSaida)

    def mostrar_senha(self, marcado):
        if marcado:
            self.linha_senha.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.linha_senha.setEchoMode(QLineEdit.EchoMode.Password)

    def entrar(self):
        try:
            self.__ctl_login.login(self.linha_nome.text(), self.linha_senha.text()) #oq pode dar ruim 
        except ValueError as e:
            QMessageBox.critical(self, "Erro", str(e))
            return
        self.hide()
        self.__tela_hospedagem.atualizar_lista()
        self.__tela_hospedagem.show()

    def reabrir(self): #limpando os dados 
        self.__ctl_login.logout()              # limpa o funcionário logado
        self.linha_nome.clear()
        self.linha_senha.clear()
        self.check_senha.setChecked(False)     # volta a esconder a senha
        self.linha_nome.setFocus()
        self.show()
        













    

    