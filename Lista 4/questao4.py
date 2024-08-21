# Faça um programa que receba um número inteiro e mostre o reverso desse número. Nesse programa deve conter uma função que faça essa transformação, que receba o número informado e retorne o número reverso.

# Lembre-se que o print da resposta (do número inverso) deve estar fora da função. E a função deve receber o número informado como parâmetro.

# Por exemplo: 127 -> 721.

def inverter_numero(numero):
    numero_inverso = str(numero)[::-1]
    return numero_inverso

N = int(input('Digite um valor: '))
inverso_N = inverter_numero(N)
print(f"Inverso: {inverso_N}")