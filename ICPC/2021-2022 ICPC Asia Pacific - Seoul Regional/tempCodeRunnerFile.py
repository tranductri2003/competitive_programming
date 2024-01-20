from collections import defaultdict

class Graph:
    INF = 10**9

    # Bipartite graph
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def isBipartite(self, src):
        colorArr = defaultdict(int)
        colorArr[src] = 1
        queue = [src]

        while queue:
            u = queue.pop(0)

            if u not in self.graph:
                continue

            for v in self.graph[u]:
                if colorArr[v] == -1:
                    colorArr[v] = 1 - colorArr[u]
                    queue.append(v)
                elif colorArr[v] == colorArr[u]:
                    return False

        return True

n, m = list(map(int, input().split()))
g = Graph()

for _ in range(m):
    u, v = list(map(int, input().split()))
    g.addEdge(u, v)

print(g.isBipartite(1))
