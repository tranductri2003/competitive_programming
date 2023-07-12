t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    res = 0

    data = []
    for i in range(1, n):
        data.append((i, abs(a[i]-a[i-1])))

    data.sort(key=lambda x: -x[1])
    splitData = [0]
    for i in range(k-1):
        splitData.append(data[i][0])
    splitData.append(n)
    print(splitData)
    for i in range(0, len(splitData)-1):
        temp = []
        for j in range(splitData[i], splitData[i+1]):
            temp.append(a[j])
        print(temp)
