t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    soChan = 0
    soLe = 0
    dataChan = []
    dataLe = []
    data = []
    for num in a:
        if num % 2 == 0:
            soChan += 1
            dataChan.append(num)
        else:
            soLe += 1
            dataLe.append(num)
    dataChan.sort()
    dataLe.sort()

    posChan = 0
    posLe = 0
    for i in range(0, n):
        if a[i] % 2 == 0:
            data.append(dataChan[posChan])
            posChan += 1
        else:
            data.append(dataLe[posLe])
            posLe += 1

    if data == sorted(data):
        print("YES")
    else:
        print("NO")
