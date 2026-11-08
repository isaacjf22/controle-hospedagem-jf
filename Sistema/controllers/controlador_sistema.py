#fronteiras 
from boudaries.fronteira_realizar_login import RealizarLogin
from boudaries.fronteira_hospedagem import RealizarHospedagem


#controlador 
from controllers.controlador_funcionario import ControladorFuncionario
from controllers.controlador_login import ControladorLogin
from controllers.controlador_hospedagem import ControladorHospedagem
from controllers.controlador_cliente import ControladorCliente
from controllers.controlador_quarto import ControladorQuarto



#instanciações 
ctl_cliente = ControladorCliente()
ctl_quarto = ControladorQuarto()
ctl_hospedagem = ControladorHospedagem(ctl_cliente, ctl_quarto)
ctl_funcionario = ControladorFuncionario()
ctl_login = ControladorLogin(ctl_funcionario)
f_realizar_login = RealizarLogin(ctl_login)
f_realizar_hospedagem = RealizarHospedagem(ctl_hospedagem, ctl_cliente, ctl_quarto,ctl_funcionario)

class ControladorSistema:
    def __init__(self):
        self.__ctl_login = ctl_login
        self.__f_realizar_login = f_realizar_login
        self.__f_realizar_hospedagem = f_realizar_hospedagem

    def inicio(self):
        while True: 
            self.__f_realizar_login.mostrar_menu()
            if self.__ctl_login.funcionarioLogado is None:
                break #significa que saiu do sistema 
            self.__f_realizar_hospedagem.mostrar_menu()
            self.__ctl_login.logout()




        