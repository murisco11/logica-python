# Em uma turma de alunos que conversavam muito, um professor montou a seguinte estratégia: após os alunos se sentarem, ele mandava os alunos trocarem de lugar.

# Para ajudar esse processo, crie um programa para ajudar esse professor. O programa deve ler um valor N, que representa a quantidade de alunos. Em seguida, deve ler os nomes de cada aluno e armazená-los em uma lista. Considere a sequência lida como a ordem das cadeiras dos alunos.

# O programa deve então imprimir os nomes em uma nova ordem, trocando os alunos sentados em cadeiras de número par (o da primeira cadeira par vai para a última par, o da segunda para a antepenúltima, etc.).

# Se houver uma quantidade ímpar de cadeiras pares (em uma turma de 7 alunos, vão haver 3 cadeiras pares), o aluno da cadeira central não terá seu local trocado.

def trocar_alunos ():
    N = int(input("Quantos alunos? "))
    print ("Digite os nomes dos alunos: ")    

    nomes = []
    
    for i in range(N):
        nomes.append(input(""))
    
    cadeiras_pares = [i for i in range(1, N, 2)]
    
    nova_ordem = nomes[:]
    
    i = 0
    j = len(cadeiras_pares) - 1
    
    while i < j:
        nova_ordem[cadeiras_pares[i]], nova_ordem[cadeiras_pares[j]] = nova_ordem[cadeiras_pares[j]], nova_ordem[cadeiras_pares[i]]
        i += 1
        j -= 1
    
    print("Nova lista:")
    for nome in nova_ordem:
        print(nome)

trocar_alunos()
