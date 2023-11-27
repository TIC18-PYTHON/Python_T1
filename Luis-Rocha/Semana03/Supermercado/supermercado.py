from produto import Produto
import random
import string

class Supermercado:
    def __init__(self):
        self.produtos = []

    def gerar_codigo(self):
        letra_maiuscula = random.choice(string.ascii_uppercase)
        numeros = ''.join(random.choices(string.digits, k=12))
        return letra_maiuscula + numeros

    def adicionar_produto(self):
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))

        novo_codigo = self.gerar_codigo()
        novo_produto = Produto(novo_codigo, nome, preco)

        if not novo_produto.validar_codigo():
            print("Código inválido. Deve ter 13 caracteres com a primeira letra maiúscula e os demais numéricos.")
            return

        if not novo_produto.validar_nome():
            print("Nome inválido. Deve começar com letra maiúscula.")
            return

        self.produtos.append(novo_produto)
        print("Produto adicionado com sucesso! Código:", novo_codigo)

    def excluir_produto(self):
        codigo = input("Digite o código do produto a ser removido: ")
        for produto in self.produtos:
            if produto.codigo == codigo:
                self.produtos.remove(produto)
                print("Produto removido com sucesso!")
                return
        print("Produto não encontrado.")

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
            return

        produtos_ordenados = sorted(self.produtos, key=lambda x: x.preco)

        qtd_produtos = len(produtos_ordenados)
        qtd_grupos = qtd_produtos // 10
        for i in range(qtd_grupos + 1):
            print(f"\nGrupo {i + 1}:")

            inicio = i * 10
            fim = min((i + 1) * 10, qtd_produtos)
            grupo = produtos_ordenados[inicio:fim]

            for produto in grupo:
                print(f"{produto}")

    def consultar_preco(self):
        codigo = input("Digite o código do produto para consultar o preço: ")
        for produto in self.produtos:
            if produto.codigo == codigo:
                print(f"O preço do produto {produto.nome} é R$ {produto.preco:.2f}")
                return
        print("Produto não encontrado.")
