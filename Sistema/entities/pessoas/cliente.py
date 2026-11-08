from entities.pessoas.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, cpf, id=None):
        super().__init__(nome, cpf, id)




