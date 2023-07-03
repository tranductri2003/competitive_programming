class Node:
    def __init__(self, answer, opened, closed):
        self.answer = answer
        self.opened = opened
        self.closed = closed


class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [Node(0, 0, 0)]*4*self.size

    def merge(self, nodeA, nodeB):
        matched = min(nodeA.opened, nodeB.closed)
        print(matched)
        ans = nodeA.answer + nodeB.answer + matched
        open = nodeA.opened + nodeB.opened - matched
        close = nodeA.closed + nodeB.closed - matched
        return Node(ans, open, close)

    def build(self, l, r, i):
        if l == r:
            if i >= len(s):
                return
            if s[i] == "(":
                self.tree[i] = Node(0, 1, 0)
            else:
                self.tree[i] = Node(0, 0, 1)
        else:
            mid = (l+r)//2
            self.build(l, mid, 2*i+1)
            self.build(mid+1, r, 2*i+2)

            self.tree[i] = self.merge(self.tree[2*i+1], self.tree[2*i+2])


s = input()
st = SegmentTree(len(s))
st.build(0, len(s), 0)
# for i in range(len(st.tree)):
#     print(st.tree[i].answer)
