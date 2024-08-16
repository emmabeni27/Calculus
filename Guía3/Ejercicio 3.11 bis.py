import math

def metodoNewtonRaphson(funcion, punto, error):

    h=10**(-10) # si es MUUUCHO MAS GRANDE, lo toma como cero y no puede dividir por cero!

    f = eval(funcion.replace('x', str(punto)).replace('X', str(punto)))
    derivada = (eval(funcion.replace('x', str(punto + h)).replace('X', str(punto + h))) - f) / h

    if derivada == 0:
        raise ValueError("La derivada es cero. El método de Newton-Raphson no puede continuar.")

    nuevo_punto = punto-(f/derivada)

    if abs(f)<error:
        return nuevo_punto
    else:
        return metodoNewtonRaphson(funcion, nuevo_punto, error)

print(metodoNewtonRaphson("x**3 - 2*x**2 - 5", 2.5, 10**(-4)))
print(metodoNewtonRaphson("x-math.cos(x)", math.pi/2, 10**(-4)))
print(metodoNewtonRaphson("x**3 + 3*x**2 - 1", -3.5, 10**(-4)))
print(metodoNewtonRaphson("x - 0.8 - 0.2 * math.sin(x)", -1, 10**(-4)))

#2.6906474480285243
#0.7390851332151392
#0.5320888862380143
#0.9643338876952838