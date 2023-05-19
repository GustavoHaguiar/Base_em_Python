class Math:
    def __init__(self, a):
        self.a = a
    
    def getNum(self):
        return self.a

    def __add__(self, *x):
        c = self.a
        for item in x:
            c += item.getNum()
        return c
    
    def __str__(self):
        return f'{self.a}'

if __name__ == "__main__":
    n1 = Math(13)
    n2 = Math(7)
    print(f'primeiro número: {n1}')
    print(f'segundo número: {n2}')
    print('\nSOMA\n')
    print(n1+n2)
    print()