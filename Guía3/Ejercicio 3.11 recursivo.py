import math


def elegirPunto(dsa, dsb, inicio, fin, alto, bajo):
    if bajo * dsb > 0:
        return inicio
    elif alto * dsa > 0:
        return fin
    else:
        return (inicio + fin) / 2


def derivada_segunda(funcion, x):
    h = 10 ** (-10)
    return (eval(funcion.replace('x', str(x + h)).replace('X', str(x + h))) -
            2 * eval(funcion.replace('x', str(x)).replace('X', str(x))) +
            eval(funcion.replace('x', str(x - h)).replace('X', str(x - h)))) / (h ** 2)


def metodoNewtonRaphson(funcion, error, inicio, fin, punto=None, max_iter=1000, iter=1):
    if punto is None:
        punto = elegirPunto(
            derivada_segunda(funcion, fin),
            derivada_segunda(funcion, inicio),
            inicio, fin,
            eval(funcion.replace('x', str(inicio)).replace('X', str(inicio))),
            eval(funcion.replace('x', str(fin)).replace('X', str(fin)))
        )

    h = 10 ** (-10)
    f = eval(funcion.replace('x', str(punto)).replace('X', str(punto)))
    derivada = (eval(funcion.replace('x', str(punto + h)).replace('X', str(punto + h))) - f) / h

    if derivada == 0:
        raise ValueError("La derivada es cero. El método de Newton-Raphson no puede continuar.")

    nuevo_punto = punto - (f / derivada)

    if abs(f) < error:
        return nuevo_punto

    # Verificar si el nuevo punto está fuera del intervalo
    if nuevo_punto < inicio or nuevo_punto > fin:
        return "El nuevo punto está fuera del intervalo dado."

    if iter >= max_iter:
        return "No se alcanzó la convergencia en el número máximo de iteraciones."

    return metodoNewtonRaphson(funcion, error, inicio, fin, nuevo_punto, max_iter, iter + 1)


# Prueba con los ejemplos
print(metodoNewtonRaphson("x**3 - 2*x**2 - 5", 10 ** (-4), 1, 4))
print(metodoNewtonRaphson("x - math.cos(x)", 10 ** (-4), 0, math.pi / 2))
print(metodoNewtonRaphson("x**3 + 3*x**2 - 1", 10 ** (-4), -4, 0))
print(metodoNewtonRaphson("x - 0.8 - 0.2 * math.sin(x)", 10 ** (-4), 0, math.pi / 2))
