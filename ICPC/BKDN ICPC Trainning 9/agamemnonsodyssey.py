from collections import defaultdict
from heapq import heappop, heappush


class Graph:
    INF = 10**9
    # Searching Algorithms: DFS, BFS

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.count = defaultdict(lambda: 0)
        self.distance = [self.INF]*vertices
        self.edges = defaultdict(dict)

    def addEdge(self, u, v, w):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.edges[u][v] = w

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

    # 2.DFS from a vertex
    # def DFS(self,vertex):
    #     path=[]
    #     stack=[vertex]
    #     visited=defaultdict(lambda:0)
    #     while len(stack):
    #         u=stack.pop()
    #         if visited[u]==0:
    #             path.append(u)
    #             visited[u]=1
    #             for neighbour in self.graph[u]:
    #                 stack.append(neighbour)
    #     return path

    # 1. Handling A Disconnected Graph:

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

    # 2. BFS from a vertex
    # def BFS(self,vertex):
    #     path=[]
    #     queue=[vertex]
    #     visited=defaultdict(lambda:0)
    #     while len(queue):
    #         u=queue.pop(0)
    #         if visited[u]==0:
    #             path.append(u)
    #             visited[u]=1
    #             for neighbour in self.graph[u]:
    #                 queue.append(neighbour)
    #     return path

    # DFSUtil in case finding Connected components
    def DFSUtilConnect(self, temp, v, visited):
        visited[v] = 1
        # Store the vertex to list
        temp.append(v)
        for neighbour in self.graph[v]:
            if visited[neighbour] == 0:
                # Update the list
                temp = self.DFSUtilConnect(temp, neighbour, visited)
        return temp

    def connectedComponentsDFS(self, numVertex):
        path = []
        visited = defaultdict(lambda: 0)
        for vertex in range(1, numVertex+1):
            if visited[vertex] == 0:
                temp = []
                path.append(self.DFSUtilConnect(temp, vertex, visited))
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
        # Trả về đường đi từ đỉnh S đến u nào đó
        # return trace
        # if u!=S and trace[u]==-1:
        #     return -1 #Không có đường đi
        # else:
        #     path=[]
        #     while u!=-1:
        #         path.append(u)
        #         u=trace[u]
        #     path.reverse()
        #     return path
        return self.distance


n, k = list(map(int, input().split()))
g = Graph(n)
tong = 0
for i in range(n-1):
    u, v, w = list(map(int, input().split()))
    g.addEdge(u, v, w)
    tong += w
if k >= 2:
    print(tong)
else:
    print("Chuwa biet")
