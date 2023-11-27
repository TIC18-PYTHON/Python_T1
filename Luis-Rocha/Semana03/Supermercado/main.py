from supermercado import Supermercado

def mostrar_menu():
    print("\nMenu:")
    print("1. Inserir novo produto")
    print("2. Excluir produto cadastrado")
    print("3. Listar todos os produtos")
    print("4. Consultar preço de um produto")
    print("5. Sair")

def main():
    mercado = Supermercado()

    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            mercado.adicionar_produto()
        elif escolha == "2":
            mercado.excluir_produto()
        elif escolha == "3":
            mercado.listar_produtos()
        elif escolha == "4":
            mercado.consultar_preco()
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
