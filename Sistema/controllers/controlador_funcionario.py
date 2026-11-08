from entities.pessoas.funcionario import Funcionario

class ControladorFuncionario:
    def __init__(self):
        self.__funcionarios = []

    def cadastrar_funcionario(self, nome , cpf, senha) -> None:
        cpfFormatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        if any(c.cpf == cpfFormatado for c in self.__funcionarios): #condição e como
            raise ValueError("CPF já cadastrado.")
        if any(f.nome == nome.strip() for f in self.__funcionarios):
            raise ValueError("Já existe funcionário registrado com esse nome.")
        funcionario = Funcionario(nome, cpf, senha )
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

    def listar_funcionarios(self):
        return list(self.__funcionarios) #copia inves do original
        #for funcionario in self.__funcionarios:
         #   print(f"{funcionario.id}) {funcionario.nome} - [{funcionario.cpf}]")

