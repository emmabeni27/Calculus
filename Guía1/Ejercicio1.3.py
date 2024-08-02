import math

numbers = [10**i for i in range(1, 26)]
for i in numbers:
    limit = (1+(1/i))**i
    absolute_error = abs(limit/math.e)
    print(f"N: ", i, "Limite: ", limit, "Error absoluto: ", absolute_error, "Error relativo: ", absolute_error/i)

#se ve afectado el valor para n muy grande debido a la aritmética de punto flotante