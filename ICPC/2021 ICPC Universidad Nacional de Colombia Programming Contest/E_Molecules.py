from collections import defaultdict
from heapq import heappop, heappush


class Graph:
    INF = 10**9
    # Searching Algorithms: DFS, BFS

    def __init__(self):
        self.graph = defaultdict(list)
        self.count = defaultdict(lambda: 0)
        self.cnt = defaultdict(lambda: 0)
        self.done = defaultdict(lambda: 0)
        self.visited = defaultdict(lambda: 0)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.cnt[u] += 1
        self.cnt[v] += 1

    # 2.DFS from a vertex

    # def DFS(self, vertex):
    #     stack = [vertex]

    #     res = []
    #     while len(stack):
    #         u = stack.pop()
    #         if visited[u] == 0:
    #             if self.cnt[u] % 2 == 1:
    #                 res.append(u)
    #                 visited[u] = 1
    #                 for neighbour in self.graph[u]:
    #                     stack.append(neighbour)
    #             else:
    #                 if self.done[u]*2 == self.cnt[u]:
    #                     res.append(u)
    #                     visited[u] = 1
    #                     for neighbour in self.graph[u]:
    #                         stack.append(neighbour)
    #                 else:
    #                     for neighbour in self.graph[u]:
    #                         stack.append(neighbour)

    #     return path

    def DFS(self, vertex, path):
        if self.visited[vertex] == 0:
            path.append(u)
            self.visited[u] = 1
            self.DFS(vertex,path)
        return path


g = Graph()

n = int(input())
for _ in range(n-1):
    u, v = list(map(int, input().split()))
    g.addEdge(u, v)
path = []
g.DFS(0, path)
print(path)
