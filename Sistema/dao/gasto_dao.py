from entities.gasto import Gasto
from database.conexao import conectar
from decimal import Decimal



class GastoDAO:

    def inserir(self, gasto : Gasto):
        with conectar() as con:
            con.execute(
                "INSERT INTO gastos (nome, id_hospedagem, valor_unitario, quantidade) VALUES (%s, %s, %s ,%s)", (gasto.nome, gasto.id_hospedagem, gasto.valorUnitario, gasto.quantidade)
            )

    def calcular_total(self, id_Hospesagem):
        with conectar() as con:
            total = con.execute(
                "SELECT COALESCE(SUM(valor_unitario * quantidade), 0) FROM gastos WHERE id_hospedagem = %s", (id_Hospesagem,)
            ).fetchone() #pegar o resultado [0]
        return total[0] if total else Decimal(0)

    





    # def __montar(self, linha):
    #     #id nome id_hosp valor quantidade
    #     return Gasto(linha[1],linha[2],linha[3],linha[4])

