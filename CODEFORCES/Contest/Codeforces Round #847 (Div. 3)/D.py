from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    check = defaultdict(lambda: 0)
    for num in a:
        check[num] += 1

    res = 0
    data = []
    for num in check:
        data.append((num, check[num]))
    res = data[0][1]
    for i in range(1, len(data)):
        if data[i][0] == data[i-1][0]+1:
            if data[i][1] > data[i-1][1]:
                res += data[i][1]-data[i-1][1]
        else:
            res += data[i][1]
    print(res)
