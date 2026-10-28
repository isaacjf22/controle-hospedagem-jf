from entities.pessoas.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self,nome , cpf , id , senha):
        super().__init__(id, nome, cpf)
        self.__senha = self.validar_senha(senha)

    @staticmethod
    def validar_senha(senha) -> str:
        if not senha or not senha.strip():
            raise ValueError("Não pode senha vazia.")
        elif len(senha) < 4:
            raise ValueError("Senha deve possuir pelo menos 4 caracteres")
        return senha

    def alterar_senha(self, nova) -> None:
        self.validar_senha(nova)
        if nova == self.__senha:
            raise ValueError("A nova senha precisa ser diferente da anterior.")
        self.__senha = nova

    def verificar_senha(self, tentativa : str) -> bool:
        if tentativa == self.__senha:
            return True
        return False
        #se estiver errada, retorna None e significa False.





