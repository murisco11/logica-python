# Crie um programa que lê um valor numérico N e que em seguida lê N números. Armazene esses números em uma lista. Em seguida, leia do usuário 3 números inteiros (OP, A e B). O primeiro número (OP) representa uma operação matemática (0 é soma, 1 é multiplicação) que deve ser realizada em cima dos dois números cujas posições (1 a N) na lista são A e B. O programa deve então apresentar a operação e seu resultado.

N = int(input("Qual o N? "))
print ('Digite os valores: ')
numeros = []

for i in range(N):
    numero = float(input(""))
    numeros.append(numero)

simbolo = int(input("Qual a op? "))
A = int(input("Qual o A? "))
B = int(input("Qual o B? "))

indice_A = A - 1
indice_B = B - 1

if simbolo == 0:
    resultado = numeros[indice_A] + numeros[indice_B]
    operacao = "+"
elif simbolo == 1:
    resultado = numeros[indice_A] * numeros[indice_B]
    operacao = "*"

print(str(A) + ' ' + operacao + ' ' + str(B) + ' = ' + str(resultado))