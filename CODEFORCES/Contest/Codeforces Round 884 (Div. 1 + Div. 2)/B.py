t = int(input())
for _ in range(t):
    n = int(input())
    a = [0] * n
    a[0] = 2
    a[n - 1] = 3
    a[n // 2] = 1
    counter = 4
    for i in range(1, n - 1):
        if i == n // 2:
            continue
        a[i] = counter
        counter += 1

    for i in range(n):
        print(a[i], end=" ")
    print()
