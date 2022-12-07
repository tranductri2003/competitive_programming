t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    check = []
    for i in range(0, n):
        temp = (i+1, a[i])
        check.append(temp)
    check = sorted(check, key=lambda x: x[1])
    prefixSum = [0]
    temp = 0
    for i in range(n):
        temp += check[i][1]
        prefixSum.append(temp)

    kiemtra = [0]*(n+1)
    kiemtra[n] = 1
    for i in range(n-1, 0, -1):
        if prefixSum[i] >= check[i][1]:
            kiemtra[i] = kiemtra[i+1]

    print(kiemtra.count(1))
    data = []
    for i in range(1, n+1):
        if kiemtra[i] == 1:
            data.append(check[i-1][0])
    data.sort()
    print(*data)
