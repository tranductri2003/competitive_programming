class SegmentTree:
    def __init__(self, n, a):
        self.n = n
        self.size = 4*n
        self.a = a
        self.tree = [0]*self.size

    def build(self, id, l, r):
        if l == r:
            if l % 2 == 0:
                self.tree[id] = self.a[l]
            else:
                self.tree[id] = -self.a[l]
        else:
            mid = (l+r)//2
            self.build(2*id+1, l, mid)
            self.build(2*id+2, mid+1, r)
            self.tree[id] = self.tree[2*id+1]+self.tree[2*id+2]

    def setValue(self, id, l, r, pos, k):
        if l == r == pos:
            if l % 2 == 0:
                self.tree[id] = k
            else:
                self.tree[id] = -k
        else:
            mid = (l+r)//2
            if pos <= mid:
                self.setValue(2*id+1, l, mid, pos, k)
            else:
                self.setValue(2*id+2, mid+1, r, pos, k)
            self.tree[id] = self.tree[2*id+1]+self.tree[2*id+2]

    def getValue(self, id, l, r, u, v):
        sum = 0
        if u > r or v < l:
            return 0
        if u <= l and v >= r:
            return self.tree[id]
        else:
            mid = (l+r)//2
            sum += self.getValue(2*id+1, l, mid, u, v)
            sum += self.getValue(2*id+2, mid+1, r, u, v)
        return sum


n = int(input())
a = list(map(int, input().split()))
st = SegmentTree(n, a)
st.build(0, 0, n-1)
q = int(input())
for _ in range(q):
    type, *arg = list(map(int, input().split()))
    if type == 0:
        pos, k = arg[0], arg[1]
        pos -= 1
        st.setValue(0, 0, n-1, pos, k)
    else:
        u, v = arg[0], arg[1]
        u -= 1
        v -= 1
        res = st.getValue(0, 0, n-1, u, v)
        if u % 2 == 1:
            res = -res
        print(res)
