from collections import defaultdict


class SegmentTree:
    def __init__(self, n, a):
        self.n = n
        self.size = 4*n
        self.a = a
        self.lastPos = defaultdict(lambda: -1)
        self.tree = [0]*self.size
        self.res = [0]*n

    def buildTree(self):
        for i in range(len(self.a)):
            if self.lastPos[self.a[i]] == -1:
                self.lastPos[self.a[i]] = i
            else:
                self.res[self.a[i]-1] = self.getValue(0, 0, self.n-1,
                                                      self.lastPos[self.a[i]], i)
                self.setValue(0, 0, self.n-1, self.lastPos[self.a[i]], 1)

    def setValue(self, id, l, r, pos, v):
        if pos < l or pos > r:
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
st = SegmentTree(2*n, a)
st.buildTree()
for i in range(n):
    print(st.res[i], end=" ")
