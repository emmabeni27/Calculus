import sympy
import matplotlib.pyplot as plt
import numpy as np

#VERIFICA LA CONTINUIDAD Y OTRAS CONDICIONES PARA QUE SEA UN SPLINE CÚBICO NATURAL ENTRE DOS FUNCIONES INTERPOLADORAS
#LA VERIFICACIÓN ES "A TROZOS"

def interpolación(f, g, punto, funciónOrignial = None): #contempla el caso en que no conozco la función original
    if funciónOrignial is None:
        print("¡No se puede verificar interpolación! Función original no disponible")
        continuidad(f, g, punto)
    else:
        x = sympy.symbols('x')
        F = sympy.sympify(f).subs(x, punto)
        G = sympy.sympify(g).subs(x, punto)
        F_O = sympy.sympify(funciónOrignial).subs(x, punto)
        if (F_O == F) and (F_O == G):
            print("Interpola correctamente los valores")
            continuidad(f, g, punto)
        else:
            return False

def continuidad(f, g, punto): #relaizo una verificación "a trozos"
    x = sympy.symbols('x')
    F = sympy.sympify(f).subs(x,punto)
    G = sympy.sympify(g).subs(x,punto)
    if (F!=G):
        print("No verifica continuidad")
        return False
    else:
        print("Verifica continuidad")
        continuidadDP(F, G, punto)

def continuidadDP(F,  G, punto):
    x = sympy.symbols('x')
    Fderivada = sympy.diff(F, x)
    Gderivada = sympy.diff(G, x)
    Fd = sympy.sympify(Fderivada).subs(x, punto)
    Gd = sympy.sympify(Gderivada).subs(x, punto)
    if (Fd!=Gd):
        print("No verifica continuidad en la derivada primera")
        return False
    else:
        print("Verifica continuidad en la derivada primera")
        continuidadDS(Fd, Gd, punto)

def continuidadDS(Fd, Gd, punto):
    x = sympy.symbols('x')
    Fdsegunda = sympy.diff(Fd, x)
    Gdsegunda = sympy.diff(Gd, x)
    Fds = sympy.sympify(Fdsegunda).subs(x, punto)
    Gds = sympy.sympify(Gdsegunda).subs(x, punto)
    if (Fds != Gds):
        print("No verifica continuidad en la derivada segunda")
        return False
    else:
        print("Verifica continuidad en la derivada segunda")
        gradoPolinomio()

def gradoPolinomio():
    rta = input("¿El grado del polinomio interpolador es 3? Responda S (sí) o N (no): ")
    if (rta=="S"):
        extra()
    elif (rta=="N"):
        print("El polinomio interpolador no cumple la condición de grado k=3")
        return False

def extra(x0, xn):
    f0 = input("Ingrese la F 0 función interpoladora: ")
    fn= input("Ingrese la F n-1 función interpoladora: ")
    x = sympy.symbols('x')
    F0= sympy.sympify(f0).subs(x, x0)
    Fn= sympy.sympify(fn).subs(x, xn)
    if (F0==0) and (Fn==0):
        print("El polinomio se puede interpolar")
        graficos()
        return True
    else:
        ("No es el caso de un spline cúbico natural")
        return False

def graficos(f, g, funcionOriginal):
    x = sympy.symbols('x')
    fGrafico = sympy.lambdify(x, f, 'numpy')
    gGrafico = sympy.lambdify(x, g, 'numpy')
    funcionOriginalGrafico = sympy.lambdify(x, funcionOriginal, 'numpy')


    xN= np.linspace(-2, 2, 10)
    fN= fGrafico(xN)
    gN = gGrafico(xN)
    fON = funcionOriginalGrafico(xN)

    plt.figure(figsize=(10, 6))
    plt.plot(xN, fN, label='Función f(x)', color='green')
    plt.plot(xN, gN, label='Función g(x)', color='red')
    plt.plot(xN, fON, label='Función funionOriginal(x)', color='yellow')

    plt.show()