t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = 0
    c = [0] * 32

    for i in a:
        x ^= i
        for j in range(31):
            if ((1 << j) & i) == 1:
                c[j] += 1

    if n % 2 == 0:
        for i in range(31):
            if c[i] % 2 == 1:
                for j in b:
                    if ((1 << i) & j) == 1:
                        for k in range(n):
                            a[k] = a[k] | j
                        break
        y = 0
        for i in a:
            y ^= i
        print(y, x)
    else:
        for i in range(31):
            if c[i] % 2 == 0:
                for j in b:
                    if ((1 << i) & j) == 1:
                        for k in range(n):
                            a[k] = a[k] | j
                        break
        y = 0
        for i in a:
            y ^= i
        print(x, y)
