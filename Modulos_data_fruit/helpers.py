from data import Data

def percorrer_listas_com_zip(lista_nomes, lista_salarios):
    # Itera sobre duas listas simultaneamente usando a função zip()
    for nome, salario in zip(lista_nomes, lista_salarios):
        print(f"{nome}: R${salario}")

def calcular_folha_com_reajuste(lista_salarios):
    # Calcula o novo salário com um reajuste de 10% para cada valor na lista de salários
    for salario in lista_salarios:
        print(f"Novo salário com reajuste de 10%: R${salario * 1.1:.2f}")

def modificar_datas_anteriores_a_2019(lista_datas):
    # Modifica as datas anteriores a 01/01/2019 para o dia 01
    for data in lista_datas:
        if data < Data(1, 1, 2019):
            data.dia = 1
    print("Datas modificadas com sucesso!")

def iterador_zip(lista_nomes, lista_salarios):
    # Chama a função percorrer_listas_com_zip() para iterar sobre duas listas usando zip()
    percorrer_listas_com_zip(lista_nomes, lista_salarios)

def iterador_map(lista_salarios):
    # Chama a função calcular_folha_com_reajuste() para calcular o novo salário com reajuste de 10% usando map()
    calcular_folha_com_reajuste(lista_salarios)

def iterador_filter(lista_datas):
    # Chama a função modificar_datas_anteriores_a_2019() para modificar as datas anteriores a 01/01/2019 usando filter()
    modificar_datas_anteriores_a_2019(lista_datas)
