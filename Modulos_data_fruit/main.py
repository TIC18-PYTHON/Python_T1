from data import Data
from analysis import ListaNomes, ListaDatas, ListaSalarios, ListaIdades
from helpers import *

def menu():
    """
    Função que exibe um menu e realiza ações de acordo com a opção escolhida pelo usuário.
    """

    # Instanciando as listas de nomes, datas, salários e idades
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    while True:
        print("\n Menu Principal \n")
        print("1. Incluir um nome na lista de nomes")
        print("2. Incluir um salário na lista de salários")
        print("3. Incluir uma data na lista de datas")
        print("4. Incluir uma idade na lista de idades")
        print("5. Percorrer as listas de nomes e salários")
        print("6. Calcular o valor da folha com um reajuste de 10%")
        print("7. Modificar o dia das datas anteriores a 2019")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nomes.entrada_de_dados()  # Chama a função para inserir um nome na lista de nomes
        elif opcao == "2":
            salarios.entrada_de_dados()  # Chama a função para inserir um salário na lista de salários
        elif opcao == "3":
            datas.entrada_de_dados()  # Chama a função para inserir uma data na lista de datas
        elif opcao == "4":
            idades.entrada_de_dados()  # Chama a função para inserir uma idade na lista de idades
        elif opcao == "5":
            iterador_zip(nomes.listar_em_ordem(), salarios.listar_em_ordem())  # Percorre as listas de nomes e salários
        elif opcao == "6":
            iterador_map(salarios.listar_em_ordem())  # Calcula o valor da folha com um reajuste de 10%
        elif opcao == "7":
            iterador_filter(datas.listar_em_ordem())  # Modifica o dia das datas anteriores a 2019
        elif opcao == "8":
            print("Saindo...")
            break  # Sai do loop while
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
