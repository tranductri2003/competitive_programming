from collections import defaultdict
from heapq import heappop, heappush


class Graph:
    INF = 10**9

    def __init__(self):
        self.graph = defaultdict(list)
        self.count = defaultdict(lambda: 0)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # 2.DFS from a vertex
    def DFS(self, vertex):
        path = []
        stack = [vertex]
        visited = defaultdict(lambda: 0)
        while len(stack):
            u = stack.pop()
            if visited[u] == 0:
                path.append(u)
                visited[u] = 1
                for neighbour in self.graph[u]:
                    stack.append(neighbour)
        return path


n, time = list(map(int, input().split()))
a = list(map(int, input().split()))
for _ in range(n-1):
    u, v = list(map(int, input().split()))
