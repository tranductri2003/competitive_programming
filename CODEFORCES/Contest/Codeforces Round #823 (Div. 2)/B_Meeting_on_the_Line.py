

for _ in range((int(input()))):
    n = int(input())
    x = list(map(int, input().split()))
    t = list(map(int, input().split()))

    new = []
    for i in range(n):
        new.append((x[i], t[i]))
    new.sort()
    # print(new)
    prefixSum = [0]

    temp = 0
    for i in range(0, n):
        temp += new[i][0]
        prefixSum.append(temp)
    # print(prefixSum)

    tongmac = sum(t)

    res = 10**9
    pos = 0
    for i in range(n):
        if prefixSum[n]-prefixSum[i+1] - (n-i-1)*x[i]-prefixSum[i]+x[i]*i+tongmac-t[i] < res:
            res = min(res, prefixSum[n]-prefixSum[i+1] -
                      (n-i-1)*x[i]-prefixSum[i]+x[i]*i+tongmac-t[i])
            pos = x[i]
    print(pos)
