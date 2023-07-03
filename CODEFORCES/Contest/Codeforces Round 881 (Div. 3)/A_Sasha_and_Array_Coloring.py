t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    somau = n//2
    a.sort()
    res = 0
    for i in range(somau):
        res += a[n-1-i]-a[i]
    print(res)
