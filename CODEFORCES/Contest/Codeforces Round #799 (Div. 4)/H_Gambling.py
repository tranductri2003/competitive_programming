"""
    The idea here is to build a segment tree. Each node stores the left and right
    endpoint of an interval and the sum of that interval. All of the leaves will store
    elements of the array and each internal node will store sum of leaves under it.
    Creating the tree takes O(n) time. Query and updates are both O(log n).
"""

# Segment tree node


class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.max = 0
        self.min = 0
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, mang, n):
        self.a = mang
        self.N = n
        self.INF_MIN = -10**9
        self.INF_MAX = 10**9

        def buildTree(mang, l, r):

            # base case
            if l > r:
                return None

            # leaf node
            if l == r:
                n = Node(l, r)
                n.total = mang[l]
                n.max = mang[l]
                n.min = mang[l]
                return n

            mid = (l+r)//2

            root = Node(l, r)

            # Recursively build the SegmentTree
            root.left = buildTree(mang, l, mid)
            root.right = buildTree(mang, mid+1, r)

            # Total stores the sum of all the leaves under root
            # i.e. those elements lying between (start,end)
            root.total = root.left.total+root.right.total
            root.max = max(root.left.max, root.right.max)
            root.min = min(root.left.min, root.right.min)

            return root
        self.root = buildTree(mang, 0, n-1)

    def updateNode(self, i, val):
        def updateVal(root, i, val):

            # Base case. The actual value will be updated in a leaf.
            # The total is them propogated upwards
            if root.start == root.end:
                root.total = val
                root.max = val
                root.min = val
                return root

            mid = (root.start+root.end)//2

            # If the index is less than the mid, that leaf must be in the left subtree
            if i <= mid:
                updateVal(root.left, i, val)
            # Otherwise, the right subtree
            else:
                updateVal(root.right, i, val)

            # Propogate the changes after recursive call returns
            root.total = root.left.total+root.right.total
            root.max = max(root.left.max, root.right.max)
            root.min = min(root.left.min, root.right.min)

            return root
        return updateVal(self.root, i, val)

    def updateRange(self, u, v, val):  # u,v là đoạn cần update; l,r là biến tạm
        # l=root.start
        # r=root.end
        def updateVal(root, u, v, val):
            if u > root.end or v < root.start:
                return

            # Base case. The actual value will be updated in a leaf.
            # The total is them propogated upwards
            if root.start == root.end:
                root.total += val
                root.max += val
                root.min += val
                return root

            mid = (root.start+root.end)//2
            updateVal(root.left, u, mid, val)
            updateVal(root.right, mid+1, v, val)

            # Propogate the changes after recursive call returns
            root.total = root.left.total+root.right.total
            root.max = max(root.left.max, root.right.max)
            root.min = min(root.left.min, root.right.min)

            return root
        return updateVal(self.root, u, v, val)

    def sumRange(self, i, j):
        def rangeSum(root, i, j):

            # If the range exactly matches the root, we already have the sum
            if root.start == i and root.end == j:
                return root.total

            mid = (root.start+root.end)//2

            # If end of the range is less than the mid, the entire interval lies
            # in the left subtree
            if j <= mid:
                return rangeSum(root.left, i, j)

            # If start of the interval is greater than the mid, the entire interval lies
            # in the right subtree
            elif i >= mid+1:
                return rangeSum(root.right, i, j)

            # Otherwise, the interval is split. So we calculate the sum recursively,
            # by splitting the interval
            else:
                return rangeSum(root.left, i, mid)+rangeSum(root.right, mid+1, j)

        return rangeSum(self.root, i, j)

    def getMax(self, l, r):  # l,r là đoạn lấy giá trị lớn nhất
        def getValue(root, l, r):
            if l > root.end or r < root.start:
                # Đoạn cần cập nhật nằm ngoài khoảng phạm vi của NODE thì ta bỏ qua
                return self.INF_MIN
            if root.start == l and root.end == r:
                return root.max

            mid = (root.start+root.end)//2
            # if r<=mid:
            #     return getValue(root.left,l,r)
            # elif l>=mid+1:
            #     return getValue(root.right,l,r)
            # else:
            return max(getValue(root.left, l, mid), getValue(root.right, mid+1, r))
        return getValue(self.root, l, r)

    def getMin(self, l, r):
        def getValue(root, l, r):
            if l > root.end or r < root.start:
                return self.INF_MAX
            if root.start == l and root.end == r:
                return root.min

            mid = (root.start+root.end)//2
            # if r<=mid:
            #     return getValue(root.left,l,r)
            # elif l>=mid+1:
            #     return getValue(root.right,l,r)
            # else:
            return min(getValue(root.left, l, mid), getValue(root.right, mid+1, r))
        return getValue(self.root, l, r)

# There are several solutions. Here is one.

# If we fix the value of a, then let's make a new array b as follows: bi=1 if roundi=a, and bi=−1 otherwise. Then the total amount of money earned will just be 2bl+⋯+br, so we only need to maximize bl+⋯+br. In other words, we need to find the maximum sum of a subarray. This is a standard problem that can be solved using segment tree.

# Note that we need to iterate over all values of a, of which there are n possibilities. So we have to update elements of the segment tree O(n) times and query once for each a, which means overall the solution runs in O(nlogn).


def maxSubArraySum(a, size):

    max_so_far = a[0]
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0

        # Do not compare for all elements. Compare only
        # when  max_ending_here > 0
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    return max_so_far


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    data = list(set(a))
    res = 0
    for num in data:
        temp = a.copy()
        for i in range(n):
            if temp[i] == num:
                temp[i] = 1
            else:
                temp[i] = -1


def solve(n, x):
    # list of (a, p, l) tuples
    prev = []

    best_p = 0
    best_ans = None

    for r, x_r in enumerate(x):
        curr = []
        seen = False
        for a, p, l in prev:
            if a == x_r:
                curr.append((a, p + 1, l))
                seen = True
            elif p > 1:
                curr.append((a, p - 1, l))

        if not seen:
            curr.append((x_r, 1, r))

        for a, p, l in curr:
            if p > best_p:
                best_p = p
                best_ans = (a, l, r)
        prev = curr

    return best_ans


t = int(input())
for _ in range(t):
    n = int(input())
    x = [int(x) for x in input().split()]
    a, l, r = solve(n, x)
    print(a, l + 1, r + 1)
