class SegmentTree:
    def __init__(self, n, a):
        self.size = 4*n
        self.a = a
        self.tree = [0]*self.size

    def showTree(self):
        print("TREE")
        for i in range(self.size):
            print(self.tree[i], end=" ")

        print()

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

    def getValue(self, id, l, r, u, v):
        sum = 0
        if u > r or v < l:
            return 0
        elif u <= l and r <= v:
            sum += self.tree[id]
        else:
            mid = (l+r)//2
            sum += self.getValue(2*id+1, l, mid, u, v)
            sum += self.getValue(2*id+2, mid+1, r, u, v)

        return sum


n = int(input())
a = list(map(int, input().split()))


data = [0]*(n+1)
st = SegmentTree(n+1, data)
for i in range(n):
    print(st.getValue(0, 0, n, a[i]+1, n), end=" ")
    data[a[i]] += 1
    st.setValue(0, 0, n, a[i], data[a[i]])
