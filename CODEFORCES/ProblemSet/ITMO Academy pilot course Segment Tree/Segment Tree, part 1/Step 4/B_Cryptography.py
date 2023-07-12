
class Node:
    def __init__(self, topLeft, topRight, bottomLeft, bottomRight):
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class SegmentTree:
    def __init__(self, n, a):
        self.n = n
        self.size = n*4
        self.a = a
        self.baseMatrix = Node(1, 0, 0, 1)
        self.tree = [self.baseMatrix]*self.size

    def merge(self, nodeA, nodeB):
        topLeft = nodeA.topLeft*nodeB.topLeft + nodeA.topRight*nodeB.bottomLeft
        topRight = nodeA.topLeft*nodeB.topRight + nodeA.topRight*nodeB.bottomRight
        bottomLeft = nodeA.bottomLeft*nodeB.topLeft + nodeA.bottomRight*nodeB.bottomLeft
        bottomRight = nodeA.bottomLeft*nodeB.topRight + \
            nodeA.bottomRight * nodeB.bottomRight
        return Node(topLeft, topRight, bottomLeft, bottomRight)

    def build(self, id, l, r):
        if l == r:
            self.tree[id] = a[l]
        else:
            mid = (l+r)//2
            self.build(2*id+1, l, mid)
            self.build(2*id+2, mid+1, r)
            self.tree[id] = self.merge(self.tree[2*id+1], self.tree[2*id+2])

    def getValue(self, id, l, r, u, v):
        if v < l or u > r:
            return self.baseMatrix
        if u <= l and r <= v:
            return self.tree[id]
        else:
            mid = (l+r)//2
            leftNode = self.getValue(2*id+1, l, mid, u, v)
            rightNode = self.getValue(2*id+2, mid+1, r, u, v)
            return self.merge(leftNode, rightNode)


modulo, n, m = list(map(int, input().split()))
a = []
for _ in range(n):
    topLeft, topRight = list(map(int, input().split()))
    bottomLeft, bottomRight = list(map(int, input().split()))
    space = input()
    a.append(Node(topLeft, topRight, bottomLeft, bottomRight))
st = SegmentTree(n, a)
st.build(0, 0, n-1)

for _ in range(m):
    l, r = list(map(int, input().split()))
    l -= 1
    r -= 1
    temp = st.getValue(0, 0, n-1, l, r)
    print(temp.topLeft % modulo, temp.topRight % modulo)
    print(temp.bottomLeft % modulo, temp.bottomRight % modulo)
    print()
