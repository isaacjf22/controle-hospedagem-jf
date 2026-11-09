from entities.pessoas.funcionario import Funcionario
from database.conexao import conectar

class FuncionarioDAO: 

    def inserir(self, funcionario : Funcionario):
        with conectar() as con:
            con.execute(
                "INSERT INTO funcionarios (nome, cpf, senha_hash) VALUES (%s, %s, %s)",(funcionario.nome, funcionario.cpf, funcionario.senha)
            )

    def buscar_id(self, id):
        with conectar() as con:
            funcionario = con.execute(
                "SELECT id, nome , cpf , senha_hash FROM funcionarios WHERE id = %s", (id,)
            ).fetchone()
        return self.__montar(funcionario) if funcionario else None

    def listar(self):
        with conectar() as con:
            funcionarios = con.execute(
                "SELECT id, nome , cpf , senha_hash FROM funcionarios ORDER BY id"
            ).fetchall()
        resultado = []
        for funcionario in funcionarios:
            resultado.append(self.__montar(funcionario))  
        return resultado          

    def atualizar_nome(self,nome, id):
        with conectar() as con:
            con.execute(
                "UPDATE funcionarios SET nome = %s WHERE id = %s",(nome,id)
            )

    def atualizar_senha(self,senha, id):
            with conectar() as con:
                con.execute(
                    "UPDATE funcionarios SET senha_hash = %s WHERE id = %s",(senha,id)
                )

    def remover(self,id):
        with conectar() as con:
            con.execute(
                "DELETE FROM funcionarios WHERE id = %s", (id,)
            )


    def __montar(self,linha):
        return Funcionario(linha[1], linha[2], linha[3], linha[0], jaHash=True)
    