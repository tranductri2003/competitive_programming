

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = input()

    dsu = DSU(n)

    for _ in range(m):
        l, r = map(int, input().split())
        dsu.union(l - 1, r - 1)

    uniqueStrings = set()
    for i in range(n):
        uniqueStrings.add((dsu.find(i), s[i]))
    print(len(uniqueStrings))
