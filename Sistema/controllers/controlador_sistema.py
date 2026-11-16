import os
import sys
from dotenv import load_dotenv
from PySide6.QtWidgets import QApplication

#telas
from boudaries.gui.tela_login import TelaLogin
from boudaries.gui.tela_hospedagem import TelaHospedagem
from boudaries.gui.tela_cliente import TelaCliente
from boudaries.gui.tela_funcionarios import TelaFuncionario
from boudaries.gui.tela_checkin import TelaCheckin
from boudaries.gui.tela_limpeza import TelaLimpeza

#controladores
from controllers.controlador_funcionario import ControladorFuncionario
from controllers.controlador_login import ControladorLogin
from controllers.controlador_hospedagem import ControladorHospedagem
from controllers.controlador_cliente import ControladorCliente
from controllers.controlador_quarto import ControladorQuarto

#DAO
from dao.quarto_dao import QuartoDAO
from dao.cliente_dao import ClienteDAO
from dao.gasto_dao import GastoDAO
from dao.hospedagem_dao import HospedagemDAO
from dao.funcionario_dao import FuncionarioDAO


class ControladorSistema:
    def __init__(self):
        load_dotenv()

        
        self.__app = QApplication(sys.argv)

        # DAOs e controladores
        dao_quarto = QuartoDAO()
        dao_cliente = ClienteDAO()
        dao_gasto = GastoDAO()
        dao_hospedagem = HospedagemDAO(dao_cliente, dao_quarto)
        dao_funcionario = FuncionarioDAO()

        ctl_cliente = ControladorCliente(dao_cliente)
        ctl_quarto = ControladorQuarto(dao_quarto)
        ctl_hospedagem = ControladorHospedagem(ctl_cliente, ctl_quarto, dao_hospedagem, dao_gasto)
        ctl_funcionario = ControladorFuncionario(dao_funcionario)
        ctl_login = ControladorLogin(ctl_funcionario)

        senha = os.getenv("ADMIN_SENHA")
        if not senha:
            sys.exit("Defina ADMIN_NOME, ADMIN_CPF e ADMIN_SENHA no .env antes do primeiro acesso.")
        ctl_funcionario.garantir_primeiro_acesso(
            os.getenv("ADMIN_NOME"), os.getenv("ADMIN_CPF"), senha
        )

        tela_cliente = TelaCliente(ctl_cliente)
        tela_funcionario = TelaFuncionario(ctl_funcionario, ctl_login)
        tela_checkin = TelaCheckin(ctl_hospedagem, ctl_quarto, ctl_cliente)
        tela_limpeza = TelaLimpeza(ctl_quarto)
        tela_hospedagem = TelaHospedagem(ctl_hospedagem, tela_cliente, tela_funcionario,
                                         tela_checkin, tela_limpeza)
        self.__tela_login = TelaLogin(ctl_login, tela_hospedagem)

    def inicio(self):
        self.__tela_login.show()
        sys.exit(self.__app.exec())     #loop da aplicação