t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    first0 = []
    last1 = []
    for num in a:
        first0.append(num)
        last1.append(num)

    # First 0:

    res1 = 0
    if 0 in first0:
        pos = first0.index(0)
        first0[pos] = 1
        num0 = first0.count(0)
        for num in first0:
            if num == 1:
                res1 += num0
            else:
                num0 -= 1

    # Last 1: 0 cuoi cung thanh 1

    res2 = 0
    if 1 in last1:
        for i in range(n-1, -1, -1):
            if last1[i] == 1:
                pos = i
                break
        last1[pos] = 0
        num0 = last1.count(0)
        for num in last1:
            if num == 1:
                res2 += num0
            else:
                num0 -= 1
    res3 = 0

    num0 = a.count(0)
    for num in a:
        if num == 1:
            res3 += num0
        else:
            num0 -= 1

    print(max(res1, res2, res3))
