# Faça um programa para imprimir:
    
# 1
# 2   2
# 3   3   3
# .....
# n   n   n   n   n   n  ... n

# para um n informado pelo usuário.

# Use uma função que receba um valor n inteiro como parâmetro e imprima até a n-ésima linha.

# OBS.: Não se esqueça de verificar se o número N recebido é positivo não nulo. Talvez você possa criar uma função pra isso também. ;-)

def verifica_numero (numero):
    if numero <= 0:
        return False
    else:
        return True

def imprimir_numeros (numero):
    for i in range (1, numero + 1):
        for _ in range (i):
            print(i, end = ' ')
        print()

N = int(input('Digite o valor de n: '))
verifica_N = verifica_numero(N)

if verifica_N == True:
    imprimir_numeros(N)