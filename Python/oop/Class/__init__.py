class CommunClass:
    def __init__(self):
        pass

    def getA(self):
        while True:
            try:
                a = int(input("digite um valor para a: "))
            except TypeError:
                print("Tipo invalido! Digite um número inteiro")
            except InterruptedError:
                print("O usuario encerrou o programa...")
            else:
                break
        return a
    
    def getB(self):
        while True:
            try:
                b = int(input("digite um valor para b: "))
            except TypeError:
                print("Tipo invalido! Digite um número inteiro")
            except InterruptedError:
                print("O usuario encerrou o programa...")
            else:
                break
        return b
    
    def sum(self, a, b):
        try:
            c = a+b
            return c
        except ValueError:
            print("Um ou mais parametros são invalidos")
    
    def sub(self, a, b):
        try:
            c = a-b
            return c
        except ValueError:
            print("Um ou mais parametros são invalidos")
    
    def mult(self, a, b):
        try:
            c = a*b
            return c
        except ValueError:
            print("Um ou mais parametros são invalidos")
    
    def div(self, a, b):
        try:
            c = a/b
            return c
        except ValueError:
            print("Um ou mais parametros são invalidos")
        

class equacoes(CommunClass):
    def __init__(self):
       super().__init__()
    
    def equaOne(self):
        try:
            print("Equações do 1° grau são expressas como: ax+b\nDigite o valor para cada variável:")
            a = self.getA()
            x = int(input("Digite um valor para x: "))
            b = self.getB()
            eq = self.sum(self.mult(a, x), b)
            result = eq
        except:
            print("Houve um erro")
        else:
            return f'resultado da equação: {result}'
