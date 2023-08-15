import heapq
from collections import defaultdict

class Graph:
    INF = 10**9

    def __init__(self):
        self.graph = defaultdict(list)
        self.weight = defaultdict(lambda: 0)

    def addEdge(self, u, v, w):
        self.graph[u].append(v)
        self.weight[(u, v)] = w

    def dijkstra(self, start, end):
        distances = [self.INF] * (len(self.graph) + 1)
        distances[start] = 0
        heap = [(0, start)]
        while heap:
            current_dist, current_vertex = heapq.heappop(heap)
            if current_dist > distances[current_vertex]:
                continue
            for neighbour in self.graph[current_vertex]:
                weight = self.weight[(current_vertex, neighbour)]
                distance = current_dist + weight
                if distance < distances[neighbour]:
                    distances[neighbour] = distance
                    heapq.heappush(heap, (distance, neighbour))
        return distances[end]

n, m, s, k = map(int, input().split())
g = Graph()

for i in range(m):
    u, v, w = map(int, input().split())
    g.addEdge(u, v, w)

shortest_distance = g.dijkstra(s, k)
print("Đường đi ngắn nhất từ đỉnh", s, "đến đỉnh", k, "là:", shortest_distance)
