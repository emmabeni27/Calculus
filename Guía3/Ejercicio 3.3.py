import matplotlib
import Numba

def métodoBisección(inicio, fin, función):
    promedio = (inicio + fin) / 2

    bajo = eval(función.replace('x', str(inicio)).replace('X', str(inicio)))
    medio = eval(función.replace('x', str(promedio)).replace('X', str(promedio)))
    alto = eval(función.replace('x', str(fin)).replace('X', str(fin)))              # no olvidar la función eval!!!

    if abs(medio) <= (10 ** (-8)):  #si no aclaro que es el absoluto, podría tomar a -0.29 como correcto, que es mayor a 0.01
        #or abs(fin - inicio) <= (10 ** (-8))
        return promedio

    elif bajo * medio < 0:
        return métodoBisección(inicio, promedio, función)

    elif medio * alto < 0:
        return métodoBisección(promedio, fin, función)

    else:
        return promedio #podría pasar que ningún intervalo me devuelva un valor negativo


print(métodoBisección(0, 2, "x**4-2x**3-4x**2+4x+4"))