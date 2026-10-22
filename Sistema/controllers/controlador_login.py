from controllers.controlador_funcionario import ControladorFuncionario

class ControladorLogin:
    def __init__(self, ctlFuncionario : ControladorFuncionario):
        self.__funcionarioLogado = None
        self.__ctlFuncionario = ctlFuncionario

    #encapsulamento
    @property
    def funcionarioLogado(self):
        return self.__funcionarioLogado

    #métodos
    def login(self, nome, senha) -> None:
        funcionario = self.__ctlFuncionario.buscar(nome=nome) #pulando parametros
        if not funcionario.verificar_senha(senha):
            raise ValueError("Senha incorreta.")
        self.__funcionarioLogado = funcionario

    def logout(self) -> None:
        self.__funcionarioLogado = None



