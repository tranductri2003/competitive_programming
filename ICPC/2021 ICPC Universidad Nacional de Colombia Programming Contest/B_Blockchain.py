
while True:
    try:

        n, m = list(map(int, input().split()))
        res = 1
        for _ in range(m):
            w, u, v = list(map(int, input().split()))
            if w % 2 == 1:
                res *= w
        print(res)
    except EOFError:
        break
