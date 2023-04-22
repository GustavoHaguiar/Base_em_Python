jg1 = jg2 = None
estado = 1
c = 0
NONE = " "
X = "X"
O = "O"

mapaPrint = [[0, 1, 2], 
            [3, 4, 5],
            [6, 7, 8]]

mapa = [[NONE, NONE, NONE], 
        [NONE, NONE, NONE], 
        [NONE, NONE, NONE]]


while jg1 != X or jg1 != O:
    jg1 = input("Jogador-1 [X/O]: ").upper().strip()
    if jg1 == X:
        jg2 = O
        break
    elif jg1 == O:
        jg2 = X
        break
    else:
        print("Opção invalida, escolha uma opção válida!")

print("\n")
print(f"Jogador 1 = {jg1}")
print(f"Jogador 2 = {jg2}")
print("\n")


for i in range(len(mapa)):
    print(f"{mapaPrint[i][0]} | {mapaPrint[i][1]} | {mapaPrint[i][2]}         ", end='')
    print(f"{mapa[i][0]} | {mapa[i][1]} | {mapa[i][2]}")


def verifyLin(matriz):
    for p in matriz:
            if p[0] == p[1]  and p[1] == p[2] and p[0] != NONE:
                print("Jogo acabou")
                return 0
    return 1


def verifyCol(matriz):
    if matriz[0][0] == matriz[1][0] == matriz [2][0] != NONE:
        print("Jogo acabou")
        return 0
    if matriz[0][1] == matriz[1][1] == matriz [2][1] != NONE:
        print("Jogo acabou")
        return 0
    if matriz[0][2] == matriz[1][2] == matriz [2][2] != NONE:
        print("Jogo acabou")
        return 0
    return 1

def verifyDi(matriz):
    if matriz[0][0] == matriz[1][1] == matriz[2][2] != NONE:
        print("Jogo acabou")
        return 0
    elif matriz[0][2] == matriz[1][1] == matriz[2][0] != NONE:
        print("Jogo acabou")
        return 0
    return 1
    

while estado:
    if c % 2 == 0:
        jogada = jg1
    else:
        jogada = jg2
    pos2 = int(input("Escolha uma posição: "))
    
    if pos2 < 3:
        pos1 = 0
    elif pos2 < 6:
        pos1 = 1
    else:
        pos1 = 2
    
    if str(pos2) in '036':
        pos2 = 0
    elif str(pos2) in '147':
        pos2 = 1
    elif str(pos2) in '258':
        pos2 = 2
    
    mapa[pos1][pos2] = jogada

    for i in range(len(mapa)):
        print(f"{mapaPrint[i][0]} | {mapaPrint[i][1]} | {mapaPrint[i][2]}         ", end='')
        print(f"{mapa[i][0]} | {mapa[i][1]} | {mapa[i][2]}")


    if estado:
        estado = verifyLin(mapa)
    if estado:
        estado = verifyCol(mapa)
    if estado:
        estado = verifyDi(mapa)

    c += 1
