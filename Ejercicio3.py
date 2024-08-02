import math

numbers = [10**i for i in range(1, 26)]
for i in numbers:
    limit = (1+(1/i))**i
    error = limit/math.e
    print(f"N: ", i, "(1+(1/n))^n: ", limit, "error absoluto: ", error, "error relativo: ", error/i)
