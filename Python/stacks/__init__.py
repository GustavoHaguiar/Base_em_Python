class Stacks:
    def __init__(self):
        pass


    def stack(self, lista, lista2):
        l = lista[:]
        try:
            for i in range(0, len(l)):
                lista2.append(l.pop())
        except:
            print('ocorreu um erro')
        else:
            return lista2


    def add_stack(self, arg):
        lista.append(arg)

if __name__ == "__main__":
    lista = [1,2,3,4,5,6,7]
    lista2 = []
    teste = Stacks()
    teste.stack(lista, lista2)

    print(f'primeira lista: {lista}')
    print(f'lista atualizada: {lista2}')

