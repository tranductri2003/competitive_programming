

class SegmentTree:
    def __init__(self, n, a):
        self.size = 4*n
        self.a = a
        self.tree = [0] * self.size

    def showTree(self):
        for i in range(self.size):
            print(self.tree[i], end=" ")

    def buildTree(self, id, l, r):
        if l == r:
            self.tree[id] = self.a[l]
        else:
            m = (l+r)//2
            self.buildTree(id*2+1, l, m)
            self.buildTree(id*2+2, m+1, r)

            self.tree[id] = self.tree[id*2+1] + self.tree[id*2+2]

    def setValue(self, id, l, r, pos, v):
        if pos > r or pos < l:
            return
        if l == r == pos:
            self.tree[id] = v
        else:
            mid = (l+r)//2
            self.setValue(2*id+1, l, mid, pos, v)
            self.setValue(2*id+2, mid+1, r, pos, v)

            self.tree[id] = self.tree[2*id+1] + self.tree[2*id+2]

    def getValue(self, id, l, r, u, v):
        sum = 0
        if u > r or v < l:
            return 0
        if u <= l and r <= v:
            sum += self.tree[id]
        else:
            mid = (l+r)//2
            sum += self.getValue(2*id+1, l, mid, u, v)
            sum += self.getValue(2*id+2, mid+1, r, u, v)

        return sum


n, q = list(map(int, input().split()))
a = list(map(int, input().split()))

t = SegmentTree(n, a)
t.buildTree(0, 0, n-1)


# t.showTree()

for i in range(q):
    type, u, v = list(map(int, input().split()))
    if type == 1:
        t.setValue(0, 0, n-1, u, v)
    else:
        print(t.getValue(0, 0, n-1, u, v-1))
