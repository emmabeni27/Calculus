import numpy as np

inicio=0.99
fin=1.01
paso = (1.01-0.99)/101

x_values = np.linspace(inicio, fin, 101) #me evita hacer un while, la función numpy.linspace divide automáticamente el intervalo en un número especificado de puntos igualmente espaciados.
#versión alternativa con while en OneNote
def f(x):
    f= (x)**8-8*(x**7)+28*(x**6)-56*(x**5)+70*(x**4)-56*(x**3)+28*(x**2)-8*x+1
    return f
def g(x):
    g=(((((((x-8)*x+28)*x-56)*x+70)*x-56)*x+28)*x-8)*x+1
    return g
def h(x):
    h=(x-1)**8
    return h

for key,value in enumerate(x_values):
    print(f(value), " ", g(value), " ", h(value))

#se nota una diferencia significativa de precisión, que se debe a la mayor o menor cantidad de operaciones por función.
#Son todas aproximaciones muy cercanas al 0. Algunas pasan al lado de los negativos.Todo esto manifiesta la inexactitud inherente de la aritmética de punto flotante en las computadoras


