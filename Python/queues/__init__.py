class Queues:
    def __init__(self):
        pass

    def queue(self, lista):
        lista2 = []
        for i in range(len(lista)):
            lista2.append(lista.pop())
        for i in range(0, len(lista2)):
            print(lista2.pop())
    
    def AddInList(self, arg):
        lista.append(arg)

if __name__ == "__main__":
    lista = [2, 4, 6, 8, 0]
    teste = Queues()
    #teste.queue(lista)
    teste.AddInList(19)
    print("\n\nNew List\n\n")
    teste.queue(lista)
