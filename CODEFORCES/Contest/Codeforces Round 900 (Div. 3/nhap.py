import random

class Node:
    def __init__(self, x):
        self.L = None
        self.R = None
        self.W = random.randint(1, 10**9)
        self.S = 1
        self.V = x
        self.F = False

def size(treap):
    return treap.S if treap else 0

def push(treap):
    if treap and treap.F:
        treap.F = False
        treap.L, treap.R = treap.R, treap.L
        if treap.L:
            treap.L.F ^= 1
        if treap.R:
            treap.R.F ^= 1

def split(treap, k):
    if treap is None:
        return None, None
    push(treap)
    if size(treap.L) < k:
        left, treap.R = treap, split(treap.R, k - size(treap.L) - 1)
        treap.S = size(treap.L) + size(treap.R) + 1
        return left, treap
    else:
        treap.L, right = split(treap.L, k)
        treap.S = size(treap.L) + size(treap.R) + 1
        return treap, right

def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    push(left)
    push(right)
    if left.W < right.W:
        left.R = merge(left.R, right)
        left.S = size(left.L) + size(left.R) + 1
        return left
    else:
        right.L = merge(left, right.L)
        right.S = size(right.L) + size(right.R) + 1
        return right

def print_treap(treap):
    if treap is None:
        return
    push(treap)
    print_treap(treap.L)
    print(treap.V, end='')
    print_treap(treap.R)

n, m = map(int, input().split())
s = input().strip()
treap = None

for i in s:
    treap = merge(treap, Node(i))

for _ in range(m):
    x, y = map(int, input().split())
    A, B = split(treap, x - 1)
    B, C = split(B, y - x + 1)
    B.F ^= 1
    treap = merge(A, merge(B, C))

print_treap(treap)
