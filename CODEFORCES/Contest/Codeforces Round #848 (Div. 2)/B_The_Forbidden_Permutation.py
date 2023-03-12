from collections import defaultdict
t = int(input())
for _ in range(t):
    n, m, d = list(map(int, input().split()))
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    pos = defaultdict(lambda: 0)
    for i in range(n):
        pos[p[i]] = i

    if m == 2:
        now = a[0]
        post = a[1]
        if pos[now] <= pos[post]:
            if pos[post]-pos[now] > d:
                res = 0
            else:
                if n-1 >= d+1:
                    res = min(pos[post]-pos[now], d+1-(pos[post]-pos[now]))
                else:
                    res = pos[post]-pos[now]
        else:
            res = 0
    else:
        res = 0
        for i in range(1, m-1):
            now = a[i]
            pre = a[i-1]
            post = a[i+1]
            if (pos[pre] < pos[now] <= pos[pre]+d) or (pos[now] < pos[post] <= pos[now]+d):
                if pos[post]-pos[pre] >= 2*(d+1):
                    res += min(d+1-pos[now]-pos[pre],
                               d+1-pos[post]-pos[now])
                else:
                    res += min(pos[now]-pos[pre], pos[post]-pos[now])
    print(res)
