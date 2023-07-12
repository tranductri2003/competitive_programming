t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    maxElement = max(a)
    if maxElement <= 0:
        print(maxElement)
    else:
        res = maxElement
        tong = 0
        for i in range(0, n, 2):
            if a[i] >= 0:
                tong += a[i]

        res = max(res, tong)
        tong = 0
        for i in range(1, n, 2):
            if a[i] >= 0:
                tong += a[i]

        res = max(res, tong)
        print(res)
