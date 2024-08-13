def metodoNewtonRaphson(funcion, punto, error):

    h=10**(-1000)

    f = eval(funcion.replace('x', str(punto)).replace('X', str(punto)))
    derivada = (eval(funcion.replace('x', str(punto + h)).replace('X', str(punto + h))) - f) / h

    nuevo_punto = punto-(f/derivada)
    if abs(0-nuevo_punto)<error:
        return nuevo_punto
    else:
        return metodoNewtonRaphson(funcion, nuevo_punto, error)
