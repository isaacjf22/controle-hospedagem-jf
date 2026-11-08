from database.conexao import conectar 
from entities.pessoas.cliente import Cliente

class ClienteDAO:
    
    def cadastrar(self, cliente : Cliente): #cadastra o objeto no banco de dados 
        with conectar() as con: # with tenta realizar uma função , se der erro ou nao , ele fecha e volta a funcionar corretamente 
            con.execute( #executar um comando no banco de dados 
                "INSERT INTO clientes (nome,cpf) VALUES (%s,%s)", (cliente.nome, cliente.cpf)
            )
    
    def buscar_id(self, id): #busca o cliente pelo id dele 
        with conectar() as con:
            linha = con.execute(
                "SELECT id, nome , cpf FROM clientes WHERE id = %s", (id,)
            ).fetchone() 
        return self.__montar(linha) if linha else None 
    
    def listar(self):
        with conectar() as con:
            dados = con.execute(
                "SELECT id, nome, cpf FROM clientes ORDER BY id"
            ).fetchall()

        lista = []
        for dado in dados:
            cliente = self.__montar(dado)
            lista.append(cliente)

        return lista #retorna lista de clientes do banco de dados 

    def atualizar(self, id, nome):
        with conectar() as con:
            con.execute(
                "UPDATE clientes SET nome = %s WHERE id = %s", (nome, id)
            )

    def remover(self, id):
        with conectar() as con:
            con.execute(
                "DELETE FROM clientes WHERE id = %s" , (id,)
            )

    def __montar(self, retorno): #transforma o dado em objeto 
        return Cliente(nome=retorno[1], cpf=retorno[2], id=retorno[0])
    
