class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.size = 4*n
        self.tree = [0]*self.size

    def showTree(self):
        print("TREE")
        for i in range(self.size):
            print(self.tree[i])

    def setValue(self, id, l, r, pos, k):
        if l == r == pos:
            self.tree[id] += k
        else:
            mid = (l+r)//2
            if pos <= mid:
                self.setValue(2*id+1, l, mid, pos, k)
            else:
                self.setValue(2*id+2, mid+1, r, pos, k)
            self.tree[id] = self.tree[2*id+1]+self.tree[2*id+2]

    def getPrefixSum(self, id, l, r, u, v):
        sum = 0
        if v < l or u > r:
            return 0

        if u <= l and r <= v:
            return self.tree[id]
        else:
            mid = (l+r)//2
            sum += self.getPrefixSum(2*id+1, l, mid, u, v)
            sum += self.getPrefixSum(2*id+2, mid+1, r, u, v)
        return sum


n, q = list(map(int, input().split()))
n += 1
st = SegmentTree(n)
for _ in range(q):
    type, *arg = list(map(int, input().split()))
    if type == 1:
        u, v, k = arg[0], arg[1], arg[2]
        st.setValue(0, 0, n-1, u, k)
        st.setValue(0, 0, n-1, v, -k)
    else:
        pos = arg[0]
        print(st.getPrefixSum(0, 0, n-1, 0, pos))
