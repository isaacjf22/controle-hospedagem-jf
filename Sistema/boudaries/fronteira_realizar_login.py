from controllers.controlador_login import ControladorLogin
from controllers.controlador_funcionario import ControladorFuncionario
from time import sleep

import os 
import subprocess

class RealizarLogin:
    def __init__(self, ctl_login : ControladorLogin, ctl_funcionario : ControladorFuncionario) -> None:
        self.__ctl_login = ctl_login
        self.__ctl_funcionario = ctl_funcionario

    def mostrar_menu(self): 
        menu = {
            "1": ("Realizar login", self.__realizar_login),
            "2": ("Gerenciar funcionários", self.__gerenciar_funcionarios),
            "3": ("Sair do programa", None)
        }
        while True:

            for chave, (texto, _ ) in menu.items():
                print(f"{chave}) {texto}")
            escolha = self.__validacao("Qual opção deseja escolher", ("1","2","3")) 
            if escolha == "3":
                print("Saindo do programa...")
                break; 
            if escolha in menu:
                menu[escolha][1]()
    
    def __realizar_login(self):
        self.__limpar_tela()
        print("="*25)
        print("LOGIN".center(25))
        print("="*25)
        nome = input("Nome: ")
        senha = input("Senha: ")
        self.__ctl_login.login(nome, senha)

    def __gerenciar_funcionarios(self):
        menu = {
            "1": ("Cadastrar funcionário", self.__criar_funcionario), #a chave serve de referencia, ai escolhe a chave para acessar o valor e acionar a função 
            "2": ("Remover funcionário", self.__remover_funcionario),
            "3": ("Atualizar funcionário" , self.__atualizar_funcionario),
            "4": ("Sair", None)
        }
        while True:
            self.__limpar_tela()
            print("="*25)
            print("HOSPEDAGEM JF".center(25))
            print("="*25)
            print()
            for chave, (texto,_) in menu.items(): #_ para ignorar completamente a parte 
                print(f"{chave}) {texto}")
            print()
            escolha = self.__validacao("Qual opção deseja escolher", ('1','2','3','4')) 
            if escolha == '4':
                break; 
            if escolha in menu: #vai acessar diretamente a chave = escolha 
                menu[escolha][1]()



    def __criar_funcionario(self): 
        self.__limpar_tela()
        print("="*25)
        print("CADASTRO DE FUNCIONÁRIOS".center(25))
        print("="*25)
        print()
        nome = input("Nome do funcionário: ")
        cpf = input("CPF do funcionário (não precisa formatar): ")
        senha = input("Nova senha do funcionário: ")
        self.__ctl_funcionario.cadastrar_funcionario(nome, cpf, senha)

    def __remover_funcionario(self): 
        self.__limpar_tela()
        print("="*25)
        print("REMOÇÃO DE FUNCIONÁRIOS".center(25))
        self.__listar_funcionarios()
        id = input("Qual funcionário deseja remover da lista?")
        self.__ctl_funcionario.remover_funcionario(id)

    def __atualizar_funcionario(self):
        self.__limpar_tela()
        print("="*25)
        print("ATUALIZAÇÃO DE FUNCIONÁRIOS".center(25))
        self.__listar_funcionarios()
        id = input("Qual funcionário deseja atualizar os dados?")
        nome = input("Novo nome (se não desejar alterar, aperte ENTER): ") or None #or None faz q aceite nada na variavel 
        senha = input("Nova senha (se não desejar alterar, aperte ENTER): ") or None
        self.__ctl_funcionario.atualizar_funcionario(id, nome, senha)

    def __listar_funcionarios(self):
        print("="*25)
        print("LISTA DE FUNCIONÁRIOS".center(25))
        print("="*25)
        for funcionario  in self.__ctl_funcionario.listar_funcionarios():
            print(f"    {funcionario.id}) {funcionario.nome} - {funcionario.cpf}")
            sleep(0.5)
        print()
    
    def __validacao(self, mensagem, valores_aceitos):
        valor = input(mensagem)
        if valor not in valores_aceitos:
            print("Entrada incorreta.")
        return valor

    def __limpar_tela(self):
        if os.name == 'nt': #windows
            subprocess.run(["cls"], shell=True) # true pq é um comando no terminal 
        else:
            subprocess.run(["clear"]) # false pq é uma execução no terminal 
