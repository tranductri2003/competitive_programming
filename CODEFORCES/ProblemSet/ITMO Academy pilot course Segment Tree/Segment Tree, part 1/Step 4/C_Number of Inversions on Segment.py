from collections import defaultdict


class Node:
    def __init__(self, frequency, res):
        self.frequency = frequency
        self.res = res


class SegmentTree:
    def __init__(self, n, a):
        self.n = n
        self.size = 4*n
        self.a = a
        dict = defaultdict(lambda: 0)
        self.tree = [Node(dict, 0)]*self.size

    def showTree(self):
        print("TREE")
        for i in range(self.size):
            print(self.tree[i].frequency, self.tree[i].res)

    def merge(self, nodeA, nodeB):
        frequency = defaultdict(lambda: 0)
        res = 0
        for i in range(0, 41):
            frequency[i] = nodeA.frequency[i]+nodeB.frequency[i]
        res = nodeA.res + nodeB.res
        for i in range(0, 41):
            for j in range(i+1, 41):
                res += nodeA.frequency[j]*nodeB.frequency[i]

        return Node(frequency, res)

    def build(self, id, l, r):
        if l == r:
            fre = defaultdict(lambda: 0)
            fre[a[l]] += 1
            self.tree[id] = Node(fre, 0)
        else:
            mid = (l+r)//2
            self.build(2*id+1, l, mid)
            self.build(2*id+2, mid+1, r)
            self.tree[id] = self.merge(self.tree[2*id+1], self.tree[2*id+2])

    def setValue(self, id, l, r, pos, k):
        if l == r == pos:
            fre = defaultdict(lambda: 0)
            fre[k] += 1
            self.tree[id] = Node(fre, 0)
            # self.tree[id].frequency = defaultdict(lambda: 0)
            # self.tree[id].frequency[self.a[l]] += 1
            # self.tree[id].res = 0
        else:
            mid = (l+r)//2
            if pos <= mid:
                self.setValue(2*id+1, l, mid, pos, k)
            else:
                self.setValue(2*id+2, mid+1, r, pos, k)
            self.tree[id] = self.merge(self.tree[2*id+1], self.tree[2*id+2])

    def getValue(self, id, l, r, u, v):
        if u > r or v < l:
            return Node(defaultdict(lambda: 0), 0)
        if u <= l and v >= r:
            return self.tree[id]
        else:
            mid = (l+r)//2
            nodeLeft = self.getValue(2*id+1, l, mid, u, v)
            nodeRight = self.getValue(2*id+2, mid+1, r, u, v)
            return self.merge(nodeLeft, nodeRight)


n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
st = SegmentTree(n, a)
st.build(0, 0, n-1)
for _ in range(q):
    type, *arg = list(map(int, input().split()))
    if type == 2:
        pos, k = arg[0], arg[1]
        pos -= 1
        st.setValue(0, 0, n-1, pos, k)
    else:
        u, v = arg[0], arg[1]
        u -= 1
        v -= 1
        res = st.getValue(0, 0, n-1, u, v)
        print(res.res)
    # st.showTree()
