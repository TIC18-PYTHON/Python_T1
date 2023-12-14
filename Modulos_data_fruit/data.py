class Data:
    def __init__(self, dia=1, mes=1, ano=1940):
        # Verifica se o dia é válido (entre 1 e 31)
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        # Verifica se o mês é válido (entre 1 e 12)
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        # Verifica se o ano é válido (entre 1940 e 2100)
        if ano < 1940 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        # Verifica se o dia é válido (entre 1 e 31)
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        # Verifica se o mês é válido (entre 1 e 12)
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        # Verifica se o ano é válido (entre 1940 e 2100)
        if ano < 1940 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        # Retorna a representação em string da data no formato "dia/mês/ano"
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        # Verifica se duas datas são iguais
        return (self.__dia, self.__mes, self.__ano) == (outraData.__dia, outraData.__mes, outraData.__ano)
    
    def __lt__(self, outraData):
        # Verifica se uma data é menor que outra
        return (self.__ano, self.__mes, self.__dia) < (outraData.__ano, outraData.__mes, outraData.__dia)
    
    def __gt__(self, outraData):
        # Verifica se uma data é maior que outra
        return (self.__ano, self.__mes, self.__dia) > (outraData.__ano, outraData.__mes, outraData.__dia)
