import math
def algoritmo1(n):
    parcial=3**n
    final=1/parcial
    return final

def algoritmo2(n):
    final = math.exp(-n * math.log(3))
    return final

def algoritmo3(n, t=1):
    if n == 0:
        return t
    else:
        return algoritmo3(n-1, t * (1/3))

print(algoritmo3(3,1))

def algoritmo4(n, t0=1, t1=1/3): #utiliza los dos términos anteriores para calcular el siguiente término en la secuencia. De hecho la estructura recursiva se parece a la de Fibonacci
    if n == 0:
        return t0
    elif n == 1:
        return t1
    else:
        parcial = (13/3) * t1 - (4/3) * t0
    return algoritmo4(n-1, t1, parcial)

#print(algoritmo4(3))

def tabla():
    valores=[x for x in range(1,20)]
    print(f" Algoritmo 1          Algoritmo 2          Algoritmo 3            Algoritmo 4")
    for i in valores:
        print(f"{i}         {algoritmo1(i)}             {algoritmo2(i)}             {algoritmo3(i)}             {algoritmo4(i)}")
tabla()

#El algoritmo 4, por su estructura recursiva de segundo orden da valores más exactos--> MAL en realidad, los más exactos son los otros 3. Al probar en valores más grandes, se van a números negativos, y esto pasa por la pérdida de precisión (error abs). No es así en los otros algoritmos.










def algoritmo5(n, t0=1, t1=1/3):
    if n == 0:
        return t0
    elif n == 1:
        return t1
    else:
        parcial = (13/3) * t1 - (4/3) * t0
    return algoritmo4(n-1, t1, parcial)
#print(algoritmo5(3, 1, 1/3))