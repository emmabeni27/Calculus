import math


def metodoNewtonRaphson(funcion, error, inicio, fin):
    punto = inicio

    h = 10 ** (-10)  # si es MUUUCHO MAS GRANDE, lo toma como cero y no puede dividir por cero!

    f = eval(funcion.replace('x', str(punto)).replace('X', str(punto)))
    derivada = (eval(funcion.replace('x', str(punto + h)).replace('X', str(punto + h))) - f) / h

    if derivada == 0:
        raise ValueError("La derivada es cero. El método de Newton-Raphson no puede continuar.")

    nuevo_punto = punto - (f / derivada)

    if abs(f) < error:
        return nuevo_punto
    else:
        return metodoNewtonRaphson(funcion, error, nuevo_punto, fin)

print(metodoNewtonRaphson("x**3 - 2*x**2 - 5", 10 ** (-4), 1, 4))
print(metodoNewtonRaphson("x-math.cos(x)", 10 ** (-4), 0, math.pi / 2))
print(metodoNewtonRaphson("x**3 + 3*x**2 - 1", 10 ** (-4), -4, 0))
print(metodoNewtonRaphson("x - 0.8 - 0.2 * math.sin(x)", 10 ** (-4), 0, math.pi / 2))

#2.690647448028614
#0.7390851334003724
#0.5320888865181468
#  0.9643338876952231