import os
from dotenv import load_dotenv


#fronteiras 
from boudaries.fronteira_realizar_login import RealizarLogin
from boudaries.fronteira_hospedagem import RealizarHospedagem


#controlador 
from controllers.controlador_funcionario import ControladorFuncionario
from controllers.controlador_login import ControladorLogin
from controllers.controlador_hospedagem import ControladorHospedagem
from controllers.controlador_cliente import ControladorCliente
from controllers.controlador_quarto import ControladorQuarto

#DAO data acess object
from dao.quarto_dao import QuartoDAO
from dao.cliente_dao import ClienteDAO
from dao.gasto_dao import GastoDAO
from dao.hospedagem_dao import HospedagemDAO
from dao.funcionario_dao import FuncionarioDAO



#instanciações 
dao_quarto = QuartoDAO()
dao_cliente = ClienteDAO()
dao_gasto = GastoDAO()
dao_hospedagem = HospedagemDAO(dao_cliente,dao_quarto)
dao_funcionario = FuncionarioDAO()
ctl_cliente = ControladorCliente(dao_cliente)
ctl_quarto = ControladorQuarto(dao_quarto)
ctl_hospedagem = ControladorHospedagem(ctl_cliente, ctl_quarto, dao_hospedagem, dao_gasto)
ctl_funcionario = ControladorFuncionario(dao_funcionario)
ctl_login = ControladorLogin(ctl_funcionario)
f_realizar_login = RealizarLogin(ctl_login)
f_realizar_hospedagem = RealizarHospedagem(ctl_hospedagem, ctl_cliente, ctl_quarto,ctl_funcionario)

class ControladorSistema:
    def __init__(self):
        self.__ctl_login = ctl_login
        self.__f_realizar_login = f_realizar_login
        self.__f_realizar_hospedagem = f_realizar_hospedagem

        load_dotenv()

        senha = os.getenv("ADMIN_SENHA") #fora para realizar condicional 
        if not senha:
            print("Define uma senha para o admin no .env, como primeiro acesso.")
            
        ctl_funcionario.garantir_primeiro_acesso(
            os.getenv("ADMIN_NOME"),os.getenv("ADMIN_CPF"),senha
        )

    def inicio(self):
        while True: 
            self.__f_realizar_login.mostrar_menu()
            if self.__ctl_login.funcionarioLogado is None:
                break #significa que saiu do sistema 
            self.__f_realizar_hospedagem.mostrar_menu()
            self.__ctl_login.logout()




        