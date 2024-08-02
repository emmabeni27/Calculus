import math

numbers = [x for x in range (0, 100000000000000000000000000)]
for i in numbers:
    limit = (1+(1/i))^i
    error = limit/math.e
    print(f"N: ", i, "(1+(1/n))^n: ", limit, "error: ", error)
