from entities.pessoas.pessoa import Pessoa
import bcrypt

class Funcionario(Pessoa):
    def __init__(self,nome , cpf , senha, id = None, jaHash = False):
        super().__init__(nome, cpf, id)
        self.__senha = senha if jaHash else self.validar_senha(senha) #pode receber um hash e fazer a conversão novamente 

    @property
    def senha(self):
        return self.__senha

    @staticmethod
    def validar_senha(senha) -> str:
        if not senha or not senha.strip():
            raise ValueError("Não pode senha vazia.")
        elif len(senha) < 4:
            raise ValueError("Senha deve possuir pelo menos 4 caracteres")
        return Funcionario.gerar_hash(senha)

    
    def alterar_senha(self, nova):
        novo_hash = self.validar_senha(nova)
        if self.__checar_hash(nova):
            raise ValueError("A nova senha precisa ser diferente da anterior.")
        self.__senha = novo_hash
        return novo_hash

    def verificar_senha(self, tentativa : str) -> bool:
        if self.__checar_hash(tentativa):
            return True
        return False
        #se estiver errada, retorna None e significa False.
    
    @staticmethod
    def gerar_hash(senha : str):
        crip = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt() )
        return crip.decode('utf-8')

    def __checar_hash(self, tentativa : str):
        return bcrypt.checkpw(tentativa.encode('utf-8'), self.__senha.encode('utf-8'))


