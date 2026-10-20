from itertools import count
from entities.pessoas.funcionario import Funcionario

class ControladorFuncionario:
    def __init__(self):
        self.__funcionarios = []
        self.__id = count(1)

    def cadastrar_funcionario(self, nome , cpf, senha) -> None:
        funcionario = Funcionario(nome, cpf, next(self.__id), senha )
        self.__funcionarios.append(funcionario) #adicionando o funcioanrio na lista de cadastrados

    def remover_funcionario(self, id) -> None:
        funcionario = self.buscar(id) #ira buscar e apagar
        self.__funcionarios.remove(funcionario)

    def atualizar_funcionario(self, id, nome=None, senha=None) -> None:
        funcionario = self.buscar(id)
        if nome is not None:
            funcionario.nome = nome
        if senha is not None:
            funcionario.alterar_senha(senha)

    def buscar(self, id=None, nome=None) -> Funcionario:
        for funcionario in self.__funcionarios:
            if id is not None:
                if funcionario.id == id:
                    return funcionario
            if nome is not None:
                if funcionario.nome == nome:
                    return funcionario
        raise ValueError("Funcionário não encontrado.")

    def listar_funcionarios(self) -> None:
        for funcionario in self.__funcionarios:
            print(f"{funcionario.id}) {funcionario.nome} - [{funcionario.cpf}]")

