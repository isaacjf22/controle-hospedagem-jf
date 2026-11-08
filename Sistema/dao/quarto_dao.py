from database.conexao import conectar
from entities.quarto.quarto_simples import QuartoSimples
from entities.quarto.quarto_duplo import QuartoDuplo
from entities.status import Status


class QuartoDAO:

    def inserir(self, numero):
        with conectar() as con:
            con.execute(
                "INSERT INTO quartos (numero_quarto) VALUES (%s)", (numero,)
            )

    def buscar_quarto(self , numero):
        with conectar() as con: #with n fecha escopo 
            quarto = con.execute(
                "SELECT id, numero_quarto, status FROM quartos WHERE numero_quarto = %s" , (numero,)
            ).fetchone()
        return self.__montar(quarto) if quarto else None 
        
    def listar(self):
        with conectar() as con:
            quartos = con.execute(
                "SELECT id, numero_quarto, status FROM quartos ORDER BY numero_quarto"
            ).fetchall()

        resultado = []
        for quarto in quartos:
            resultado.append(self.__montar(quarto))
        return resultado

    def ocupar(self, numero):
        with conectar() as con:
            con.execute(
                "UPDATE quartos SET status = 'OCUPADO' WHERE numero_quarto = %s" , (numero,)
            )

    def limpar(self, numero):
        with conectar() as con:
            con.execute(
                "UPDATE quartos SET status = 'LIMPEZA' WHERE numero_quarto = %s" , (numero,)
            )

    def concluir_limpeza(self, numero):
        with conectar() as con:
            con.execute(
                "UPDATE quartos SET status = 'LIVRE' WHERE numero_quarto = %s" , (numero,)
            )        



    def __montar(self, quarto):
        id_ , numero , status = quarto #os atributos serao atribuidos em sequencia 
        status = Status[status] #converter o texto em status enum
        if numero < 11 :
            return QuartoSimples(numero,status, id_)
        return QuartoDuplo(numero,status, id_)