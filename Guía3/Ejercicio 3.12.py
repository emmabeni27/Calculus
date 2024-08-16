def metodoNewtonRaphson(funcion, punto, error):


    h=10**(-10)

    f = eval(funcion.replace('x', str(punto)).replace('X', str(punto)))
    derivada = (eval(funcion.replace('x', str(punto + h)).replace('X', str(punto + h))) - f) / h

    if derivada == 0: #nunca esta de mas
        raise ValueError("La derivada es cero. El método de Newton-Raphson no puede continuar.")

    nuevo_punto = punto-(f/derivada)

    if abs(0-f)<error:
        return nuevo_punto
    else:
        return metodoNewtonRaphson(funcion, nuevo_punto, error)

print(metodoNewtonRaphson("x**2 -3", 2, 10**(-4)))

#1.7320508075688794