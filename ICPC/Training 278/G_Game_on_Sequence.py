N = 400005
M = 256

def cmp(x, y):
    return v[x] > v[y]

def gao(x):
    if x != v[a[x]]:
        return True

    q = list(range(M))
    q.sort(key=lambda i: v[i], reverse=True)

    f = [0] * M
    for i in range(M):
        for j in range(8):
            if f[q[i] ^ (1 << j)]:
                break
        if q[i] == a[x]:
            return j < 8
        if j == 8:
            f[q[i]] = 1

n, m = map(int, input().split())
a = [0] * N
v = [0] * (M + 1)

for i, num in enumerate(map(int, input().split()), start=1):
    a[i] = num
    v[num] = i

for _ in range(m):
    op, x = map(int, input().split())
    if op == 1:
        n += 1
        a[v[x]] = n
        v[x] = n
    else:
        result = "Grammy" if gao(x) else "Alice"
        print(result)
