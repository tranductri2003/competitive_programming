
class SegmentTree:
    def __init__(self, n, a):
        self.size = 4*n
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
            self.setValue(2 * id + 1, l, mid, pos, v)
            self.setValue(2 * id + 2, mid + 1, r, pos, v)
            self.tree[id] = max(self.tree[2*id+1], self.tree[2*id+2])

    def getValue(self, id, l, r, k):
        if l == r and self.tree[id] >= k:
            return l
        else:
            mid = (l+r)//2
            leftMax = self.tree[2*id+1]
            rightMax = self.tree[2*id+2]
            if k > max(leftMax, rightMax):
                return -1

            if leftMax >= k:
                return self.getValue(2*id+1, l, mid, k)
            else:
                return self.getValue(2*id+2, mid+1, r, k)


n, m = map(int, input().split())
a = list(map(int, input().split()))

st = SegmentTree(n, a)
st.buildTree(0, 0, n-1)
# st.showTree()

for _ in range(m):
    type, *arg = map(int, input().split())
    if type == 1:
        pos, v = arg[0], arg[1]
        st.setValue(0, 0, n-1, pos, v)
    else:
        k = arg[0]
        print(st.getValue(0, 0, n-1, k))
