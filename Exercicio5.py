#Manipulação de variáveis de tipo inteiro, explorando as características e os limites.

a = 2.0
b = 5.0

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
a = 2.0
b = 5.0

#SUBTRACAO ATRIBUICAO
a -= b
print("A subtracao atribuição é: ", a)
a = 2.0
b = 5.0

#MULTIPLICACAO ATRIBUICAO
a *= b
print("A multiplicacao atribuição é: ", a)
a = 2.0
b = 5.0

#DIVISAO ATRIBUICAO
a /= b
print("A divisao atribuição é: ", a)
a = 2.0
b = 5.0

#DIVISAO INTEIRA ATRIBUICAO
a //= b
print("A divisao inteira atribuição é: ", a)
a = 2.0
b = 5.0

#MODULO ATRIBUICAO
a %= b
print("O resto da divisao atribuição é: ", a)
a = 2.0
b = 5.0

#EXPONENCIACAO ATRIBUICAO
a **= b
print("A exponenciacao atribuição é: ", a)


#MAIOR E MENOR POTENCIA DE 2

import sys

# Maior potência de 2 representável em ponto flutuante
maior_potencia_de_2 = sys.float_info.max_exp

# Menor potência de 2 representável em ponto flutuante
menor_potencia_de_2 = sys.float_info.min_exp

print(f"Maior potência de 2 representável: 2^{maior_potencia_de_2}")
print(f"Menor potência de 2 representável: 2^{menor_potencia_de_2}")


#EXEMPLO DE VARIAVEIS IMUTAVEIS

A = 10.2
B = A 
print("A = ", A)
print("e ")
print("B = ", B)
print("Após incrmentar o valor de A em 1 temos que ...")
A += 1.2 
print("A = ", A)
print("enquanto ")
print("B = ", B)

#BUSCANDO METODOS DE INTEIROS
help(float)