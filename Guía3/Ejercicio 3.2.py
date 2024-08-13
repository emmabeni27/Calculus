#MÉTODO DE BISECCIÓN
#tener en cuenta antes q es continua, si, si no se hace largo el codigo (son las tres verificaciones de analisis 1) rango(inicio, fin, punto de paso)

from sympy import symbols, diff

def métodoBisección(inicio, fin, función):

    bajo = eval(función.replace('x', str(inicio)).replace('X', str(inicio)))
    alto = eval(función.replace('x', str(fin)).replace('X', str(fin)))      # no olvidar la función eval!!!


    if(bajo*alto<0):

        promedio = (inicio + fin) / 2
        medio = eval(función.replace('x', str(promedio)).replace('X', str(promedio)))

        if abs(medio) <= (10 ** (-2)):  #si no aclaro que es el absoluto, podría tomar a -0.29 como correcto, que es mayor a 0.01
            return promedio

        elif bajo * medio < 0:
            return métodoBisección(inicio, promedio, función)

        elif medio * alto < 0:
            return métodoBisección(promedio, fin, función)

        else:
            return promedio

    else:
        return "¡El intervalo no contiene raíces! Suponiendo que el intervalo sólo contiene una, por el Teorema de Weiertstrass se requiere cambio de signo."


print(métodoBisección(1, 2, "x**3-x-1"))
