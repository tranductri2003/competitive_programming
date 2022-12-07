y = int(input())
if y == 1:
    print(0)
else:

    data = []

    temp = 1
    for i in range(1, 10):
        temp *= i
        data.append(temp)
    res = []
    while y > 0:
        for i in range(8, -1, -1):
            if y >= data[i]:
                time = (y//data[i])
                res += time*[i+1]
                y -= (y//data[i])*data[i]
                break
    res.sort()
    for i in range(len(res)):
        res[i] = str(res[i])

    ans = int("".join(res))
    print(ans)
