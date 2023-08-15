t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()

    res = 0
    currentRes = 1
    i = 1
    while i < n:
        while i < n and a[i]-a[i-1] <= k:
            currentRes += 1
            i += 1
        res = max(res, currentRes)
        currentRes = 1
        i += 1

    res = max(res, currentRes)
    print(n-res)
