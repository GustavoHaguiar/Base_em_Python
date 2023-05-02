from random import randint
from tkinter import *
from tkinter import filedialog
root = Tk()
abre = filedialog.askopenfile(mode='r', title='Select file')
print(abre.name)
root.mainloop()




'''
def criptografar(arq, key):
    pass

def descriptografar(arq, key):
    pass
'''