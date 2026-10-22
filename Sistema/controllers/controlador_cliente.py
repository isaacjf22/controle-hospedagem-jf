from itertools import count
from entities.pessoas.cliente import Cliente

class ControladorCliente:
    def __init__(self):
        self.__clientes = []
        self.__contador = count(1)

    def cadastrar_cliente(self, nome , cpf) -> None:
        cpfFormatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        if any(c.cpf == cpfFormatado for c in self.__clientes):
            raise ValueError("CPF já cadastrado.")
        cliente = Cliente(nome , cpf, next(self.__contador))
        self.__clientes.append(cliente)

    def remover_cliente(self, id) -> None:
        cliente = self.buscar(id)
        self.__clientes.remove(cliente)

    def atualizar_cliente(self, id ,nome=None):
        cliente = self.buscar(id)
        if nome is not None: #se o nome tem algum valor
            cliente.nome = nome

    def listar_clientes(self):
        return list(self.__clientes) #manda uma copia inves da referencia
        #for cliente in self.__clientes:
            #print(f"{cliente.id}) {cliente.nome} - [{cliente.cpf}]")


    def buscar(self, id):
        for cliente in self.__clientes:
            if cliente.id == id:
                return cliente
        raise ValueError("Cliente não encontrado")

