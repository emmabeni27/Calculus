def métodoBisección(inicio, fin, función):
    promedio = (inicio + fin) / 2

    bajo = eval(función.replace('x', str(inicio)).replace('X', str(inicio)))
    medio = eval(función.replace('x', str(promedio)).replace('X', str(promedio)))
    alto = eval(función.replace('x', str(fin)).replace('X', str(fin)))              # no olvidar la función eval!!!

    if abs(medio) <= (10 ** (-2)):  #si no aclaro que es el absoluto, podría tomar a -0.29 como correcto, que es mayor a 0.01
        return promedio

    elif bajo * medio < 0:
        return métodoBisección(inicio, promedio, función)

    elif medio * alto < 0:
        return métodoBisección(promedio, fin, función)

    else:
        return promedio

print(métodoBisección(2, 3, "x**3-25"))