from database.conexao import conectar
from entities.hospedagem import Hospedagem
from dao.cliente_dao import ClienteDAO
from dao.quarto_dao import QuartoDAO

class HospedagemDAO:
    def __init__(self, cliente_dao : ClienteDAO, quarto_dao : QuartoDAO):
        self.__cliente_dao = cliente_dao
        self.__quarto_dao = quarto_dao
        


    def check_in(self, hospedagem :  Hospedagem):
        with conectar() as con:
            con.execute(
                "INSERT INTO hospedagens (id_cliente, numero_quarto, saida_prevista, entrada) VALUES (%s, %s ,%s, %s)", (hospedagem.cliente.id, hospedagem.quarto.numeroQuarto, hospedagem.saidaPrevista,hospedagem.entrada)
            )

    def check_out(self, idHospedagem, saida , valor_total):
        with conectar() as con:
            con.execute(
                "UPDATE hospedagens SET saida = %s , valor_total = %s WHERE id = %s", (saida,valor_total,idHospedagem)
            )

    def buscar_id(self, idHospedagem):
        with conectar() as con:
            hospedagem = con.execute(
                "SELECT id, id_cliente, numero_quarto, saida_prevista, entrada FROM hospedagens WHERE id = %s", (idHospedagem,)
            ).fetchone()
        return self.__montar(hospedagem)

    def listar(self):
        with conectar() as con:
            hospedagens = con.execute(
                "SELECT id, id_cliente, numero_quarto, saida_prevista, entrada FROM hospedagens WHERE saida IS NULL ORDER BY id"
            ).fetchall()
        resultado = []
        for hospedagem in hospedagens:
            resultado.append(self.__montar(hospedagem))
        return resultado

    def __montar(self, linha):
        # id , id_cliente, quarto, saida , entrada 
        cliente = self.__cliente_dao.buscar_id(linha[1])
        quarto = self.__quarto_dao.buscar_quarto(linha[2])
        return Hospedagem(linha[4],linha[3],cliente,quarto,linha[0])
    