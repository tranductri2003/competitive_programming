class Node:
    def __init__(self, sum, pref, suf, seg):
        self.sum = sum
        self.pref = pref  # tổng liên tiếp lớn nhất từ đầu
        self.suf = suf  # tổng liên tiếp lớn nhất từ cuối
        self.seg = seg  # tổng liên tiếp lớn nhất bất kỳ


class SegmentTree:
    def __init__(self, n, a):
        self.size = 4*n
        self.a = a
        self.tree = [Node(0, 0, 0, 0)] * (self.size)

    def showTree(self):
        print("TREE")
        for i in range(self.size):
            print(self.tree[i].sum, self.tree[i].pref,
                  self.tree[i].suf, self.tree[i].seg)

    def mergeNode(self, a, b):
        return Node(
            a.sum + b.sum,
            max(a.pref, a.sum + b.pref),
            max(b.suf, a.suf + b.sum),
            max(a.seg, b.seg, a.suf + b.pref)
        )

    def buildTree(self, id, l, r):
        if l == r:
            if self.a[l] < 0:
                self.tree[id] = Node(self.a[l], 0, 0, 0)
            else:
                self.tree[id] = Node(self.a[l], self.a[l],
                                     self.a[l], self.a[l])
        else:
            mid = (l+r)//2
            self.buildTree(2*id+1, l, mid)
            self.buildTree(2*id+2, mid+1, r)
            self.tree[id] = self.mergeNode(
                self.tree[2*id+1], self.tree[2*id+2])

    def setValue(self, id, l, r, pos, v):
        if pos > r or pos < l:
            return
        if l == r == pos:
            if v < 0:
                self.tree[id] = Node(v, 0, 0, 0)
            else:
                self.tree[id] = Node(v, v,
                                     v, v)
        else:
            mid = (l + r) // 2
            self.setValue(2 * id + 1, l, mid, pos, v)
            self.setValue(2 * id + 2, mid + 1, r, pos, v)
            self.tree[id] = self.mergeNode(
                self.tree[2*id + 1], self.tree[2*id + 2])


n, m = map(int, input().split())
a = list(map(int, input().split()))

st = SegmentTree(n, a)
st.buildTree(0, 0, n-1)

print(st.tree[0].seg)

for _ in range(m):
    i, v = map(int, input().split())
    st.setValue(0, 0, n-1, i, v)
    print(st.tree[0].seg)
