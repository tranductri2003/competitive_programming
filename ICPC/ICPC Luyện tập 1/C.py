import math
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))

    a = [0]*(k+1)
    for i in range(k):
        a[i] = n//k
    for i in range(1, n % k+1):
        a[i] += 1
    res = 0
    for i in range(0, k//2+1):
        if i == 0:
            res += math.comb(a[i], 2)
        elif i == k-i:
            res += math.comb(a[i], 2)
        else:
            res += a[i]*a[k-i]
    print(res)
