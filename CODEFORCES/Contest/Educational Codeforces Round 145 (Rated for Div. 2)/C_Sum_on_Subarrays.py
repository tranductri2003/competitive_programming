import math
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    if k == 0:
        res = [-1000]*n
    else:
        temp = 0
        while temp*(temp+1)//2 < k:
            temp += 1
        if temp*(temp+1)//2 == k:
            res = [1]*temp+[-1000]*(n-temp)
        else:
            d = temp*(temp+1)//2-k
            res = [1]*(temp-d-1)+[2]*d+[-d*2+1]+[-1000]*(n-temp)
    print(*res)

    # 1 1 1 1 1 -1000 -1000
