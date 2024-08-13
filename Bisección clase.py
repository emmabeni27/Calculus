def biseccionFor(f, a,b,n):
    #cota
    #while cota<10**(-3)
    for i in range(n):
        raiz = (a+b)/2
        test = f(a)*f(raiz)
        if f(raiz) ==0:
            return(raiz)
        if test>0:
            a=raiz
        else:
            b=raiz
        return(raiz)
def f(x):
    return(x**2)
print("La raiz de f(x) se encuentra en "+ str(biseccionFor(f,0,1.5,10)))