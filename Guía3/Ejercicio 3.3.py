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
        return "¡El intervalo no contiene raíces! O contiene una cantidad par. Suponiendo que el intervalo sólo contiene una, por el Teorema de Weiertstrass se requiere cambio de signo."

print(métodoBisección(-2, 0, "x**4-2*x**3-4*x**2+4*x+4"))