# Escreva um programa que lê a quantidade dos alunos de uma turma. Em seguida, o programa deve ler os nomes de cada aluno e imprimí-los na ordem inversa.

N = int(input("Quanto nomes? "))

nomes = []
novo_nomes = []

for i in range(N):
    nomes.append(input(""))

for i in range(N):
    novo_nomes.append(nomes[N - i - 1])

print("Você digitou: ")

for nome in novo_nomes:
    print(nome)