import math
from collections import defaultdict


def check(n):
    if n == 1:
        return 0
    result = n   # Initialize result as n

    # Consider all prime factors
    # of n and for every prime
    # factor p, multiply result with (1 - 1 / p)
    p = 2
    while p * p <= n:

        # Check if p is a prime factor.
        if n % p == 0:

            # If yes, then update n and result
            while n % p == 0:
                n = n // p
            result = result * (p-1)//p
        p = p + 1

    # If n has a prime factor
    # greater than sqrt(n)
    # (There can be at-most one
    # such prime factor)
    if n > 1:
        result -= result // n
  # Since in the set {1,2,....,n-1}, all numbers are relatively prime with n
  # if n is a prime number

    return int(result)


res = defaultdict(lambda: 0)
for i in range(3*10**5+1000):
    res[i] = check(i)


def f(x):
    import math
    ans = 0
    for i in range(1, x):
        if math.gcd(x, i) == 1:
            ans += 1
    return ans


def ff(x, y):
    ans = f(x)
    for i in range(1, y):
        temp = ans
        ans = 2*f(ans)
        if temp == ans:
            return ans

    return ans


def fff(x, y):
    return x+y


for _ in range(int(input())):
    inputX = input()
    inputY = input()
    inputZ = input()

    x = int(inputX[8:-1])
    y = int(inputY[8:-1])
    z = (inputZ[8:-1])
    result = eval(z)
    print(result)
