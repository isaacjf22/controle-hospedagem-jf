class ExtratoConta:
    def __init__(self, nome, cpf, saida, valorTotal):
        self.__nome = nome
        self.__cpf = cpf
        self.__saida = saida
        self.__valorTotal = valorTotal

    def __str__(self): #texto formatado do extrato
        cpf = f"{self.__cpf[:3]}.{self.__cpf[3:6]}.{self.__cpf[6:9]}-{self.__cpf[9:]}"
        return (
                "=" * 36 + "\n"
                           "        EXTRATO DE CONTA\n"
                + "=" * 36 + "\n"
                             f"Cliente: {self.__nome}\n"
                             f"CPF:     {cpf}\n"
                             f"Saída:   {self.__saida:%d/%m/%Y %H:%M}\n"
                + "-" * 36 + "\n"
                             f"TOTAL:   R$ {self.__valorTotal:.2f}\n"
                + "=" * 36
        )
    