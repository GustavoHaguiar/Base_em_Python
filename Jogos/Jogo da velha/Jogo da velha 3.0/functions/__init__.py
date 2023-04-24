from time import sleep

def showMap(matriz, type=False):
    """mostra o mapa <matriz> e tem a opção de mostrá-la vazia caso type == None, 
    no caso de type == True vai ser impresso o mapa do jogo, False retorna a própria matriz.
    Essa função não funciona caso o número de caracteres nas colunas/linhas não seja proporcional."""
    if type == None:
        l = len(matriz)
        c = len(matriz[0])
        new_matriz = []
        for i in range(l):
            linha = []
            for j in range(c):
                linha.append(None)
            new_matriz.append(linha)
    elif type == True:
        l = len(matriz)
        c = len(matriz[0])
        new_matriz = []
        linha = []
        new_matriz = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]
    if type != False:
        for item in new_matriz:
            print(item)
    else:
        for item in matriz:
                print(item)

def showInfo():
    print("---------------------- Jogo da Velha ----------------------")
    print("Regras:\n")
    print("   - Jogador 1 começa o jogo")
    print("   - Ganha quem fizer uma fileira tanto na linear com [X/O]\n")
    print("1")
    sleep(1)
    print("2")
    sleep(1)
    print("3")
    sleep(1)
    print("\t\t\tComeçou!")
    print("-----------------------------------------------------------")

def verifyCol(matriz):
    for i in range(len(matriz)):
        if matriz[0][i] == matriz[1][i] == matriz[2][i] != None:
            return True
    return False
    
def verifyLine(matriz):
    for i in range(len(matriz[0])):
        if matriz[i][0] == matriz[i][1] == matriz[i][2] != None:
            return True
    return False

def verifyDiag(matriz):
    if matriz[0][0] == matriz[1][1] == matriz[2][2] != None:
        return True
    elif matriz[2][0] == matriz[1][1] == matriz[0][2] != None:
        return True
    return False

def verifyVelha(matriz):  ## verifica Velha
    h = 0
    for i in range(3):
        for j in range(3):
            if None == matriz[i][j]:
                h += 1
    if h >= 1:
        return False
    return True

def verifyPlayers(player1, player2):
    if player1 == "X":
        player2 = "O"
    elif player1 == "O":
        player2 = "X"
    if player1 not in "XxOo":
        player1 = "X"
        player2 = "O"
    return player1, player2

def jogada(matriz, player):
    while True: # escolher posição certa    
        posição = int(input("Digite a posição: "))
        if posição < 3 and posição >= 0:
            pos1 = 0
            break
        elif posição < 6 and posição >= 0:
            pos1 = 1
            break
        elif posição < 9 and posição >= 0:
            pos1 = 2
            break
        else:
            print("Escolha uma posição válida")

        
        if str(posição) in '036':
            posição = 0
        elif str(posição) in '147':
            posição = 1
        elif str(posição) in '258':
            posição = 2
        
        if matriz[pos1][posição] == None:
            matriz[pos1][posição] = player
            return matriz

def verifyEnd(matriz):
    fimJogo = False
    if fimJogo == False:
        fimJogo = verifyCol(matriz)
    if fimJogo == False:
        fimJogo = verifyLine(matriz)
    if fimJogo == False:
        fimJogo = verifyDiag(matriz)
    if fimJogo == False:
        fimJogo = verifyVelha(matriz)
    return fimJogo