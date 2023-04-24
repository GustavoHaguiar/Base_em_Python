def som(*n):
    r = 0
    for i in n:
        r += i
    return r

def sub(r, *n):
    for i in n:
        r -= i
    return r

def div(r, *n):
    for i in n:
        r /= i
    return r

def mult(r, *n):
    for i in n:
        r *= i
    return r

# potenciação
# radiciação
# logaritimo
# mdc
# mmc
# derivada
# integral
# ...