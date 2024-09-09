import sympy
import matplotlib.pyplot as plt
import numpy as np

#VERIFICA LA CONTINUIDAD Y OTRAS CONDICIONES PARA QUE SEA UN SPLINE CÚBICO NATURAL ENTRE DOS FUNCIONES INTERPOLADORAS
#LA VERIFICACIÓN ES "A TROZOS"

def interpolación(f, g, punto, funcionOrignial = None): #contempla el caso en que no conozco la función original
    if funcionOrignial is None:
        print("¡No se puede verificar interpolación! Función original no disponible")
        continuidad(f, g, punto, funcionOrignial)
    else:
        x = sympy.symbols('x')
        F = sympy.sympify(f).subs(x, punto)
        G = sympy.sympify(g).subs(x, punto)
        F_O = sympy.sympify(funcionOrignial).subs(x, punto)
        if (F_O == F) and (F_O == G):
            print("Interpola correctamente los valores")
            continuidad(f, g, punto, funcionOrignial)
        else:
            return False

def continuidad(f, g, punto, funcionOriginal): #relaizo una verificación "a trozos"
    x = sympy.symbols('x')
    F = sympy.sympify(f).subs(x,punto)
    G = sympy.sympify(g).subs(x,punto)
    if (F!=G):
        print(F)
        print(G)
        print("No verifica continuidad")
        return False
    else:
        print("Verifica continuidad")
        continuidadDP(F, G, punto, f, g, funcionOriginal)

def continuidadDP(F,  G, punto, f, g, funcionOriginal):
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
        continuidadDS(Fd, Gd, punto, f, g, funcionOriginal)

def continuidadDS(Fd, Gd, punto, f, g, funcionOriginal):
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
        gradoPolinomio(f, g, funcionOriginal)

def gradoPolinomio(f, g, funcionOriginal):
    rta = input("¿El grado del polinomio interpolador es 3? Responda S (sí) o N (no): ")
    x0 = int(input("Ingrese x0: "))
    xn = int(input("Ingrese xn: "))
    if (rta=="S"):
        extra(x0, xn, f, g, funcionOriginal)
    elif (rta=="N"):
        print("El polinomio interpolador no cumple la condición de grado k=3")
        return False

def extra(x0, xn, f, g, funcionOriginal):
    f0 = input("Ingrese la F 0 función interpoladora: ")
    fn= input("Ingrese la F n-1 función interpoladora: ")
    x = sympy.symbols('x')

    f0derivada = sympy.diff(f0, x)
    fnderivada = sympy.diff(fn, x)

    f0segunda = sympy.diff(f0derivada, x)
    fnsegunda = sympy.diff(fnderivada, x)

    F0= sympy.sympify(f0segunda).subs(x, x0)
    Fn= sympy.sympify(fnsegunda).subs(x, xn)
    print(F0)
    print(Fn)
    if (F0==0) and (Fn==0):
        print("El polinomio se puede interpolar")
        graficos(f, g, funcionOriginal)
        return True
    else:
        print("No es el caso de un spline cúbico natural")
        return False


def graficos(f, g, funcionOriginal):

    if(funcionOriginal!=None):
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

    else:
        print("No se puede graficar")

#NO SE PUEDE INTERPOLAR
#interpolación("(x+1)+(x+1)**3", "3+(x-1)+(x-1)**3", 0)

#SE PUEDE INTERPOLAR, NO GRAFICAR
#interpolación("((-x)**3)/72+(x**2)/24-(19/36)*x+3/2", "(x**3)/72-((x)**2)/8+(7/36)*x+1/2", 2)

#SE PUEDE INTERPOLAR Y GRAFICAR
#interpolación("((-x)**3)/72+(x**2)/24-(19/36)*x+3/2", "(x**3)/72-((x)**2)/8+(7/36)*x+1/2", 2, "1/x")
