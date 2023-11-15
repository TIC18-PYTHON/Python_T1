#Exercício 3: Manipulação de variáveis de tipo string e explorando o uso de print.

#A função ord() retorna o valor ASCII de um caractere.	

x =input("Digite apenas um caractere: ")
print ("O valor na tabela ASCII de é:" , ord(x), "! e o caractere é:", x)

#A função chr() retorna o caractere correspondente ao valor ASCII.
z = int(input("Digite um valor: "))
print ("O caractere correspondente ao valor ASCII é:" , chr(z))
print ("O valor em octal é:" , oct(z))
print ("O valor em hexadecimal é:" , hex(z))
