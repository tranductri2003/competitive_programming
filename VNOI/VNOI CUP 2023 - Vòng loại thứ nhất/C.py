t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort(reverse=True)

    tong = 0
    for i in range(n):
        tong += max(a[i], b[i])
    print(tong)
