from entities.pessoas.cliente import Cliente
from dao.cliente_dao import ClienteDAO

class ControladorCliente:
    def __init__(self, cliente_dao : ClienteDAO):
        self.__cliente_dao = cliente_dao

    def cadastrar_cliente(self, nome , cpf) -> None:
        cliente = Cliente(nome , cpf)
        clientes = self.__cliente_dao.listar()
        if any(c.cpf == cliente.cpf for c in clientes):
            raise ValueError("CPF já cadastrado.")
        self.__cliente_dao.cadastrar(cliente)

    def remover_cliente(self, id) -> None:
        cliente = self.buscar_cliente(id)
        self.__cliente_dao.remover(id)

    def atualizar_cliente(self, id ,nome=None):
        cliente = self.buscar_cliente(id)
        if nome is not None: #se o nome tem algum valor
            cliente.nome = nome
            self.__cliente_dao.atualizar(id, nome)

    def listar_clientes(self):
        return list(self.__cliente_dao.listar()) #manda uma copia inves da referencia
        #for cliente in self.__clientes:
            #print(f"{cliente.id}) {cliente.nome} - [{cliente.cpf}]")

    def buscar_cliente(self, id):
        cliente = self.__cliente_dao.buscar_id(id)
        if cliente is None:
            raise ValueError("Cliente não encontrado.")
        return cliente
