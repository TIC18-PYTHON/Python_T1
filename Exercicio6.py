#Exercicio 6: Manipulando Listas

l = [1,2,3,4,5,6,7,8,9]
print(l[::-1])
print(l[-1::])
print(l[:-1:])
print(l[::-2])
print(l[-2::])
print(l[:-2:])

#Ano chines

L = ["Macaco","Galo", "Cão", "Porco", "Rato", "Boi", "Tigre", "Coelho","Dragão", "Serpente", "Cavalo", "Carneiro"]
x = int(input("Digite o ano que você nasceu:"))
print("Você nasceu no ano do:", L[x%12])