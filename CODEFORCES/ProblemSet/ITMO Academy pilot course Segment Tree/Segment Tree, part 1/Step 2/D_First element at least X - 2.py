class SegmentTree:
    def __init__(self, n, a):
        size = 1
        while size < n:
            size *= 2

        self.size = 2*size
        self.a = a
        self.tree = [0] * (self.size)

    def showTree(self):
        print("TREE")
        for i in range(self.size):
            print(self.tree[i])

    def buildTree(self, id, l, r):
        if l == r:
            self.tree[id] = self.a[l]

        else:
            mid = (l+r)//2
            self.buildTree(2*id+1, l, mid)
            self.buildTree(2*id+2, mid+1, r)
            self.tree[id] = max(self.tree[2*id+1], self.tree[2*id+2])

    def setValue(self, id, l, r, pos, v):
        if pos > r or pos < l:
            return
        if l == r == pos:
            self.tree[id] = v
        else:
            mid = (l + r) // 2
            if pos <= mid:
                self.setValue(2 * id + 1, l, mid, pos, v)
            else:
                self.setValue(2 * id + 2, mid + 1, r, pos, v)
            self.tree[id] = max(self.tree[2*id+1], self.tree[2*id+2])

    def getValue(self, id, l, r, k, index):
        if k > self.tree[id]:
            return -1
        if index > r:
            return -1
        if l == r:
            return l
        else:
            mid = (l+r)//2

            res = self.getValue(2*id+1, l, mid, k, index)
            if res == -1:
                return self.getValue(2*id+2, mid+1, r, k, index)
            else:
                return res


n, m = map(int, input().split())
a = list(map(int, input().split()))

st = SegmentTree(n, a)
st.buildTree(0, 0, n-1)

for _ in range(m):
    type, *arg = map(int, input().split())
    if type == 1:
        pos, v = arg[0], arg[1]
        st.setValue(0, 0, n-1, pos, v)
    else:
        k = arg[0]
        index = arg[1]
        print(st.getValue(0, 0, n-1, k, index))
