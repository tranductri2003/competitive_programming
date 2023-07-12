class Node:
    def __init__(self, answer, opened, closed):
        self.answer = answer
        self.opened = opened
        self.closed = closed


class SegmentTree:
    def __init__(self, size):
        self.size = 4*size
        self.tree = [Node(0, 0, 0)]*self.size

    def merge(self, nodeA, nodeB):
        matched = min(nodeA.opened, nodeB.closed)
        # print("matched", nodeA.opened, nodeB.closed, matched)
        ans = nodeA.answer + nodeB.answer + matched
        open = nodeA.opened + nodeB.opened - matched
        close = nodeA.closed + nodeB.closed - matched
        # print("res", ans, open, close)
        return Node(ans, open, close)

    def build(self, l, r, i):
        # print("down", i, l, r)
        if l == r:
            if l >= len(s):
                return
            if s[l] == "(":
                self.tree[i] = Node(0, 1, 0)
            if s[l] == ")":
                self.tree[i] = Node(0, 0, 1)
        else:
            mid = (l+r)//2
            self.build(l, mid, 2*i+1)
            self.build(mid+1, r, 2*i+2)

            # print("merge", 2*i+1, self.tree[2*i+1].opened, self.tree[2 *
            #       i+1].closed, self.tree[2*i+1].answer)
            # print("merge", 2*i+2, self.tree[2*i+2].opened, self.tree[2 *
            #       i+2].closed, self.tree[2*i+2].answer)
            self.tree[i] = self.merge(self.tree[2*i+1], self.tree[2*i+2])
            # print("temp", temp.answer, temp.opened, temp.closed)
            # self.tree[i] = temp
            # print("tree[i]", self.tree[i].answer,
            #       self.tree[i].opened, self.tree[i].closed)

    def query(self, l, r, u, v, i):  # find correct brackets from u->v
        if u > r or v < l:
            return Node(0, 0, 0)
        if u <= l and r <= v:
            return self.tree[i]

        mid = (l+r)//2
        leftNode = self.query(l, mid, u, v, 2*i+1)
        rightNode = self.query(mid+1, r, u, v, 2*i+2)

        return self.merge(leftNode, rightNode)


s = input()
n = len(s)
st = SegmentTree(n)
st.build(0, n-1, 0)
# for i in range(len(st.tree)):
#     print(st.tree[i].answer, st.tree[i].opened, st.tree[i].closed)

q = int(input())
for _ in range(q):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1

    ansNode = st.query(0, n-1, u, v, 0)
    print(ansNode.answer*2)

"""

class SegmentTree:
    def __init__(self, size):
        self.size = 4*size
        self.tree = [[0, 0, 0]]*self.size

    def merge(self, nodeA, nodeB):
        matched = min(nodeA[1], nodeB[2])
        # print("matched", nodeA[1], nodeB[2], matched)
        ans = nodeA[0] + nodeB[0] + matched
        open = nodeA[1] + nodeB[1] - matched
        close = nodeA[2] + nodeB[2] - matched
        # print("res", ans, open, close)
        return [ans, open, close]

    def build(self, l, r, i):
        # print("down", i, l, r)
        if l == r:
            if l >= len(s):
                return
            if s[l] == "(":
                self.tree[i] = [0, 1, 0]
            if s[l] == ")":
                self.tree[i] = [0, 0, 1]
        else:
            mid = (l+r)//2
            self.build(l, mid, 2*i+1)
            self.build(mid+1, r, 2*i+2)

            # print("merge", 2*i+1, self.tree[2*i+1][1], self.tree[2 *
            #       i+1][2], self.tree[2*i+1][0])
            # print("merge", 2*i+2, self.tree[2*i+2][1], self.tree[2 *
            #       i+2][2], self.tree[2*i+2][0])
            self.tree[i] = self.merge(self.tree[2*i+1], self.tree[2*i+2])
            # print("temp", temp[0], temp[1], temp[2])
            # self.tree[i] = temp
            # print("tree[i]", self.tree[i][0],
            #       self.tree[i][1], self.tree[i][2])

    def query(self, l, r, u, v, i):  # find correct brackets from u->v
        if u > r or v < l:
            return [0, 0, 0]
        if u <= l and r <= v:
            return self.tree[i]

        mid = (l+r)//2
        leftNode = self.query(l, mid, u, v, 2*i+1)
        rightNode = self.query(mid+1, r, u, v, 2*i+2)

        return self.merge(leftNode, rightNode)


s = input()
n = len(s)
st = SegmentTree(n)
st.build(0, n-1, 0)
# for i in range(len(st.tree)):
#     print(st.tree[i][0], st.tree[i][1], st.tree[i][2])

q = int(input())
for _ in range(q):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1

    ansNode = st.query(0, n-1, u, v, 0)
    print(ansNode[0]*2)

# class Node:
#     def __init__(self, answer, opened, closed):
#         self[0] = answer
#         self[1] = opened
#         self[2] = closed


# class SegmentTree:
#     def __init__(self, size):
#         self.size = 4*size
#         self.tree = [Node(0, 0, 0)]*self.size

#     def merge(self, nodeA, nodeB):
#         matched = min(nodeA[1], nodeB[2])
#         # print("matched", nodeA[1], nodeB[2], matched)
#         ans = nodeA[0] + nodeB[0] + matched
#         open = nodeA[1] + nodeB[1] - matched
#         close = nodeA[2] + nodeB[2] - matched
#         # print("res", ans, open, close)
#         return Node(ans, open, close)

#     def build(self, l, r, i):
#         # print("down", i, l, r)
#         if l == r:
#             if l >= len(s):
#                 return
#             if s[l] == "(":
#                 self.tree[i] = Node(0, 1, 0)
#             if s[l] == ")":
#                 self.tree[i] = Node(0, 0, 1)
#         else:
#             mid = (l+r)//2
#             self.build(l, mid, 2*i+1)
#             self.build(mid+1, r, 2*i+2)

#             # print("merge", 2*i+1, self.tree[2*i+1][1], self.tree[2 *
#             #       i+1][2], self.tree[2*i+1][0])
#             # print("merge", 2*i+2, self.tree[2*i+2][1], self.tree[2 *
#             #       i+2][2], self.tree[2*i+2][0])
#             self.tree[i] = self.merge(self.tree[2*i+1], self.tree[2*i+2])
#             # print("temp", temp[0], temp[1], temp[2])
#             # self.tree[i] = temp
#             # print("tree[i]", self.tree[i][0],
#             #       self.tree[i][1], self.tree[i][2])

#     def query(self, l, r, u, v, i):  # find correct brackets from u->v
#         if u > r or v < l:
#             return Node(0, 0, 0)
#         if u <= l and r <= v:
#             return self.tree[i]

#         mid = (l+r)//2
#         leftNode = self.query(l, mid, u, v, 2*i+1)
#         rightNode = self.query(mid+1, r, u, v, 2*i+2)

#         return self.merge(leftNode, rightNode)


# s = input()
# n = len(s)
# st = SegmentTree(n)
# st.build(0, n-1, 0)
# # for i in range(len(st.tree)):
# #     print(st.tree[i][0], st.tree[i][1], st.tree[i][2])

# q = int(input())
# for _ in range(q):
#     u, v = list(map(int, input().split()))
#     u -= 1
#     v -= 1

#     ansNode = st.query(0, n-1, u, v, 0)
#     print(ansNode[0]*2)

"""
"""
class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.answer = [0] * (4*self.size)
        self.opened = [0] * (4*self.size)
        self.closed = [0] * (4*self.size)

    def build(self, l, r, i):
        # print("down", i, l, r)
        if l == r:
            if l >= len(s):
                return
            if s[l] == "(":
                self.opened[i] = 1
            if s[l] == ")":
                self.closed[i] = 1
        else:
            mid = (l+r)//2
            self.build(l, mid, 2*i+1)
            self.build(mid+1, r, 2*i+2)

            matched = min(self.opened[2*i+1], self.closed[2*i+2])
            self.answer[i] = self.answer[2*i+1] + self.answer[2*i+2] + matched
            self.opened[i] = self.opened[2*i+1] + self.opened[2*i+2] - matched
            self.closed[i] = self.closed[2*i+1] + self.closed[2*i+2] - matched

            # print("temp", temp[0], temp[1], temp[2])
            # self.tree[i] = temp
            # print("tree[i]", self.tree[i][0],
            #       self.tree[i][1], self.tree[i][2])

    def query(self, l, r, u, v, i):  # find correct brackets from u->v
        if u > r or v < l:
            return [0, 0, 0]
        if u <= l and r <= v:
            return [self.answer[i], self.opened[i], self.closed[i]]

        mid = (l+r)//2
        leftNode = self.query(l, mid, u, v, 2*i+1)
        rightNode = self.query(mid+1, r, u, v, 2*i+2)

        matched = min(leftNode[1], rightNode[2])
        answer = leftNode[0] + rightNode[0] + matched
        opened = leftNode[1] + rightNode[1] - matched
        closed = leftNode[2] + rightNode[2] - matched

        return [answer, opened, closed]


s = input()
n = len(s)
st = SegmentTree(n)
st.build(0, n-1, 0)
# for i in range(len(st.tree)):
#     print(st.tree[i][0], st.tree[i][1], st.tree[i][2])

q = int(input())
for _ in range(q):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1

    ansNode = st.query(0, n-1, u, v, 0)
    print(ansNode[0]*2)

# class Node:
#     def __init__(self, answer, opened, closed):
#         self[0] = answer
#         self[1] = opened
#         self[2] = closed


# class SegmentTree:
#     def __init__(self, size):
#         self.size = 4*size
#         self.tree = [Node(0, 0, 0)]*self.size

#     def merge(self, nodeA, nodeB):
#         matched = min(nodeA[1], nodeB[2])
#         # print("matched", nodeA[1], nodeB[2], matched)
#         ans = nodeA[0] + nodeB[0] + matched
#         open = nodeA[1] + nodeB[1] - matched
#         close = nodeA[2] + nodeB[2] - matched
#         # print("res", ans, open, close)
#         return Node(ans, open, close)

#     def build(self, l, r, i):
#         # print("down", i, l, r)
#         if l == r:
#             if l >= len(s):
#                 return
#             if s[l] == "(":
#                 self.tree[i] = Node(0, 1, 0)
#             if s[l] == ")":
#                 self.tree[i] = Node(0, 0, 1)
#         else:
#             mid = (l+r)//2
#             self.build(l, mid, 2*i+1)
#             self.build(mid+1, r, 2*i+2)

#             # print("merge", 2*i+1, self.tree[2*i+1][1], self.tree[2 *
#             #       i+1][2], self.tree[2*i+1][0])
#             # print("merge", 2*i+2, self.tree[2*i+2][1], self.tree[2 *
#             #       i+2][2], self.tree[2*i+2][0])
#             self.tree[i] = self.merge(self.tree[2*i+1], self.tree[2*i+2])
#             # print("temp", temp[0], temp[1], temp[2])
#             # self.tree[i] = temp
#             # print("tree[i]", self.tree[i][0],
#             #       self.tree[i][1], self.tree[i][2])

#     def query(self, l, r, u, v, i):  # find correct brackets from u->v
#         if u > r or v < l:
#             return Node(0, 0, 0)
#         if u <= l and r <= v:
#             return self.tree[i]

#         mid = (l+r)//2
#         leftNode = self.query(l, mid, u, v, 2*i+1)
#         rightNode = self.query(mid+1, r, u, v, 2*i+2)

#         return self.merge(leftNode, rightNode)


# s = input()
# n = len(s)
# st = SegmentTree(n)
# st.build(0, n-1, 0)
# # for i in range(len(st.tree)):
# #     print(st.tree[i][0], st.tree[i][1], st.tree[i][2])

# q = int(input())
# for _ in range(q):
#     u, v = list(map(int, input().split()))
#     u -= 1
#     v -= 1

#     ansNode = st.query(0, n-1, u, v, 0)
#     print(ansNode[0]*2)
"""
