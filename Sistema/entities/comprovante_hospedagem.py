class ComprovanteHospedagem:
    def __init__(self, nomeCliente, cpfCliente, entrada, saidaPrevista, numeroQuarto):
        self.__nomeCliente = nomeCliente
        self.__cpfCliente = cpfCliente
        self.__entrada = entrada
        self.__saidaPrevista = saidaPrevista
        self.__numeroQuarto = numeroQuarto

    def __str__(self):
        return (
                "=" * 36 + "\n"
                           "    COMPROVANTE DE HOSPEDAGEM\n"
                + "=" * 36 + "\n"
                             f"Cliente:        {self.__nomeCliente}\n"
                             f"CPF:            {self.__cpfCliente}\n"
                             f"Quarto:         {self.__numeroQuarto}\n"
                             f"Entrada:        {self.__entrada:%d/%m/%Y %H:%M}\n"
                             f"Saída prevista: {self.__saidaPrevista:%d/%m/%Y %H:%M}\n"
                + "=" * 36
        )

