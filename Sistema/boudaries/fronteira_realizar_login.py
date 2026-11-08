from controllers.controlador_login import ControladorLogin
from controllers.controlador_funcionario import ControladorFuncionario
from time import sleep

import os 
import subprocess

class RealizarLogin:
    def __init__(self, ctl_login : ControladorLogin) -> None:
        self.__ctl_login = ctl_login
        

    def mostrar_menu(self): 
        menu = {
            "1": ("Realizar login", self.__realizar_login),
            "2": ("Sair do programa", None)
        }
        while True:
            if self.__ctl_login.funcionarioLogado is not None:
                return 
            self.__limpar_tela()
            print("="*25)
            print("HOSPEDAGEM JF".center(25))
            print("="*25)
            print()
            for chave, (texto, _ ) in menu.items():
                print(f"{chave}) {texto}")
            escolha = self.__validacao("Qual opção deseja escolher: ", ("1","2")) 
            if escolha == "2":
                print("Saindo do programa...")
                break 
            if escolha in menu:
                menu[escolha][1]()
    
    def __realizar_login(self):
        self.__limpar_tela()
        print("="*25)
        print("LOGIN".center(25))
        print("="*25)
        nome = input("Nome: ")
        senha = input("Senha: ")
        try: #oq for tentar , coloca em try 
            self.__ctl_login.login(nome, senha) 
            print("Login realizado!")
            sleep(3)
        except ValueError as erro:
            print(erro)
            self.__pausar()
    
    def __validacao(self, mensagem, valores_aceitos):
        while True:
            valor = input(mensagem)
            if valor not in valores_aceitos:
                print("Entrada incorreta.")
            else:
                break
        return valor

    def __pausar(self):
        input("Aperte qualquer tecla para continuar...\n")

    def __limpar_tela(self):
        if os.name == 'nt': #windows
            subprocess.run(["cls"], shell=True) # true pq é um comando no terminal 
        else:
            subprocess.run(["clear"]) # false pq é uma execução no terminal 
