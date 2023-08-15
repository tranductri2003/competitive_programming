from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = defaultdict(lambda: 0)
    for num in a:
        count[num] += 1
    res = 0
    for i in range(1, n+1):
        currentRes = 0
        j = 1
        while j*j <= i:
            if j*j == i:
                currentRes += count[j]
                break
            else:
                if i % j == 0:
                    currentRes += count[j]
                    currentRes += count[i//j]
            j += 1
        res = max(res, currentRes)
    print(res)
