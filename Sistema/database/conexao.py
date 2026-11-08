import os 
import psycopg #conexao entre python e postgreSQL 
from dotenv import load_dotenv #carregar as informações do .env 

load_dotenv() #aqui carrega as informações do .env 

def conectar(): #essa funçao serve para conectar ao banco de dados toda vez que for feita alguma ação relacionada ao banco de dados 
    return psycopg.connect(
        host=os.getenv("DB_HOST"), #onde esta o servidor 
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

