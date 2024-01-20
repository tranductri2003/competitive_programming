def build_max(id, l, r):
    if l == r:
        tree_max[id] = a[l].y
        return
    mid = (l + r) // 2
    build_max(id * 2, l, mid)
    build_max(id * 2 + 1, mid + 1, r)
    tree_max[id] = max(tree_max[id * 2], tree_max[id * 2 + 1])

def build_min(id, l, r):
    if l == r:
        tree_min[id] = a[l].y
        return
    mid = (l + r) // 2
    build_min(id * 2, l, mid)
    build_min(id * 2 + 1, mid + 1, r)
    tree_min[id] = min(tree_min[id * 2], tree_min[id * 2 + 1])

def get_max(id, l, r, u, v):
    if r < u or v < l:
        return -1e18
    if u <= l and r <= v:
        return tree_max[id]
    mid = (l + r) // 2
    return max(get_max(id * 2, l, mid, u, v), get_max(id * 2 + 1, mid + 1, r, u, v))

def get_min(id, l, r, u, v):
    if r < u or v < l:
        return 1e18
    if u <= l and r <= v:
        return tree_min[id]
    mid = (l + r) // 2
    return min(get_min(id * 2, l, mid, u, v), get_min(id * 2 + 1, mid + 1, r, u, v))

def left(l, r, val):
    if l == r:
        return l
    mid = (l + r) // 2
    if get_max(1, 0, n - 1, l, mid) > val:
        return left(l, mid, val)
    else:
        return left(mid + 1, r, val)

n = int(input())
a = []

for i in range(n):
    x, y = map(int, input().split())
    a.append((x, y, i))

a.sort(key=lambda x: (x[0], x[1]))
tree_max = [-1e18] * (4 * n)
tree_min = [1e18] * (4 * n)

build_max(1, 0, n - 1)
build_min(1, 0, n - 1)

l, r = [], []

maxn = -1e18
for i in range(n - 1, -1, -1):
    if a[i][1] >= maxn:
        r.append(a[i])
        maxn = a[i][1]

r.sort(key=lambda x: (x[0], x[1]))

minn = 1e18
for i in range(n):
    if a[i][1] <= minn:
        l.append(a[i])
        minn = a[i][1]

l.sort(key=lambda x: (x[0], x[1]))

t1, t2, t3 = [], [], []

for u in l:
    t1.append(u[0])
    t2.append(u[1])

t1.append(1e18)
t2.sort()

res = 0
for u in r:
    pos_min = get_min(1, 0, n - 1, u[2] + 1, n - 1)
    val_max = get_max(1, 0, n - 1, 0, u[2])

    phai = t1.index(u[0])
    phai -= 1
    trai = len(t2) - t2.index(pos_min) - 1

    if val_max > u[1]:
        temp = t1.index(left(0, u[2] - 1, u[1]))
        phai = min(phai, temp)

    res += phai - trai + 1

print(res)
