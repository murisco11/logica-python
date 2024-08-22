N = int(input('Digite a idade da pessoa: '))

if N > 89:
    print ('Longevo')
elif N > 59:
    print('Pessoa Idosa')
elif N > 18:
    print('Adulto')
elif N > 12:
    print('Adolescente')
elif N > 1:
    print('Criança')
elif N > 0:
    print('Recém nascido')