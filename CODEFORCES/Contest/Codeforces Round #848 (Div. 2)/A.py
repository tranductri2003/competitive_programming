t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(0, n-1):
        if a[i] == -1 and a[i+1] == -1:
            a[i] = 1
            a[i+1] = 1
            break
    print(sum(a))
