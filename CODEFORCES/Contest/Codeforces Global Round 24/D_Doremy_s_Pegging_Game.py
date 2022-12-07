import math
n, p = list(map(int, input().split()))

if n == 3:
    print(3)
else:
    print(n*pow(2, n-2) % p)
