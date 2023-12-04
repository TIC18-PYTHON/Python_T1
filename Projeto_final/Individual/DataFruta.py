from abc import ABC, abstractmethod
from typing import List

class Data:
    def __init__(self, dia=1, mes=1, ano=1940):
        if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1940 or ano > 2100:
            raise ValueError("Dados inválidos")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        if ano < 1940 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano

    def __str__(self):
        return "{:02d}-{:02d}-{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return self.__dia == outraData.__dia and self.__mes == outraData.__mes and self.__ano == outraData.__ano

    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                return self.__dia < outraData.__dia
        return False

    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                return self.__dia > outraData.__dia
        return False


class AnaliseDados(ABC):
    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass

    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass


class ListaNomes(AnaliseDados):
    def __init__(self):
        super().__init__(str)
        self.__lista = []

    def entradaDeDados(self):
        elementos = int(input("Quantos nomes você deseja adicionar? "))
        for _ in range(elementos):
            nome = input("Digite um nome: ")
            self.__lista.append(nome)

    def mostraMediana(self):
        sorted_lista = sorted(self.__lista)
        meio = len(sorted_lista) // 2
        print("Mediana:", sorted_lista[meio])

    def mostraMenor(self):
        print("Menor:", min(self.__lista, key=len))

    def mostraMaior(self):
        print("Maior:", max(self.__lista, key=len))


class ListaDatas(AnaliseDados):
    def __init__(self):
        super().__init__(Data)
        self.__lista = []

    def entradaDeDados(self):
        elementos = int(input("Quantas datas você deseja adicionar? "))
        for _ in range(elementos):
            dia = int(input("Digite o dia: "))
            mes = int(input("Digite o mês: "))
            ano = int(input("Digite o ano: "))
            try:
                data = Data(dia, mes, ano)
                self.__lista.append(data)
            except ValueError as e:
                print(f"Erro: {e}. Dados não adicionados. Tente novamente.")

    def mostraMediana(self):
        sorted_lista = sorted(self.__lista, key=lambda x: (x.ano, x.mes, x.dia))
        meio = len(sorted_lista) // 2
        if meio < len(sorted_lista):
            print("Mediana:", sorted_lista[meio])
        else:
            print("Lista vazia, não é possível calcular a mediana.")

    def mostraMenor(self):
        if self.__lista:
            menor_data = min(self.__lista, key=lambda x: (x.ano, x.mes, x.dia))
            print("Menor:", menor_data)
        else:
            print("Lista vazia, não é possível calcular o menor valor.")

    def mostraMaior(self):
        if self.__lista:
            maior_data = max(self.__lista, key=lambda x: (x.ano, x.mes, x.dia))
            print("Maior:", maior_data)
        else:
            print("Lista vazia, não é possível calcular o maior valor.")


class ListaSalarios(AnaliseDados):
    def __init__(self):
        super().__init__(float)
        self.__lista = []

    def entradaDeDados(self):
        elementos = int(input("Quantos salários você deseja adicionar? "))
        for _ in range(elementos):
            salario = float(input("Digite um salário: "))
            self.__lista.append(salario)

    def mostraMediana(self):
        sorted_lista = sorted(self.__lista)
        meio = len(sorted_lista) // 2
        print("Mediana:", sorted_lista[meio])

    def mostraMenor(self):
        print("Menor:", min(self.__lista))

    def mostraMaior(self):
        print("Maior:", max(self.__lista))


class ListaIdades(AnaliseDados):
    def __init__(self):
        super().__init__(int)
        self.__lista = []

    def entradaDeDados(self):
        elementos = int(input("Quantas idades você deseja adicionar? "))
        for _ in range(elementos):
            idade = int(input("Digite uma idade: "))
            self.__lista.append(idade)

    def mostraMediana(self):
        sorted_lista = sorted(self.__lista)
        meio = len(sorted_lista) // 2
        print("Mediana:", sorted_lista[meio])

    def mostraMenor(self):
        print("Menor:", min(self.__lista))

    def mostraMaior(self):
        print("Maior:", max(self.__lista))


def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas: List[AnaliseDados] = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.entradaDeDados()
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        print("___________________")

    print("Fim do teste!!!")


if __name__ == "__main__":
    main()