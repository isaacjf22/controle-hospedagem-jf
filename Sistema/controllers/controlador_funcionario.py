from entities.pessoas.funcionario import Funcionario
from dao.funcionario_dao import FuncionarioDAO

class ControladorFuncionario:
    def __init__(self, funcionario_dao : FuncionarioDAO):
        self.__funcionario_dao = funcionario_dao
        

    def cadastrar_funcionario(self, nome , cpf, senha) -> None:
        funcionario = Funcionario(nome, cpf, senha)
        funcionarios = self.__funcionario_dao.listar()
        if any(c.cpf == funcionario.cpf for c in funcionarios): #condição e como
            raise ValueError("CPF já cadastrado.")
        if any(f.nome == funcionario.nome for f in funcionarios):
            raise ValueError("Já existe funcionário registrado com esse nome.")
        self.__funcionario_dao.inserir(funcionario)
        

    def remover_funcionario(self, id) -> None:
        funcionario = self.buscar(id) #ira buscar e verificar a existencia 
        if (len(self.__funcionario_dao.listar()) == 1):
            raise ValueError("Não pode apagar o único funcionário do sistema.")
        self.__funcionario_dao.remover(id)

    def atualizar_funcionario(self, id, nome=None, senha=None) -> None:
        funcionario = self.buscar(id) # verifica se existe
        if nome is not None:
            funcionario.nome = nome
            self.__funcionario_dao.atualizar_nome(nome, id)
        if senha is not None:
            novo = funcionario.alterar_senha(senha)
            self.__funcionario_dao.atualizar_senha(novo,id)

    def buscar(self, id=None, nome=None) -> Funcionario:
        for funcionario in self.__funcionario_dao.listar():
            if id is not None:
                if funcionario.id == id:
                    return funcionario
            if nome is not None:
                if funcionario.nome == nome:
                    return funcionario
        raise ValueError("Funcionário não encontrado.")

    def listar_funcionarios(self):
        return list(self.__funcionario_dao.listar()) #copia inves do original
        #for funcionario in self.__funcionarios:
         #   print(f"{funcionario.id}) {funcionario.nome} - [{funcionario.cpf}]")

    def garantir_primeiro_acesso(self, nome, cpf, senha):
        if not self.__funcionario_dao.listar(): #se n tiver ninguem 
            self.__funcionario_dao.inserir(Funcionario(nome,cpf,senha))



