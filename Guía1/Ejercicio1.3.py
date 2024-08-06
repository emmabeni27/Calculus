import math

numbers = [10**i for i in range(1, 26)]
for i in numbers:
    limit = (1+(1/i))**i
    absolute_error = abs(math.e-limit)
    print(f"N: ", i, "Limite: ", limit, "Error absoluto: ", absolute_error, "Error relativo: ", absolute_error/math.e)

#se ve afectado el valor para n muy grande debido a la aritmética de punto flotante
# habiendo corregido el error del código, el cambio abrupto se puede deber a que en la compu queda 0,0000000001
#pero la compu no llega a leer ese 1 final. Entonces deja desumarlo. No es 0, pasa que no lo suma.