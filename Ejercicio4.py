import math


def limit_sin(h,x):
    value = (math.sin(x+h)-math.sin(x))/h
    return value

def chart_sin():
    range_of_h = [10**(-i) for i in range(1, 26)]
    for h in range_of_h:
        print(f"Sin(X): ", limit_sin(h, 1),"  ",limit_sin(h, 0.5),"  ",limit_sin(h, 0.1), "  ",limit_sin(h, 0.05),"  ",limit_sin(h, 0.01),"  ",limit_sin(h, 0))
    print("END")
chart_sin()

#-----------------------------------------------------------------------------------------------------------------------

def limit_cos(h,x):
    value = (math.cos(x+h)-math.cos(x))/h
    return value

def chart_cos():
    range_of_h = [10**(-i) for i in range(1, 26)]
    for h in range_of_h:
        print(f"Cos(X): ", limit_cos(h, 1),"  ",limit_cos(h, 0.5),"  ",limit_cos(h, 0.1), "  ",limit_cos(h, 0.05),"  ",limit_cos(h, 0.01),"  ",limit_cos(h, 0))
    print("END")

chart_cos()

#-----------------------------------------------------------------------------------------------------------------------

def limit_quadratic(h, x):
    value = ((x + h)**2 - x**2) / h
    return value

def chart_quadratic():
    range_of_h = [10**(-i) for i in range(1, 100)]
    print(range_of_h)
    for h in range_of_h:
        print(f"Quadratic(X): ", limit_quadratic(h, 1),"  ",limit_quadratic(h, 0.5),"  ",limit_quadratic(h, 0.1), "  ",limit_quadratic(h, 0.05),"  ",limit_quadratic(h, 0.01),"  ",limit_quadratic(h, 0)) #para ahorrarme el fstring largo podría construir una lista, usando un for, donde almaceno los valores de la función evaluada y acá los pongeo, pero no me ahorro líneas ni bajo el orden
    print("END")
chart_quadratic()