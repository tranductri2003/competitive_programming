def MEX(mang):
    mang.sort()
    n = len(mang)
    for i in range(0, n):
        if mang[i] != i:
            return i
    return n


for _ in range(int(input())):

    a = list(map(int, input().split()))
    n = a[0]
    a = a[1:]

    for num in a:
        if n <= num <= n*(n-1):
            print("Alice")
            break
    else:
        data = []
        for num in a:
            data.append(num % (n*(n-1)))

        if MEX(data) == 0:
            print("Bob")
        else:
            print("Alice")
