from pathlib import Path
from typing import LiteralString, cast
from database.conexao import conectar

def criar_quartos():
    sql = (Path(__file__).resolve().parents[2] / "quartos.sql").read_text(encoding="utf-8")
    with conectar() as con:
        con.execute(cast(LiteralString, sql))
    print("Quartos criados no banco de dados.")

if __name__ == "__main__":
    criar_quartos()