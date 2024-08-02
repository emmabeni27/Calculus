import math
def x1(a,b,c):
    x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    return f"{x1:.4f}"
def x2(a,b,c):
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c))/(2*a)
    return f"{x2:.4f}"

def x1bis(a,b,c):
    inter = float(x2(a,b,c)) #tengo que volver a float para poder operar, pero si pongo float en el return de x1 y x2 pierdo decimales y no me quedan 4 como pide la consigna
    return (c/(a*inter))

print(x1(1, 62.10, 1)) #Efectivamente. Reduzco a 4 decimales un número irracional.
print(x1bis(1, 62.10, 1)) #Aproxima mejor, en parte se debe a que no lo redondeo a 4 decimales! Pero en realidad el problema mayor es estar restando dos núeros MUY cercanos en valor
# con el segundo método me lo evito

def printer():
    bs=[10**x for x in range(1,10)]
    for b in bs:
        print(f"Raíz 1 = {x1(1,b,1)} | Raíz 1 corregida = {x1bis(1,b,1)} | Raíz 2 = {x2(1,b,1)}")
printer()