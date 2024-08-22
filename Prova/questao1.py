for_N = int(input('Digite o número de vezes que deve repetir a palavra: '))
for_palavra = input('Qual a palavra para o FOR: ')

while_N = int(input('Digite o número de vezes que deve repetir a palavra: '))
while_palavra = input('Qual a palavra para o FOR: ')

def funcao_for (numero, palavra):
    print('Com FOR:')
    for _ in range (numero):
        print(palavra)

def funcao_while(numero, palavra):
    print()
    print('Com WHILE:')
    i = 0
    while i < numero:
        print(palavra)
        i += 1

funcao_for(for_N, for_palavra)
funcao_while(while_N, while_palavra)