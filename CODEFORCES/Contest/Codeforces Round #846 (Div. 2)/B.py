import math

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    pre = [0]*(n)
    pre[0] = a[0]
    post = [0]*n
    for i in range(1, n):
        pre[i] = pre[i-1]+a[i]
    post[n-1] = a[-1]
    for i in range(n-2, -1, -1):
        post[i] = post[i+1]+a[i]

    res = 0
    for i in range(n-1):
        res = max(res, math.gcd(pre[i], post[i+1]))
    print(res)
