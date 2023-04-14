t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    n -= 1
    res = [0]*(n+1)
    res[0] = a[0]
    res[n] = a[n-1]
    for i in range(n-1):
        res[i+1] = min(a[i], a[i+1])
    print(*res)
