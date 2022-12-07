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

    def DFSUtil(self, vertex, visited, path):
        stack = [vertex]
        while len(stack):
            u = stack.pop()
            if visited[u] == 0:
                path.append(u)
                visited[u] = 1
                for neighbour in self.graph[u]:
                    stack.append(neighbour)
    # 1.Handling A Disconnected Graph:

    def DFS(self, numVertex):
        visited = defaultdict(lambda: 0)
        path = []
        for vertex in range(1, numVertex+1):
            if visited[vertex] == 0:
                self.DFSUtil(vertex, visited, path)
        return path

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


n = int(input())
g = Graph()
for _ in range(n):
    a, b = list(map(int, input().split()))
    g.addEdge(a, b)

path = g.connectedComponentsBFS(n)

data = []

for num in path:
    data.append(len(num))

print(max(data))
