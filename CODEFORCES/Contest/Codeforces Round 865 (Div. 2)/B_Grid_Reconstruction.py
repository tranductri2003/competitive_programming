from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    res = defaultdict(lambda: defaultdict(lambda: 0))
    temp = 2*n
    res[0][0] = temp
    res[1][n-1] = temp-1
    start = 1
    end = temp-2
    for i in range(0, n-1):
        if i % 2 == 1:
            res[1][i] = end-1
            res[0][i+1] = end
            end -= 2
        else:
            res[1][i] = start
            res[0][i+1] = start+1
            start += 2
    for i in range(0, 2):
        for j in range(0, n):
            print(res[i][j], end=" ")
        print()
