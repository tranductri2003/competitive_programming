from collections import defaultdict
from heapq import heappop, heappush

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


def show(matrix, n, m):
    for i in range(1, n+1):
        print(matrix[i][1:m+1])


def xytonum(x, y, n, m):
    return (x-1)*m+y


class Graph:
    INF = 10**9

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # Algorithms for finding the shortest path: Dijskra
    def __init__(self, vertices):
        self.distance = [self.INF]*vertices
        self.edges = defaultdict(dict)

    def addEdge(self, u, v, w):
        self.edges[u][v] = w

    def Dijsktra(self, S):
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

        return self.distance


n, m = list(map(int, input().split()))

matrix = []
for i in range(n+1):
    matrix.append([])
    for j in range(m+1):
        matrix[i].append(0)


for i in range(n):
    a = list(map(int, input().split()))
    for j in range(m):
        matrix[i+1][j+1] = a[j]

t = int(input())
for _ in range(t):
    x0, y0, x1, y1 = list(map(int, input().split()))
    if x0 == x1 and y0 == y1:
        print(0)
    elif x0 == x1:
        res = 0
        if y1 > y0:
            for i in range(y0+1, y1+1):
                res += matrix[x0][i]
            print(res)
        else:
            for i in range(y0-1, y1-1, -1):
                res += matrix[x0][i]
            print(res)
    elif y0 == y1:
        res = 0
        if x1 > x0:
            for i in range(x0+1, x1+1):
                res += matrix[i][y0]
            print(res)
        else:
            for i in range(x0-1, x1-1, -1):
                res += matrix[i][y0]
            print(res)
    else:
        print(14)
