class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.size = 4*n
        self.tree = [10**20]*self.size

    def setValue(self, id, l, r, pos, k):
        if l == r == pos:
            self.tree[id] = k
        else:
            mid = (l+r)//2
            if pos <= mid:
                self.setValue(2*id+1, l, mid, pos, k)
            else:
                self.setValue(2*id+2, mid+1, r, pos, k)
            self.tree[id] = min(self.tree[2*id+1], self.tree[2*id+2])

    def getValue(self, id, l, r, u, v, p):
        if v < l or u > r:
            return 0
        if self.tree[id] > p:
            return 0
        else:
            if l == r:
                self.tree[id] = 10**20
                return 1
            else:
                mid = (l+r)//2
                leftNode = self.getValue(2*id+1, l, mid, u, v, p)
                rightNode = self.getValue(2*id+2, mid+1, r, u, v, p)
                self.tree[id] = min(self.tree[id*2+1], self.tree[id*2+2])
                return leftNode+rightNode


n, q = list(map(int, input().split()))
st = SegmentTree(n)
for _ in range(q):
    type, *arg = list(map(int, input().split()))
    if type == 1:
        st.setValue(0, 0, n-1, arg[0], arg[1])
    else:
        print(st.getValue(0, 0, n-1, arg[0], arg[1]-1, arg[2]))
