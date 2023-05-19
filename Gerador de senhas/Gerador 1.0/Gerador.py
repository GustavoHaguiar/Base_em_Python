import random


# Caracteres da senha
num = [0,1,2,3,4,5,6,7,8,9]

let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
       'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']

let_m = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
        'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']

sim = ['_', '@', '&']


# variaveis necessarias
senha = ''
tam_senha = 0
all_char = list()
temp = list()
new_senha = list()


# logica do programa

    # gera uma lista temporaria para organização do programa
temp.append(let)
temp.append(num)
temp.append(sim)
temp.append(let_m)
temp.append(sim) # 2 sim porque são poucos

    # adiciona os elementos em uma só lista
for i in temp:
    for j in i:
        all_char.append(j)

    # deleta a variavel temp para melhorar o funcionamento e embaralha os caracteres
del(temp)
# all_char = random.choices(all_char, k=len(all_char))

    # define o tamanho da senha
tam_senha = int(input("Enter tam password [0 to random]: "))
if tam_senha == 0:
    tam_senha = random.randint(4, 12)

    # embaralha novamente a senha
new_senha = random.choices(all_char, k=tam_senha)

    # transforma a senha em string
for i in new_senha:
    senha = senha+str(i)


# retorno para o usuario
print('------------------------------------')
print("Sua senha é: ", end='')
print(senha)
