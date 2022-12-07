
t = int(input())
for _ in range(t):
    n = int(input())
    if n == 3:
        print(-1)
    else:
        if n % 2 == 0:
            res = [i for i in range(n, 0, -1)]
        else:
            res = [n, n-1]
            for i in range(1, n-1):
                res.append(i)

        print(*res)
