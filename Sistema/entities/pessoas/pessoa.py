from abc import ABC , abstractmethod

class Pessoa(ABC):
    def __init__(self, id , nome, cpf):
        self._id = id
        self.nome = nome
        self._cpf = self.validar_cpf(cpf) #validando cpf sem liberar o acesso pro codigo

    #encapsulamento
    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self.nome
    @nome.setter
    def nome(self,nome : str):
        if not nome or not nome.strip(): ##se estiver vazio ou vazio com espaços cortados
            raise ValueError("Não pode nome vazio.")
        else:
            self.nome = nome.strip() #corta os espços vazios

    @property
    def cpf(self):
        return f"{self._cpf[:3]}.{self._cpf[3:6]}.{self._cpf[6:9]}-{self._cpf[9:]}" #formatação realizada por meio de fatiamentos

    @staticmethod
    def validar_cpf(cpf : str) -> str:
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("CPF inválido")
        return cpf



