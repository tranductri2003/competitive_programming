class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node, start, mid)
            self.build(arr, 2 * node + 1, mid + 1, end)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, start, end, left, right):
        if start > right or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        left_sum = self.query(2 * node, start, mid, left, right)
        right_sum = self.query(2 * node + 1, mid + 1, end, left, right)
        return left_sum + right_sum

    def update(self, node, start, end, idx):
        if start == end:
            self.tree[node] += 1
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                self.update(2 * node, start, mid, idx)
            else:
                self.update(2 * node + 1, mid + 1, end, idx)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]


def count_segments(n, k, a):
    freq = {}
    count = 0
    seg_tree = SegmentTree(a)

    for i in range(n):
        if a[i] not in freq:
            freq[a[i]] = 1
        else:
            freq[a[i]] += 1
        if freq[a[i]] == k:
            seg_tree.update(1, 0, n - 1, i)

    def check_segments(start, end):
        if start > end:
            return
        if seg_tree.query(1, 0, n - 1, start, end) == 0:
            nonlocal count
            count += 1
        mid = (start + end) // 2
        check_segments(start, mid)
        check_segments(mid + 1, end)

    check_segments(0, n - 1)
    return count


# Đọc input từ người dùng
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Gọi hàm và in ra kết quả
result = count_segments(n, k, a)
print(result)
