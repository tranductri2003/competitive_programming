def cal(pos, last):
    if pos == 0:
        return 0
    if f[pos][last] != -1:
        return f[pos][last]

    x, y = a[pos][last + 1]
    tmp = cal(pos - 1, last + 1) + c[x][y]
    if last + 2 < len(a[pos]):
        tmp = max(tmp, cal(pos, last + 1))

    f[pos][last] = tmp
    return tmp

n, m, k = map(int, input().split())
c = [[0] * (n + 1) for _ in range(11)]
a = [[] for _ in range(m + 1)]
f = [[-1] * 110 for _ in range(m + 1)]

for i in range(1, n + 1):
    c[i] = list(map(int, input().split()))

for j in range(1, m - k + 2):
    for k in range(j, min(j + k - 1, m) + 1):
        for i in range(1, n + 1):
            a[j].append((i, k))
    a[j].append((0, 0))
    a[j].reverse()

for i in range(m - k + 1, 0, -1):
    cal(i, 0)

print(f[m - k + 1][0])
