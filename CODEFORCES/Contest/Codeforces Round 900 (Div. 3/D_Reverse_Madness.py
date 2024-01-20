import bisect
import random

class Node:
    def __init__(self, x):
        self.L = None
        self.R = None
        self.W = random.randint(0, 10**9)
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
    if not treap:
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
    if not left:
        return right
    if not right:
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
    if not treap:
        return
    push(treap)
    print_treap(treap.L)
    print(treap.V, end='')
    print_treap(treap.R)

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    treap = None

    s = input().strip()

    for i in s:
        treap = merge(treap, Node(i))

    l = list(map(int, input().split()))
    r = list(map(int, input().split()))

    q = int(input())
    x = list(map(int, input().split()))

    for i in x:
        index = bisect.bisect_left(l, i)
        left = min(i, r[index] + l[index] - i)
        right = max(i, r[index] + l[index] - i)

        A, B, C = split(treap, left - 1)
        B.F ^= 1
        treap = merge(A, B)
        B, C = split(treap, right - left + 1)
        B.F ^= 1
        treap = merge(B, C)

    print_treap(treap)
    print()
