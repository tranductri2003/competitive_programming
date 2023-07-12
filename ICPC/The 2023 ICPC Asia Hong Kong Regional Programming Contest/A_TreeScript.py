from collections import defaultdict, deque
from heapq import heappop, heappush


class Graph:
    INF = 10**9
    # Searching Algorithms: DFS, BFS

    def __init__(self):
        self.graph = defaultdict(list)
        self.count = defaultdict(lambda: 0)
        self.maxDepth = defaultdict(lambda: 0)
        self.res = 0

    def addEdge(self, u, v):
        # self.graph[u].append(v)
        self.graph[v].append(u)

    # 1. Handling A Disconnected Graph:

    def DFS(self, vertex):
        path = []
        stack = [vertex]
        visited = defaultdict(lambda: 0)
        while len(stack):
            u = stack.pop()
            if visited[u] == 0:
                path.append(u)
                visited[u] = 1
                if len(self.graph[u]) != 0:
                    self.res += 1
                    for neighbour in self.graph[u]:
                        self.maxDepth[neighbour] = self.maxDepth[u]+1
                        stack.append(neighbour)
        return path
    # 2. BFS from a vertex

    def BFS(self, vertex):
        path = []
        queue = deque()
        queue.append(vertex)
        visited = defaultdict(lambda: 0)
        while len(queue):
            u = queue.popleft()
            if visited[u] == 0:
                path.append(u)
                visited[u] = 1
                if len(self.graph[u]) != 0:
                    self.res += 1
                    for neighbour in self.graph[u]:
                        self.maxDepth[neighbour] = self.maxDepth[u]+1
                        queue.append(neighbour)
        return path


t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    g = Graph()

    for i in range(n):
        g.addEdge(i+1, p[i])

    # print(g.graph)

    (g.BFS(1))
    # print(max(g.maxDepth.values())-3)
    print(g.res-1)
    # print(g.depth_of_tree(1))
    # print(g.graph)
