class SegmentTree:
    def __init__(self, n, a):
        self.size = 4*n
        self.a = a
        self.tree = [0]*self.size

    def showTree(self):
        print("TREE")
        for i in range(self.size):
            print(self.tree[i])

    def buildTree(self, id, l, r):
        if l == r:
            self.tree[id] = 1

        else:
            mid = (l+r)//2
            self.buildTree(2*id+1, l, mid)
            self.buildTree(2*id+2, mid+1, r)
            self.tree[id] = self.tree[2*id+1] + self.tree[2*id+2]

    def setValue(self, id, l, r, pos, v):
        if pos > r or pos < l:
            return
        if l == r == pos:
            self.tree[id] = v
        else:
            mid = (l+r)//2
            if pos <= mid:
                self.setValue(2*id+1, l, mid, pos, v)
            else:
                self.setValue(2*id+2, mid+1, r, pos, v)
            self.tree[id] = self.tree[2*id+1] + self.tree[2*id+2]

    def getValue(self, id, l, r, sum):
        if l == r and self.tree[id] == sum:
            return l
        else:
            mid = (l+r)//2
            # print("DEMAND", sum)
            # print("LEFT", self.tree[2*id+1])
            # print("RIGHT", self.tree[2*id+2])
            if sum <= self.tree[2*id+2]:
                # print("GO RIGHT FOR", sum)
                # z = input()
                return self.getValue(2*id+2, mid+1, r, sum)
            else:
                # print("GO LEFT FOR", sum-self.tree[2*id+2])
                # z = input()
                return self.getValue(2*id+1, l, mid, sum-self.tree[2*id+2])


n = int(input())
a = list(map(int, input().split()))
sample = [i for i in range(1, n+1)]
res = [0]*n
st = SegmentTree(n, sample)
st.buildTree(0, 0, n-1)

# st.showTree()
for i in range(n-1, -1, -1):
    pos = st.getValue(0, 0, n-1, a[i]+1)
    st.setValue(0, 0, n-1, pos, 0)
    value = sample[pos]
    res[i] = value

print(*res)
