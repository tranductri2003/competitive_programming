t = int(input())
for _ in range(t):
    stop = False
    n = int(input())
    a = list(map(int, input().split()))
    sole = 0
    sochan = 0
    for num in a:
        if num % 2 == 1:
            sole += 1
        else:
            sochan += 1

    if sole >= 3:
        res = []
        for i in range(n):
            if a[i] % 2 == 1:
                res.append(i+1)
            if len(res) == 3:
                break
        print("YES")
        print(*res)
    elif sole > 0 and sochan >= 2:
        res = []
        for i in range(n):
            if a[i] % 2 == 1:
                res.append(i+1)
                break
        for i in range(n):
            if a[i] % 2 == 0:
                res.append(i+1)
            if len(res) == 3:
                break
        print("YES")
        print(*res)
    else:
        print("NO")
