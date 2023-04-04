
t = int(input())
for _ in range(t):
    q = int(input())
    minHeight = -10**19
    maxHeight = 10**19
    res = []
    for event in range(q):
        A = list(map(int, input().split()))
        if A[0] == 1:
            a, b, n = A[1:]
            currentMinHeight = (a-b)*(n-2)+a+1
            currentMaxHeight = (a-b)*(n-1)+a
            if n == 1:
                currentMinHeight = 1
                currentMaxHeight = a
            if currentMinHeight > maxHeight or currentMaxHeight < minHeight:
                res.append(0)
            else:
                res.append(1)
                minHeight = max(minHeight, currentMinHeight)
                maxHeight = min(maxHeight, currentMaxHeight)
        else:
            a, b = A[1:]
            leastDay = max(1, (minHeight-b-1)//(a-b)+1)
            mostDay = max(1, (maxHeight-b-1)//(a-b)+1)
            if leastDay == mostDay:
                res.append(leastDay)
            else:
                res.append(-1)
    print(*res)
