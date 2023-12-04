

#ToDoList


lista = []
listaid = []
id = 0
listamarcada = []


while True:

    print("ESCOLHA UMA OPÇÃO:")
    print("--------------------------")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Listar itens")
    print("4 - Sair")
    opcao = input()
    match opcao:
        case '1':
            print("Adicionar item")
            print("Qual item deseja adicionar?")
            item = input()
            lista.append(item)
            id += 1
            listaid.append(id)
            listamarcada.append("[]")
        
        
        
        case '2':
            print("Remover item")
            print("Qual item deseja remover?")
            item = input()
            if item in lista:
                indice = lista.index(item)
                lista.pop(indice)
                listaid.pop(indice)
                listamarcada.pop(indice)
                print("Item removido")
            else:
                print("Item inexistente")
       
       
       
       
       
        case '3':
            print("Listar itens")
            for item in lista:
                print (listaid[lista.index(item)], "-", item, listamarcada[lista.index(item)])

            print ("Você deseja marcar como concluído um item?")
            print ("1 - Sim")
            print ("2 - Não")
            op = input()
            if op == '1':
                print ("Qual item deseja alterar?")
                item = input()
                if item in lista:
                    print ("Marcado como concluido")
                    listamarcada[lista.index(item)] = "[X]"
                else:
                    print("Item inexistente")
        case '4':
            print("Sair")
            break
        

