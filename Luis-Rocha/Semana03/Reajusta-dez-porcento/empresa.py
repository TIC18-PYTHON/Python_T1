from funcionario import Funcionario

def carregar_funcionarios(arquivo):
    funcionarios = []
    try:
        with open(arquivo, 'r') as file:
            linhas = file.readlines()
            for linha in linhas:
                dados = linha.strip().split(',')
                nome, sobrenome, ano_nascimento, rg, ano_admissao, salario = dados
                funcionario = Funcionario(nome, sobrenome, ano_nascimento, rg, ano_admissao, salario)
                funcionarios.append(funcionario)
    except FileNotFoundError:
        print(f"Arquivo '{arquivo}' não encontrado. Será criado um novo arquivo ao salvar os dados.")

    return funcionarios

def salvar_funcionarios(funcionarios, arquivo):
    with open(arquivo, 'w') as file:
        for funcionario in funcionarios:
            file.write(str(funcionario))

def reajusta_dez_porcento(funcionarios):
    for funcionario in funcionarios:
        funcionario.salario *= 1.1 

def adicionar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    sobrenome = input("Digite o sobrenome do funcionário: ")
    ano_nascimento = input("Digite o ano de nascimento do funcionário (AAAA): ")
    rg = input("Digite o RG do funcionário: ")
    ano_admissao = input("Digite o ano de admissão do funcionário: ")
    salario = input("Digite o salário do funcionário: ")

    return Funcionario(nome, sobrenome, ano_nascimento, rg, ano_admissao, salario)

def excluir_funcionario(funcionarios):
    if not funcionarios:
        print("Não há funcionários para excluir.")
        return funcionarios

    print("Funcionários:")
    for i, funcionario in enumerate(funcionarios):
        print(f"{i + 1}. {funcionario.nome} {funcionario.sobrenome}")

    try:
        indice = int(input("Digite o número do funcionário a ser excluído: ")) - 1
        if 0 <= indice < len(funcionarios):
            funcionarios.pop(indice)
            print("Funcionário excluído com sucesso!")
        else:
            print("Número de funcionário inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")

    return funcionarios
