class Node:
    def __init__(self, val):
        self.val = val  # giá trị lớn nhất trong đoạn mà nút nắm giữ


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.size = 4*n
        self.tree = [Node(0) for _ in range(self.size)]

    def getValue(self, id, l, r, pos):
        if l == r == pos:
            return self.tree[id].val
        else:
            mid = (l+r)//2
            if pos <= mid:
                return max(self.tree[id].val, self.getValue(2*id+1, l, mid, pos))
            else:
                return max(self.tree[id].val, self.getValue(2*id+2, mid+1, r, pos))

    def setValue(self, id, l, r, u, v, k):
        if u > r or v < l:
            return
        if u <= l and r <= v:
            self.tree[id].val = max(self.tree[id].val, k)
        else:
            mid = (l+r)//2
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
        print(st.getValue(0, 0, n-1, pos))
    # st.showTree()
