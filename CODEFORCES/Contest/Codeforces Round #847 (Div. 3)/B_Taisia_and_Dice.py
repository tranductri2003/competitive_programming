t = int(input())
for _ in range(t):
    n, s, r = list(map(int, input().split()))
    res = []
    res.append(s-r)
    restN = n-1
    if r % restN == 0:
        for i in range(restN):
            res.append(r//restN)
        print(*res)
    else:
        down = r//restN
        up = down+1
        for i in range(0, restN+1):
            if down*i+up*(restN-i) == r:
                for j in range(i):
                    res.append(down)
                for j in range(restN-i):
                    res.append(up)
                break
        print(*res)
