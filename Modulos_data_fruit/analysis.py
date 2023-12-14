from abc import ABC, abstractmethod
from data import Data

class AnaliseDados(ABC): 
    @abstractmethod
    def entrada_de_dados(self):
        pass

    @abstractmethod
    def mostra_mediana(self):
        pass
    
    @abstractmethod
    def mostra_menor(self):
        pass

    @abstractmethod
    def mostra_maior(self):
        pass
    
    @abstractmethod
    def listar_em_ordem(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass


class ListaNomes(AnaliseDados):
    def __init__(self):
        self.__lista = []        

    def entrada_de_dados(self):
        try:
            quantidade = int(input("Quantos nomes deseja inserir? "))  # Solicita a quantidade de nomes a serem inseridos
            for _ in range(quantidade):
                nome = input("Digite o nome: ")  # Solicita o nome
                self.__lista.append(nome)  # Adiciona o nome à lista
        except ValueError:
            print("Erro: Insira um número válido para a quantidade.")

    def mostra_mediana(self):
        self.__lista.sort()  # Ordena a lista de nomes
        tamanho = len(self.__lista)
        if tamanho % 2 == 0:
            indice1 = tamanho // 2 - 1
            indice2 = tamanho // 2
            mediana = self.__lista[indice1]  # Retorna o primeiro nome entre os dois no meio
        else:
            indice = tamanho // 2
            mediana = self.__lista[indice]  # Retorna o nome do meio
        return mediana

    def mostra_menor(self):
        return min(self.__lista)  # Retorna o menor nome da lista

    def mostra_maior(self):
        return max(self.__lista)  # Retorna o maior nome da lista

    def listar_em_ordem(self):
        return sorted(self.__lista)  # Retorna a lista de nomes ordenada

    def __iter__(self):
        return iter(self.__lista)  # Retorna um iterador para a lista de nomes


class ListaDatas(AnaliseDados):
    def __init__(self):
        self.__lista = []        
    
    def entrada_de_dados(self):
        try:
            quantidade = int(input("Quantas datas deseja inserir? "))  # Solicita a quantidade de datas a serem inseridas
            for _ in range(quantidade):
                while True:
                    try:
                        data_input = input("Digite a data no formato dd/mm/aaaa: ")  # Solicita a data no formato dd/mm/aaaa
                        dia, mes, ano = map(int, data_input.split('/'))  # Separa o dia, mês e ano da data
                        data = Data(dia, mes, ano)  # Cria um objeto Data com a data informada
                        self.__lista.append(data)  # Adiciona a data à lista
                        break
                    except ValueError:
                        print("Erro: Insira uma data válida no formato dd/mm/aaaa.")
        except ValueError:
            print("Erro: Insira um número válido para a quantidade.")

    def mostra_mediana(self):
        self.__lista.sort()  # Ordena a lista de datas
        tamanho = len(self.__lista)
        if tamanho % 2 == 0:
            indice1 = tamanho // 2 - 1
            indice2 = tamanho // 2
            mediana = self.__lista[indice1]  # Retorna a primeira data entre as duas no meio
        else:
            indice = tamanho // 2
            mediana = self.__lista[indice]  # Retorna a data do meio
        return mediana

    def mostra_menor(self):
        return min(self.__lista)  # Retorna a menor data da lista

    def mostra_maior(self):
        return max(self.__lista)  # Retorna a maior data da lista

    def listar_em_ordem(self):
        return sorted(self.__lista)  # Retorna a lista de datas ordenada

    def __iter__(self):
        return iter(self.__lista)  # Retorna um iterador para a lista de datas

    def __str__(self):
        return ', '.join(str(data) for data in self.__lista)  # Retorna uma string com as datas da lista separadas por vírgula


class ListaSalarios(AnaliseDados):
    def __init__(self):
        self.__lista = []        

    def entrada_de_dados(self):
        try:
            quantidade = int(input("Quantos salários deseja inserir? "))  # Solicita a quantidade de salários a serem inseridos
            for _ in range(quantidade):
                while True:
                    try:
                        salario = float(input("Digite o salário: "))  # Solicita o salário
                        if salario < 0:
                            raise ValueError("Salário não pode ser negativo.")
                        self.__lista.append(salario)  # Adiciona o salário à lista
                        break
                    except ValueError:
                        print("Erro: Insira um valor de salário válido.")
        except ValueError:
            print("Erro: Insira um número válido para a quantidade.")

    def mostra_mediana(self):
        self.__lista.sort()  # Ordena a lista de salários
        tamanho = len(self.__lista)
        if tamanho % 2 == 0:
            indice1 = tamanho // 2 - 1
            indice2 = tamanho // 2
            mediana = (self.__lista[indice1] + self.__lista[indice2]) / 2  # Retorna a média entre os dois valores do meio
        else:
            indice = tamanho // 2
            mediana = self.__lista[indice]  # Retorna o valor do meio
        return mediana

    def mostra_menor(self):
        return min(self.__lista)  # Retorna o menor salário da lista

    def mostra_maior(self):
        return max(self.__lista)  # Retorna o maior salário da lista

    def listar_em_ordem(self):
        return sorted(self.__lista)  # Retorna a lista de salários ordenada

    def __iter__(self):
        return iter(self.__lista)  # Retorna um iterador para a lista de salários


class ListaIdades(AnaliseDados):
    def __init__(self):
        self.__lista = []        
    
    def entrada_de_dados(self):
        try:
            quantidade = int(input("Quantas idades deseja inserir? "))  # Solicita a quantidade de idades a serem inseridas
            for _ in range(quantidade):
                while True:
                    try:
                        idade = int(input("Digite a idade: "))  # Solicita a idade
                        if idade < 0:
                            raise ValueError("Idade não pode ser negativa.")
                        self.__lista.append(idade)  # Adiciona a idade à lista
                        break
                    except ValueError:
                        print("Erro: Insira uma idade válida.")
        except ValueError:
            print("Erro: Insira um número válido para a quantidade.")

    def mostra_mediana(self):
        self.__lista.sort()  # Ordena a lista de idades
        tamanho = len(self.__lista)
        if tamanho % 2 == 0:
            indice1 = tamanho // 2 - 1
            indice2 = tamanho // 2
            mediana = (self.__lista[indice1] + self.__lista[indice2]) / 2  # Retorna a média entre as duas idades do meio
        else:
            indice = tamanho // 2
            mediana = self.__lista[indice]  # Retorna a idade do meio
        return mediana

    def mostra_menor(self):
        return min(self.__lista)  # Retorna a menor idade da lista

    def mostra_maior(self):
        return max(self.__lista)  # Retorna a maior idade da lista

    def listar_em_ordem(self):
        return sorted(self.__lista)  # Retorna a lista de idades ordenada

    def __iter__(self):
        return iter(self.__lista)  # Retorna um iterador para a lista de idades
