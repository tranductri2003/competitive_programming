
def recur(res, x):
    for i in range(x+1, n):
        if n % i == 0 and res[i] % x == 0:
            return i
    return 0


t = int(input())
for _ in range(t):
    n, x = list(map(int, input().split()))
    res = [0]*(n+1)
    res[1] = x
    res[n] = 1
    if n == x:
        for i in range(2, n):
            res[i] = i
        print(*res[1:])
    else:
        for i in range(2, n):
            res[i] = i
        res[x] = n

        if n % x != 0:
            for i in range(x-1, 1):
                if n % i == 0 and res[i] % x == 0:
                    res[i], res[x] = res[x], res[i]
                    print(*res[1:])
                    break
            else:
                print(-1)
        else:
            while recur(res, x) != 0:
                i = recur(res, x)
                res[i], res[x] = res[x], res[i]
                x = i
            print(*res[1:])
