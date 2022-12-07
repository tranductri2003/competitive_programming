import math

n, m, r = list(map(int, input().split()))
if m * n > r:
    print(0)
else:
    rest = r - m * n
    res = math.comb(rest + n - 1, rest)
    print(res)
