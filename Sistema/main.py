
from controllers.controlador_funcionario import ControladorFuncionario
from controllers.controlador_login import ControladorLogin




from boudaries.fronteira_realizar_login import RealizarLogin

#controladores 
ctl_fun = ControladorFuncionario()
ctl_login = ControladorLogin(ctl_fun)


#fronteiras 
fronteira_login = RealizarLogin(ctl_login,ctl_fun)






def main():
    fronteira_login.mostrar_menu()









if __name__ == "__main__" : 
    main()