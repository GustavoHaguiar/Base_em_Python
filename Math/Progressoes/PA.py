def pa(a0, n, r):
    return a0 + (n-1) * r

def som_pa(a0, n, r):
    an = pa(a0, n, r)
    soma = (a0+an)*n/2
    return soma
    

