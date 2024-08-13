def metodoNewtonRaphson(funcion, punto, error):

    h=10**(-10) # si es MUUUCHO MAS GRANDE, lo toma como cero y no puede dividir por cero!

    f = eval(funcion.replace('x', str(punto)).replace('X', str(punto)))
    derivada = (eval(funcion.replace('x', str(punto + h)).replace('X', str(punto + h))) - f) / h

    nuevo_punto = punto-(f/derivada)

    if abs(0-f)<error:
        return nuevo_punto
    else:
        return metodoNewtonRaphson(funcion, nuevo_punto, error)

print(metodoNewtonRaphson("x**3-3", 2, 10**(-4) ))