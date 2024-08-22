# Um treinador de voleibol gostaria de manter estatísticas sobre sua equipe. A cada jogo, seu auxiliar anota quantas tentativas de saques, bloqueios e ataques cada um de seus jogadores fez, bem como quantos desses saques, bloqueios e ataques tiveram sucesso (resultaram em pontos). Seu programa deve mostrar qual o percentual de saques, bloqueios e ataques do time todo tiveram sucesso.

#  Formato de entrada

# A primeira entrada é o número de jogadores N (N >= 1). Em seguida, para cada jogador, deve-se se ler uma linha com as seguintes informações: nome do jogador, os valores S, B e A, representam a quantidade de tentativas de saques, bloqueios e ataques; os valores S1, B1 e A1, representando o número de saques, bloqueios e ataques deste jogador que tiveram sucesso.

#Lembre-se de usar LISTA para guardar os valores de cada jogador.

# Formato de saída

# A saída deve mostrar o percentual total de saques, bloqueios e ataques do time todo que resultaram em pontos

def verificar_jogadores():
    N = int(input("Quantidade de jogadores? "))
    
    if N <= 1:
        print('Insira uma quantidade de jogadores válida')
        return 

    print("Digite os dados para cada jogador:")
    
    saques = 0
    bloqueios = 0
    ataques = 0
    saques_ok = 0 
    bloqueios_ok = 0 
    ataques_ok = 0 
    
    for i in range(N):
        info_jogador = input().split()
        saques += int(info_jogador[1])
        bloqueios += int(info_jogador[2])
        ataques += int(info_jogador[3])
        saques_ok += int(info_jogador[4])
        bloqueios_ok += int(info_jogador[5])
        ataques_ok += int(info_jogador[6])
    
        estatistica_saque = round((saques_ok / saques) * 100, 2)
        estatistica_bloqueios = round((bloqueios_ok / bloqueios) * 100, 2)
        estatistica_ataques = round((ataques_ok / ataques) * 100, 2)
    
    print("Pontos de Saque: " + str(estatistica_saque) + ' %')
    print("Pontos de Bloqueio: " + str(estatistica_bloqueios) + ' %')
    print("Pontos de Ataque: " + str(estatistica_ataques) + ' %')
            
verificar_jogadores()