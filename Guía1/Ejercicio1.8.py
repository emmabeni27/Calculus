import math
def x1(a,b,c):
    x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    return round(x1, 4)
def x2(a,b,c):
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c))/(2*a)
    return round(x2, 4)

def x1bis(a,b,c):
    inter = x2(a,b,c)
    return (c/(a*inter))

print(x1(1, 62.10, 1)) #Efectivamente. Reduzco a 4 decimales un número irracional.
print(x1bis(1, 62.10, 1)) #Aproxima mejor, en parte se debe a que no lo redondeo a 4 decimales! Pero en realidad el problema mayor es estar restando dos núeros MUY cercanos en valor
# con el segundo método me lo evito

