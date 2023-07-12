class Node:
    def __init__(self, val, lazy):
        self.val = val
        self.lazy = lazy


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.size = 4*n
        self.tree = [Node(0, 0) for _ in range(self.size)]

    def showTree(self):
        print("_____________________________________________")
        for i in range(self.size):
            print(self.tree[i].val)
        print("_____________________________________________")

    def down(self, id):
        t = self.tree[id].lazy
        self.tree[2*id+1].val += t
        self.tree[2*id+1].lazy += t
        self.tree[2*id+2].val += t
        self.tree[2*id+2].lazy += t
        self.tree[id].lazy = 0

    def getValue(self, id, l, r, pos):
        if l == r == pos:
            return self.tree[id].val
        else:
            mid = (l+r)//2
            self.down(id)
            if pos <= mid:
                # print("LEFT")
                return self.getValue(2*id+1, l, mid, pos)
            else:
                # print("RIGHT")
                return self.getValue(2*id+2, mid+1, r, pos)

    def setValue(self, id, l, r, u, v, k):
        if u > r or v < l:
            return
        if u <= l and r <= v:
            self.tree[id].val = k
            self.tree[id].lazy = k
        else:
            mid = (l+r)//2
            self.down(id)
            self.setValue(2*id+1, l, mid, u, v, k)
            self.setValue(2*id+2, mid+1, r, u, v, k)


n, q = list(map(int, input().split()))
st = SegmentTree(n)

for _ in range(q):
    type, *arg = list(map(int, input().split()))
    if type == 1:
        l, r, k = arg[0], arg[1], arg[2]
        r -= 1
        st.setValue(0, 0, n-1, l, r, k)
    else:
        pos = arg[0]
        res = (st.getValue(0, 0, n-1, pos))
        print(res)
    # st.showTree()
