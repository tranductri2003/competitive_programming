import math
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    data = []
    if max(a) <= 0:
        for i in range(n-2, -1, -1):
            if a[i] <= a[i+1]:
                continue
            else:
                a[i] += a[i+1]
                res += 1
                data.append((i+1, i+2))
    elif min(a) >= 0:
        for i in range(1, n):
            if a[i] >= a[i-1]:
                pass
            else:
                a[i] += a[i-1]
                res += 1
                data.append((i+1, i))
    else:
        best = max(a)
        for i in range(n):
            if a[i] == best:
                pos = i
                break
        while a[-1] < 0:
            a[-1] += a[pos]
            res += 1
            data.append((n, pos+1))
        for i in range(5):
            a[-1] *= 2
            res += 1
            data.append((n, n))

        for i in range(1, n-1):
            if a[i] >= a[i-1]:
                continue
            else:

                a[i] += a[-1]
                res += 1
                data.append((i+1, n))

                a[-1] *= 2
                res += 1
                data.append((n, n))
    if res > 50:
        while True:
            pass

    print(a)
    print(res)
    for i in range(len(data)):
        print(data[i][0], data[i][1])
