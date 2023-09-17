# bibliotecas
from tkinter import *
from tkinter import messagebox
from customtkinter import *
from random import choice, randint


# configurações iniciais
root = CTk()
set_appearance_mode('light')
set_default_color_theme('blue')
root.title('Gerador de versículos')
root.geometry('600x400')

# pegando os versiculos
new_testament = list()
old_testament = list()

new = open(
    "versiculos\\novo testamento\\versiculos.txt",
    "r"
    )
for i in new:
    new_testament.append(i)
new.close()

old = open(
    "versiculos\\velho testamento\\versiculos.txt",
    "r"
    )
for j in old:
    old_testament.append(j)
old.close()


# cria a variavel que vai armazenar a escolha do usuario
escolha = None

# armazena a escolha na variavel globar: escolha
def get_op(choice):
    global escolha
    escolha = choice

# gera o versiculo apos clicar no botao
def executar():
    versiculo_new = choice(new_testament)
    versiculo_old = choice(old_testament)
    aleatorio = randint(1, 2)

    def gerar_aleatorio():
        if aleatorio == 1:
            gerar_novo()
        else:
            gerar_velho()

    def gerar_novo():
        messagebox.showinfo(title='Versiculo', message=versiculo_new)

    def gerar_velho():
        messagebox.showinfo(title='Versiculo', message=versiculo_old)
    
    if escolha == opcoes[0] or escolha == None:
        gerar_aleatorio()
    if escolha == opcoes[1]:
        gerar_novo()
    if escolha == opcoes[2]:
        gerar_velho()

# opcoes de versiculos
opcoes = ['Aleatório', 'Novo testamento', 'Velho testamento']
# tabela par escolha
key = CTkOptionMenu(root, values=opcoes, command=get_op)
key.place(relx=0.5, rely=0.5, anchor=CENTER)

#botao para gerar o versiculo
button = CTkButton(root, text='Gerar versículo', command=executar)
button.place(relx=0.5, rely=0.7, anchor=CENTER)


root.mainloop()