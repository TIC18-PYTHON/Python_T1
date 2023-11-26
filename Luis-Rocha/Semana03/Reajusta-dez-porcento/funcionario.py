class Funcionario:
    def __init__(self, nome, sobrenome, ano_nascimento, rg, ano_admissao, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
        self.rg = rg
        self.ano_admissao = ano_admissao
        self.salario = float(salario)  # Garante que o salário seja um número float

    def __str__(self):
        return f"{self.nome},{self.sobrenome},{self.ano_nascimento},{self.rg},{self.ano_admissao},{self.salario}\n"
