from collections import defaultdict
from heapq import heappop, heappush


class Graph:
    INF = 10**9
    # Searching Algorithms: DFS, BFS

    def __init__(self):
        self.graph = defaultdict(list)
        self.count = defaultdict(lambda: 0)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BFS(self, numVertex):
        visited = defaultdict(lambda: 0)
        queue = []
        for i in range(1, numVertex+1):
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                while queue:
                    u = queue.pop(0)
                    print(u, end=' ')
                    for v in self.graph[u]:
                        if visited[v] == 0:
                            queue.append(v)
                            visited[v] = 1

    def connectedComponentsBFS(self, numVertex):
        visited = defaultdict(lambda: 0)
        stack = []
        path = []
        for i in range(1, numVertex+1):
            if visited[i] == 0:
                stack.append(i)
                visited[i] = 1
                temp = []
                while stack:
                    u = stack.pop()
                    temp.append(u)
                    for v in self.graph[u]:
                        if visited[v] == 0:
                            stack.append(v)
                            visited[v] = 1
                path.append(temp)
        return path


def xytonum(x, y, n, m):
    return (x-1)*m+y


def show(matrix, n, m):
    for i in range(n+2):
        print(*matrix[i])


n, m = list(map(int, input().split()))
g = Graph()
matrix = []
for i in range(n+2):
    matrix.append([])
    for j in range(m+2):
        matrix[i].append('.')
for i in range(n):
    a = input()
    for j in range(m):
        matrix[i+1][j+1] = a[j]
# show(matrix, n, m)

ban = []
for i in range(1, n+1):
    for j in range(1, m+1):
        if matrix[i][j] == "W":
            now = xytonum(i, j, n, m)
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if matrix[k][l] == "W":
                        then = xytonum(k, l, n, m)
                        g.addEdge(now, then)
        else:
            ban.append(xytonum(i, j, n, m))


path = g.connectedComponentsBFS(n*m)
res = 0
for num in path:
    if len(num) > 1:
        res += 1
    elif len(num) == 1:
        if num[0] not in ban:
            res += 1
print(res)
