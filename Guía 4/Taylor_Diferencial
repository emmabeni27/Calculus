import sympy


def Taylor_Diferencial (x0, y0, h, limite, funcion):
    x, y = sympy.symbols('x y')
    F = sympy.sympify(funcion).subs(x, x0)
    print(f"{x0}, {y0}")
    while x0<limite :
        y1 = y0+h*y0*(F+x0)
        x0 = x0 + h
        print(f"{x0}, {y1}")



Taylor_Diferencial()
