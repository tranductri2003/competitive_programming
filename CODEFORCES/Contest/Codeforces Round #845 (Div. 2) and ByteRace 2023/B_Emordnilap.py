
t = int(input())
for _ in range(t):
    n = int(input())
    res = n*(n-1)
    for i in range(1, n+1):
        res *= i
        res %= 10**9+7
    print(res)
