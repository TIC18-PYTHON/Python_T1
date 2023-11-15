#Manipulação de variáveis de tipo inteiro, explorando as características e os limites.

a = 5
b = 7

#ADIÇÃO
c = a + b
print("A soma é: ", c)

#SUBTRAÇÃO
d = a - b
print("A subtração é: ", d)

#MULTIPLICACAO
e = a * b
print("A multiplicação é: ", e)

#DIVISAO
f = a / b
print("A divisão é: ", f)

#DIVISÃO INTEIRA
g = a // b
print("A divisão inteira é: ", g)

#MODULO
h = a % b
print("O resto da divisão é: ", h)

#EXPONENCIACAO
i = a ** b
print("A exponenciacao é: ", i)

#ADIÇÃO ATRIBUICAO
a += b
print("A soma atribuição é: ", a)
a = 5
b = 7

#SUBTRACAO ATRIBUICAO
a -= b
print("A subtracao atribuição é: ", a)
a = 5
b = 7

#MULTIPLICACAO ATRIBUICAO
a *= b
print("A multiplicacao atribuição é: ", a)
a = 5
b = 7

#DIVISAO ATRIBUICAO
a /= b
print("A divisao atribuição é: ", a)
a = 5
b = 7

#DIVISAO INTEIRA ATRIBUICAO
a //= b
print("A divisao inteira atribuição é: ", a)
a = 5
b = 7

#MODULO ATRIBUICAO
a %= b
print("O resto da divisao atribuição é: ", a)
a = 5
b = 7

#EXPONENCIACAO ATRIBUICAO
a **= b
print("A exponenciacao atribuição é: ", a)


#COMPARAÇÃO DE TAMANHO DE INTEIROS ENTRE C++ E PYTHON

fat = 1
Maiorinteirocpp = 2147483647
for x in range(1,31):
    fat*=x
    print(x, "! =", fat)

print ("O fatorial de 30 é: ", fat, " e o maior inteiro em C++ é: ", Maiorinteirocpp)

#EXEMPLO DE VARIAVEIS IMUTAVEIS

A = 10
B = A 
print("A = ", A)
print("e ")
print("B = ", B)
print("Após incrmentar o valor de A em 1 temos que ...")
A += 1 
print("A = ", A)
print("enquanto ")
print("B = ", B)

#BUSCANDO METODOS DE INTEIROS
help(int)