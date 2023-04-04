t = int(input())
for _ in range(t):
    n, c, d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    unique = list(set(a))
    res = 10**19
    unique.sort()
    for i in range(len(unique)):
        res = min(res, d*(unique[i]-1-i)+c*(n-(i+1)))
    print(min(res, c*n+d))
