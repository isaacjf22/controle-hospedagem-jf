from entities.pessoas.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, cpf, id):
        super().__init__(id, nome, cpf)




