# Escreva um programa que peça ao usuário um numero inteiro N e depois um conjunto de N números. O programa deverá armazenar todos os números lidos numa lista, e então imprimir todos os números, classificando se cada número é primo ou não, no caso se não ser primo o programa também deve imprimir a lista de divisores do número.

# Para verificar se um número é primo ou não, escreva uma função que recebe um número inteiro como parâmetro e retorna a sua lista de divisores. Use o retorno da função para imprimir a saída do programa no formato abaixo:

def obter_divisores(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def verificar_primo(numero):
    divisores = obter_divisores(numero)
    return len(divisores) < 2

N = int(input('Qual o valor de N? '))
numeros = []

print('Digite os valores: ')

for i in range(N):
    numeros.append(int(input('')))

for numero in numeros:
    if verificar_primo(numero):
        print(f'O número {numero} é primo')
    else:
        divisores = obter_divisores(numero)
        print(f'O número {numero} não é primo, os divisores são: {divisores}')