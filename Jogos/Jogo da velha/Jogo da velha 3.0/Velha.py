import functions as velha


# declarações

matriz = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
]

fimJogo = False
player1 = ''
player2 = ''
vez = 0


#informações e introdução ao jogo
velha.showInfo()

# entrada do jogador1
player1 = str(input("Player1 [X/O]: ")).upper()

# definição dos jogadores
player1, player2 = velha.verifyPlayers(player1, player2)

# resultado da correção
print(f"Player 1: {player1}\nPlayer 2: {player2}\n")

# loop para fazer jogo funcionar

while fimJogo == False:
    if vez % 2 == 0:
        jgd = player1
    else:
        jgd = player2
    
    # imprime o mapa
    print("Escolha uma posição: \n")
    velha.showMap(matriz, type=True)
    print("\nEstado jogo:")
    velha.showMap(matriz)

    # realiza a jogada
    matriz = velha.jogada(matriz, jgd)

    # resultado da jogada
    velha.showMap(matriz)

    # verifica o fim de jogo
    fimJogo = velha.verifyEnd(matriz)

# ALGUNS BUGS PARA CORRIGIR
