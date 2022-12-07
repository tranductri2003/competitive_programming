from heapq import heappop, heappush
from collections import defaultdict
import sys
import os
from io import BytesIO, IOBase


MOD = 10**9+7
BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


input = sys.stdin.readline


class Graph:
    INF = 10**9

    # Algorithms for finding the shortest path: Dijsktra

    def __init__(self, vertices):
        self.vertice = vertices
        self.distance = [self.INF]*(vertices+1)
        self.edges = defaultdict(dict)

    def addEdge(self, u, v, w):
        self.edges[u][v] = w
        self.edges[v][u] = w

    def Dijsktra(self, S, u, note, check):
        self.distance = [self.INF]*(self.vertice+1)
        self.distance[S] = 0
        queue = [(0, S)]
        trace = defaultdict(lambda: -1)
        while queue:
            cost, vertex = heappop(queue)
            for neighbour, weight in self.edges[vertex].items():
                if cost+weight < self.distance[neighbour]:
                    self.distance[neighbour] = cost+weight
                    heappush(queue, (cost + weight, neighbour))
                    trace[neighbour] = vertex
        path = []
        while u != -1:
            if note[u] == check:
                print(1, end="")
                return
            path.append(u)
            u = trace[u]
        path.reverse()
        print(0, end="")
        return
        # return self.distance


N, M = list(map(int, input().split()))
g = Graph(N)
note = [0]*(N+1)
s = input()
for i in range(N):
    note[i+1] = s[i]

for i in range(N-1):
    u, v = list(map(int, input().split()))
    g.addEdge(u, v, 1)

for i in range(M):
    u, v, c = input().split()
    u = int(u)
    v = int(v)
    g.Dijsktra(u, v, note, c)
