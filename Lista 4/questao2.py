# Faça um programa que leia 4 números inteiros e some somente os números pares. Mostre a soma resultante.

# Esse programa deve conter a seguinte função:

# FUNÇÃO PAR: verifica se um número é par. A função recebe um número inteiro como parâmetro de entrada e retorna 0 (zero) se o valor for par e 1 (um) se o valor for ímpar.

def funcao_par (numero):
    if numero % 2 == 0:
        return 0
    else:
        return 1

soma = 0

for i in range (1, 5, 1):
    numero = (int(input('Digite o número ' + str(i) + ': ')))
    verifica_par = funcao_par(numero)
    if verifica_par == 0:
        soma += numero

print("Soma dos números pares: " + str(soma))