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
    return eval(funcion.replace('x', str(x)).replace('X', str(x)))

def verificaciones( dsa, dsb, bajo, alto):
    if (bajo * alto) > 0 or dsb * dsa < 0:
        return False
    return True #si sale en el return del False, nunca pasa por acá!!!


def metodoNewtonRaphson(funcion, error, inicio, fin, d_s, max_iter=1000): #fijo un maximo de iteraciones permitidas, para el caso en que el metodo no converja

    iter = 0

    h = 10 ** (-10)  # si es MUUUCHO MAS GRANDE, lo toma como cero y no puede dividir por cero!

    bajo = eval(funcion.replace('x', str(inicio)).replace('X', str(inicio)))
    alto = eval(funcion.replace('x', str(fin)).replace('X', str(fin)))

    dsa = derivada_segunda(d_s, fin)
    print(dsa)
    dsb = derivada_segunda(d_s, inicio)

    if not verificaciones(dsa, dsb, bajo, alto):
        return "No cumple las condiciones para aplicar Newton-Raphson."

    punto = float(elegirPunto(dsa, dsb, inicio, fin, alto, bajo)) # para elegir el punto
    print(f"El punto es: {punto}")

    while iter < max_iter:
        f = eval(funcion.replace('x', str(punto)).replace('X', str(punto)))
        derivada = (eval(funcion.replace('x', str(punto + h)).replace('X', str(punto + h))) - f) / h

        if derivada == 0:
            raise ValueError("La derivada es cero. El método de Newton-Raphson no puede continuar.")

        nuevo_punto = punto - (f / derivada)

        if abs(f) < error:
            return nuevo_punto

        if nuevo_punto < inicio or nuevo_punto > fin:
            return "El nuevo punto está fuera del intervalo dado."

        punto = nuevo_punto
        iter+=1



print(metodoNewtonRaphson("x**3 - 2*x**2 - 5", 10 ** (-4), 1, 4, "6*x-4"))
print(metodoNewtonRaphson("x-math.cos(x)", 10 ** (-4), 0, math.pi / 2,"math.cos(x)"))
print(metodoNewtonRaphson("x**3 + 3*x**2 - 1", 10 ** (-4), -4, 0,"6*x+6"))
print(metodoNewtonRaphson("x - 0.8 - 0.2 * math.sin(x)", 10 ** (-4), 0, math.pi / 2,"0.2*math.sin(x)"))