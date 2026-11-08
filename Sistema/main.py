from controllers.controlador_sistema import ControladorSistema
import psycopg

ctl_sistema = ControladorSistema()

def main():
    try:
        ctl_sistema.inicio()
    except psycopg.OperationalError:
        print("Não foi possível conectar ao banco de dados.")
    except psycopg.Error as erro:
        print(f"Erro no banco de dados : {erro}")



if __name__ == "__main__":
    main()