class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def validar_codigo(self):
        return len(self.codigo) == 13 and self.codigo[0].isupper() and self.codigo[1:].isdigit()

    def validar_nome(self):
        return self.nome[0].isupper()

    def __str__(self):
        return f"Código: {self.codigo}, Nome: {self.nome}, Preço: R$ {self.preco:.2f}"
