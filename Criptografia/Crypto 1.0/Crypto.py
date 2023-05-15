from tkinter import *
from tkinter import filedialog
text = ''
root = filedialog.askopenfile(mode='r', title='Select file')
file_root = open(root.name)
file = file_root.readlines()
for lin in file:
    text = text+lin

file_root.close()

def criptografar(arq, key):
    wordCrypto = ''
    for i in arq:
        if i == '\n':
            wordCrypto = wordCrypto+'\n'
        else:    
            i = ord(i) + key
            i = chr(i)
            wordCrypto = wordCrypto+i
    return wordCrypto


def descriptografar(arq, key):
    return criptografar(arq, -key)


def writeArq(text):
    name = filedialog.askopenfile(mode='r', title='Select arq to write')
    obj = open(name.name, 'w')
    obj.writelines(text)
    obj.close()


if __name__ == "__main__":
    key = 2
    palavra = criptografar(text, key)
    new_palavra = descriptografar(palavra, key)
    print('\n')
    print(palavra)
    print('\n\n')
    print(new_palavra)
    writeArq(palavra)