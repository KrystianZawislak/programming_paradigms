from math import isqrt

print(2, end=" ")

for n in range(3, 101, 2):
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            break
    else:
        print(n, end=" ")

print()
