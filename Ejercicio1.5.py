import math


def f(x):
    value=math.sqrt(x**2+1)-1
    return value
def g(x):
    value=(x**2)/(math.sqrt(x**2+1)+1)
    return value

values = [8**-i for i in range(1, 26)]

for value in values:
    print(f"F(x)= ", f(value), "G(x)= ", g(value))

#Los valores de g(x) son más precisos y por tanto más fiables que los de f(x). No se generaun cambio tan brusco en g, el descenso y redondeo es paulatino.

#La diferencia en los resultados de las funciones f(x) y g(x) se debe a la precisión numérica y a los errores de redondeo inherentes a las operaciones en punto flotante en Python. Aunque matemáticamente f(x) y g(x) son equivalentes, las pequeñas diferencias en los resultados se deben a cómo se realizan las operaciones internamente.
#Para determinar cuál de los resultados es más fiable, es importante entender que ambos son correctos dentro de los límites de la precisión numérica de la computadora. Sin embargo, a medida que los valores de x se vuelven muy pequeños, las diferencias se vuelven más notorias debido a la pérdida de precisión.
