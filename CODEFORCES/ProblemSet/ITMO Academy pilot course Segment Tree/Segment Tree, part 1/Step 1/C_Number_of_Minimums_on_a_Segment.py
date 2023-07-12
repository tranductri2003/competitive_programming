class Node:
    def __init__(self, val, cnt):
        self.val = val
        self.cnt = cnt


class SegmentTree:
    def __init__(self, n, a):
        self.size = 4 * n
        self.a = a
        self.tree = [Node(10**9, 0)] * self.size

    def buildTree(self, id, l, r):
        if l == r:
            self.tree[id] = Node(self.a[l], 1)
        else:
            mid = (l + r) // 2
            self.buildTree(2 * id + 1, l, mid)
            self.buildTree(2 * id + 2, mid + 1, r)
            self.mergeNodes(id)

    def mergeNodes(self, id):
        leftNode = self.tree[2 * id + 1]
        rightNode = self.tree[2 * id + 2]

        if leftNode.val < rightNode.val:
            self.tree[id] = Node(leftNode.val, leftNode.cnt)
        elif leftNode.val > rightNode.val:
            self.tree[id] = Node(rightNode.val, rightNode.cnt)
        else:
            self.tree[id] = Node(leftNode.val, leftNode.cnt + rightNode.cnt)

    def setValue(self, id, l, r, pos, v):
        if l == r == pos:
            self.tree[id] = Node(v, 1)
        else:
            mid = (l + r) // 2
            if pos <= mid:
                self.setValue(2 * id + 1, l, mid, pos, v)
            else:
                self.setValue(2 * id + 2, mid + 1, r, pos, v)
            self.mergeNodes(id)

    def query(self, id, l, r, u, v):
        if u > r or v < l:
            return Node(10**9, 0)
        if u <= l and r <= v:
            return self.tree[id]
        else:
            mid = (l + r) // 2
            leftNode = self.query(2 * id + 1, l, mid, u, v)
            rightNode = self.query(2 * id + 2, mid + 1, r, u, v)

            if leftNode.val < rightNode.val:
                return Node(leftNode.val, leftNode.cnt)
            elif leftNode.val > rightNode.val:
                return Node(rightNode.val, rightNode.cnt)
            else:
                return Node(leftNode.val, leftNode.cnt + rightNode.cnt)


n, q = map(int, input().split())
a = list(map(int, input().split()))

t = SegmentTree(n, a)
t.buildTree(0, 0, n - 1)

for _ in range(q):
    op, *args = map(int, input().split())
    if op == 1:
        pos, val = args
        t.setValue(0, 0, n - 1, pos, val)
    elif op == 2:
        l, r = args
        res = t.query(0, 0, n - 1, l, r - 1)
        print(res.val, res.cnt)
