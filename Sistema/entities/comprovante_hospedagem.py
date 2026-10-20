class ComprovanteHospedagem:
    def __init__(self, nomeCliente, cpfCliente, entrada, saidaPrevista, numeroQuarto):
        self.__nomeCliente = nomeCliente
        self.__cpfCliente = cpfCliente
        self.__entrada = entrada
        self.__saidaPrevista = saidaPrevista
        self.__numeroQuarto = numeroQuarto

    def __str__(self):
        cpf = f"{self.__cpfCliente[:3]}.{self.__cpfCliente[3:6]}.{self.__cpfCliente[6:9]}-{self.__cpfCliente[9:]}"
        return (
                "=" * 36 + "\n"
                           "    COMPROVANTE DE HOSPEDAGEM\n"
                + "=" * 36 + "\n"
                             f"Cliente:        {self.__nomeCliente}\n"
                             f"CPF:            {cpf}\n"
                             f"Quarto:         {self.__numeroQuarto}\n"
                             f"Entrada:        {self.__entrada:%d/%m/%Y %H:%M}\n"
                             f"Saída prevista: {self.__saidaPrevista:%d/%m/%Y %H:%M}\n"
                + "=" * 36
        )

