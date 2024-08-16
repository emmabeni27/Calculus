import math


#AJUSTADO PARA CASO DE INTERVALO!!!

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

def metodoNewtonRaphson(funcion, error, inicio, fin):
    h = 10 ** (-10)  # si es MUUUCHO MAS GRANDE, lo toma como cero y no puede dividir por cero!

    #verificaciones
    #1) derivada distinta de cero--> se verifica teoricamente, seria un for de muuuchos pasos

    bajo = eval(funcion.replace('x', str(inicio)).replace('X', str(inicio)))
    alto = eval(funcion.replace('x', str(fin)).replace('X', str(fin)))


    if bajo*alto > 0:  #2) la funcion cambia de signo en el intervalo
        return "No cumple las condiciones."

    #para elegir el punto
    else:
        dsa = derivada_segunda(funcion, fin)
        dsb = derivada_segunda(funcion, inicio)

        punto = float(elegirPunto(dsa, dsb, inicio, fin, alto, bajo))

        if dsb * dsa < 0:
            # 3) la derivada segunda NO cambia de signo en el intervalo dado
            return "No cumple las condiciones para aplicar Newton-Raphson."

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


