from pathlib import Path
from typing import LiteralString, cast
from database.conexao import conectar


def resetar():
    resposta = input("Isso APAGA clientes, hospedagens e gastos. Digite RESETAR para confirmar: ")
    if resposta != "RESETAR":
        print("Cancelado.")
        return

    sql = (Path(__file__).resolve().parents[2] / "resetar.sql").read_text(encoding="utf-8")
    with conectar() as con:
        con.execute(cast(LiteralString, sql))
    print("Sistema restaurado ao estado inicial.")


if __name__ == "__main__":
    resetar()