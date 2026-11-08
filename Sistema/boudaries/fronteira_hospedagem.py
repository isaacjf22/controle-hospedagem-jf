import os
import subprocess
from time import sleep
from datetime import datetime

from controllers.controlador_hospedagem import ControladorHospedagem
from controllers.controlador_cliente import ControladorCliente
from controllers.controlador_quarto import ControladorQuarto
from controllers.controlador_funcionario import ControladorFuncionario


class RealizarHospedagem:
    def __init__(self, ctl_hospedagem : ControladorHospedagem, ctl_cliente : ControladorCliente, ctl_quarto : ControladorQuarto, ctl_funcionario) :
        self.__ctl_cliente = ctl_cliente
        self.__ctl_quarto = ctl_quarto
        self.__ctl_hospedagem = ctl_hospedagem
        self.__ctl_funcionario = ctl_funcionario


    def mostrar_menu(self):
        menu = {
            "1" : ("Realizar check-in", self.__realizar_checkin),
            "2" : ("Realizar check-out", self.__realizar_chekout),
            "3" : ("Concluir limpeza", self.__concluir_limpeza),
            "4" : ("Adicionar consumo", self.__adicionar_consumo),
            "5" : ("Gerenciar clientes", self.__gerenciar_clientes),
            "6": ("Gerenciar funcionários", self.__gerenciar_funcionarios),
            "7" : ("Realizar logout ", None),
        }
        while True:
            self.__limpar_tela()
            print("="*25)
            print("CONTROLE DE HOSPEDAGEM".center(25))
            print("="*25)
            print()            
            for chave, (texto, _) in menu.items():
                print(f"{chave}) {texto}")
            escolha = self.__validacao("Qual opção deseja escolher: ", ('1','2','3','4', '5', '6','7')) 
            if escolha == '7':
                break
            if escolha in menu: #vai acessar diretamente a chave = escolha 
                menu[escolha][1]() #escolhe qual parte da tupla e executa a função 


    def __realizar_checkin(self):
        self.__limpar_tela()
        print("="*25)
        print("CHECK-IN".center(25))
        print("="*25)
        self.__listar_clientes()
        try:
            idC = int(input("Qual é o id do cliente a ser hospedado? --> "))
            self.__listar_quartos()
            idQ = int(input("Qual é o n° do quarto a ser ocupado? --> "))
            dataSaida = input("Data de saída prevista (dd/mm/aaaa): ")
            data = datetime.strptime(dataSaida, "%d/%m/%Y")
            comprovante = self.__ctl_hospedagem.realizar_checkin(idC, idQ, data)
            self.__limpar_tela()
            print("HOSPEDAGEM REALIZADA!")
            print()
            print(comprovante)
            self.__pausar()
        except ValueError as erro:
            print(erro)
            self.__pausar()

    def __realizar_chekout(self):
        self.__limpar_tela()
        self.__listar_hospedagens()
        try:
            idH = int(input("Qual é o n° da hospedagem para realizar check-out? --> "))
            extrato = self.__ctl_hospedagem.realizar_checkout(idH)
            print(extrato)
            self.__pausar()
        except ValueError as erro:
            print(erro)
            self.__pausar()

    def __concluir_limpeza(self):
        self.__limpar_tela()
        self.__listar_quartos()
        try:
            id = int(input("Qual é o n° do quarto para concluir a limpeza? --> "))
            self.__ctl_quarto.concluir_limpeza(id)
        except ValueError as erro:
            print(erro)
            self.__pausar()

    def __adicionar_consumo(self):
        self.__limpar_tela()
        self.__listar_hospedagens()
        try:
            id = int(input("Qual é o n° da hospedagem a ser adicionada consumo? -->"))
            nome = input("Qual é o nome do produto? --> ")
            quantidade = int(input("Qual é a quantidade desse produto? --> "))
            valor = float(input("Qual é o valor unitário desse produto? --> "))
            self.__ctl_hospedagem.adicionar_consumo(id,nome,quantidade,valor)
        except ValueError as erro:
            print(erro)
            self.__pausar()


    ##FRONTEIRA CRUD CLIENTE 
    def __gerenciar_clientes(self): #deveria estar em outra fronteira
        menu = { #menu pythonico , dicionario com várias opções 
            "1" : ("Cadastrar cliente", self.__cadastrar_cliente),
            "2" : ("Remover cliente", self.__remover_cliente),
            "3" : ("Atualizar cliente", self.__atualizar_cliente),
            "4" : ("Sair", None)
        }
        while True:
            self.__limpar_tela()
            print("="*25)
            print("CONTROLE DE CLIENTE".center(25))
            print("="*25)
            print()            
            for chave, (texto, _) in menu.items():
                print(f"{chave}) {texto}")
            escolha = self.__validacao("Qual opção deseja escolher: ", ('1','2','3','4')) 
            if escolha == '4':
                break
            if escolha in menu: #vai acessar diretamente a chave = escolha 
                menu[escolha][1]() #escolhe qual parte da tupla e executa a função 

    def __cadastrar_cliente(self):
        self.__limpar_tela()
        print("="*25)
        print("CADASTRO DE CLIENTES".center(25))
        print("="*25)
        print()
        try:
            nome = input("Nome do cliente: ")
            cpf = input("CPF do cliente(não precisa formatar): ")
            self.__ctl_cliente.cadastrar_cliente(nome, cpf)
        except ValueError as erro:
            print(erro)
            self.__pausar()

    def __remover_cliente(self): 
        self.__limpar_tela()
        print("="*25)
        print("REMOÇÃO DE CLIENTES".center(25))
        self.__listar_clientes()
        try:
            id = int(input("Qual cliente deseja remover da lista? --> "))
            self.__ctl_cliente.remover_cliente(id)
        except ValueError as erro:
            print(erro)
            self.__pausar()

    def __atualizar_cliente(self):
        self.__limpar_tela()
        print("="*25)
        print("ATUALIZAÇÃO DE CLIENTES".center(25))
        self.__listar_clientes()
        try:
            id = int(input("Qual cliente deseja atualizar os dados? --> "))
            nome = input("Novo nome (se não desejar alterar, aperte ENTER): ") or None #or None faz q aceite nada na variavel 
            self.__ctl_cliente.atualizar_cliente(id, nome)
        except ValueError as erro:
            print(erro)
            self.__pausar()

    def __listar_clientes(self):
        print("="*25)
        print("LISTA DE CLIENTES".center(25))
        print("="*25)
        for cliente  in self.__ctl_cliente.listar_clientes():
            print(f"    {cliente.id}) {cliente.nome} - {cliente.cpf_formatado}")
            sleep(0.05)
        print()

    def __listar_quartos(self):
            print("="*25)
            print("LISTA DE QUARTOS".center(25))
            print("="*25)    
            for quarto in self.__ctl_quarto.listar_quartos():
                print(f"    Quarto n° {quarto.numeroQuarto} - STATUS: {quarto.statusQuarto.value}")
                sleep(0.05)
            print()

    def __listar_hospedagens(self):
            print("="*30)
            print("LISTA DE HOSPEDAGENS ATIVAS".center(30))
            print("="*30)    
            for hospedagem in self.__ctl_hospedagem.listar_hospedagens_ativas():
                print(f"    {hospedagem.id}) QUARTO: {hospedagem.quarto.numeroQuarto} / CLIENTE: {hospedagem.cliente.nome}")
                sleep(0.05)
            print()   

    #FUNCIONÁRIOS 
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
            print("FUNCIONÁRIOS".center(25))
            print("="*25)
            print()
            for chave, (texto,_) in menu.items(): #_ para ignorar completamente a parte 
                print(f"{chave}) {texto}")
            print()
            escolha = self.__validacao("Qual opção deseja escolher: ", ('1','2','3','4')) 
            if escolha == '4':
                break
            if escolha in menu: #vai acessar diretamente a chave = escolha 
                menu[escolha][1]()



    def __criar_funcionario(self): 
        self.__limpar_tela()
        print("="*25)
        print("CADASTRO DE FUNCIONÁRIOS".center(25))
        print("="*25)
        print()
        try:
            nome = input("Nome do funcionário: ")
            cpf = input("CPF do funcionário (não precisa formatar): ")
            senha = input("Nova senha do funcionário: ")
            self.__ctl_funcionario.cadastrar_funcionario(nome, cpf, senha)
        except ValueError as erro:
            print(erro)
            self.__pausar()

    def __remover_funcionario(self): 
        self.__limpar_tela()
        print("="*25)
        print("REMOÇÃO DE FUNCIONÁRIOS".center(25))
        self.__listar_funcionarios()
        try:
            id = int(input("Qual funcionário deseja remover da lista? --> "))
            self.__ctl_funcionario.remover_funcionario(id)
        except ValueError as erro:
            print(erro)
            self.__pausar()

    def __atualizar_funcionario(self):
        self.__limpar_tela()
        print("="*25)
        print("ATUALIZAÇÃO DE FUNCIONÁRIOS".center(25))
        self.__listar_funcionarios()
        try:
            id = int(input("Qual funcionário deseja atualizar os dados? --> "))
            nome = input("Novo nome (se não desejar alterar, aperte ENTER): ") or None #or None faz q aceite nada na variavel 
            senha = input("Nova senha (se não desejar alterar, aperte ENTER): ") or None
            self.__ctl_funcionario.atualizar_funcionario(id, nome, senha)
        except ValueError as erro:
            print(erro)
            self.__pausar()

    def __listar_funcionarios(self):
        print("="*25)
        print("LISTA DE FUNCIONÁRIOS".center(25))
        print("="*25)
        for funcionario  in self.__ctl_funcionario.listar_funcionarios():
            print(f"    {funcionario.id}) {funcionario.nome} - {funcionario.cpf}")
            sleep(0.05)
        print()
         

    #FUNÇÕES
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

    #deveria criar def das leituras e except 