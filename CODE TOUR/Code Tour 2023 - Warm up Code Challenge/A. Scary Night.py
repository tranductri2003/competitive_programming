s = ""
n, q = 0, 0


def lay(x):
    if x == 'N':
        return 1
    if x == 'E':
        return 2
    if x == 'S':
        return 3
    if x == 'W':
        return 4


class point:
    def __init__(self):
        self.count = [0, 0, 0, 0, 0]


def chuyendoi(a, k):
    temp = point()
    for i in range(1, 5):
        temp.count[(i + k - 1) % 4 + 1] = a.count[i]
    return temp


def down(id):
    if lazy[id] == 0:
        return
    lazy[id * 2] += lazy[id]
    lazy[id * 2 + 1] += lazy[id]
    tree[id * 2] = chuyendoi(tree[id * 2], lazy[id])
    tree[id * 2 + 1] = chuyendoi(tree[id * 2 + 1], lazy[id])
    lazy[id] = 0


def tong(a, b):
    temp = point()
    temp.count[1] = a.count[1] + b.count[1]
    temp.count[2] = a.count[2] + b.count[2]
    temp.count[3] = a.count[3] + b.count[3]
    temp.count[4] = a.count[4] + b.count[4]
    return temp


def build(id, l, r):
    if l == r:
        tree[id].count[lay(s[l])] = 1
        return
    mid = (l + r) // 2
    build(id * 2, l, mid)
    build(id * 2 + 1, mid + 1, r)
    tree[id] = tong(tree[id * 2], tree[id * 2 + 1])


def get(id, l, r, u, v):
    if r < u or v < l:
        temp = point()
        return temp
    if u <= l and r <= v:
        return tree[id]
    down(id)
    mid = (l + r) // 2
    return tong(get(id * 2, l, mid, u, v), get(id * 2 + 1, mid + 1, r, u, v))


def update1(id, l, r, pos, c):
    if l == r:
        for i in range(1, 5):
            if tree[id].count[i]:
                tree[id].count[i] = 0
                tree[id].count[lay(c)] = 1
                return
    down(id)
    mid = (l + r) // 2
    if pos <= mid:
        update1(id * 2, l, mid, pos, c)
    else:
        update1(id * 2 + 1, mid + 1, r, pos, c)
    tree[id] = tong(tree[id * 2], tree[id * 2 + 1])


def update2(id, l, r, u, v, k):
    if r < u or v < l:
        return
    if u <= l and r <= v:
        if k != 0:
            tree[id] = chuyendoi(tree[id], k)
        lazy[id] += k
        return
    down(id)
    mid = (l + r) // 2
    update2(id * 2, l, mid, u, v, k)
    update2(id * 2 + 1, mid + 1, r, u, v, k)
    tree[id] = tong(tree[id * 2], tree[id * 2 + 1])


def check(temp):
    return temp.count[1] == temp.count[3] and temp.count[2] == temp.count[4]


# main function
n, q = map(int, input().split())
s = input()
s = " " + s
tree = [point() for _ in range(10000000)]
lazy = [0] * 10000000

build(1, 1, n)

res = 0
for _ in range(q):
    x = int(input())
    if x == 1:
        vt, c = input().split()
        vt = int(vt)
        update1(1, 1, n, vt, c)
        temp = get(1, 1, n, 1, n)
        if check(temp):
            res += 1
    else:
        l, r, k = map(int, input().split())
        update2(1, 1, n, l, r, k)
        temp = get(1, 1, n, 1, n)
        if check(temp):
            res += 1

print(res)
