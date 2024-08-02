inicio = 0.99
fin = 1.01
n_puntos = 101
paso = (fin - inicio) / (n_puntos - 1)  # Calcula el tamaño del paso

# Inicializar el contador y el primer valor de x
i = 0
x = inicio

# Bucle while para generar y procesar los puntos
while i < n_puntos:
    f_val = (x) ** 8 - 8 * (x ** 7) + 28 * (x ** 6) - 56 * (x ** 5) + 70 * (x ** 4) - 56 * (x ** 3) + 28 * (
                x ** 2) - 8 * x + 1
    g_val = (((((((x - 8) * x + 28) * x - 56) * x + 70) * x - 56) * x + 28) * x - 8) * x + 1
    h_val = (x - 1) ** 8

    # Imprimir los valores calculados
    print(f"x = {x}, f(x) = {f_val}, g(x) = {g_val}, h(x) = {h_val}")

    # Incrementar x al siguiente punto
    x += paso
    i += 1
