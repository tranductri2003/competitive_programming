t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if a != sorted(a):
        print(0)
    else:
        minDis = 10**9
        for i in range(1, n):
            minDis = min(minDis, a[i]-a[i-1])

        print(minDis//2+1)
