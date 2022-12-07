from heapq import heappop, heappush
from collections import defaultdict


def _lis(arr, n):

    global maximum

    if n == 1:
        return 1

    maxEndingHere = 1

    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2]
       IF arr[n-1] is maller than arr[n-1], and max ending with
       arr[n-1] needs to be updated, then update it"""
    for i in range(1, n):
        res = _lis(arr, i)
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
            maxEndingHere = res + 1

    maximum = max(maximum, maxEndingHere)

    return maxEndingHere


def LIS(arr):

    global maximum

    n = len(arr)

    maximum = 1

    _lis(arr, n)

    return maximum


class Graph:
    INF = 10**9
    # Searching Algorithms: DFS, BFS

    def __init__(self):
        self.graph = defaultdict(list)
        self.count = defaultdict(lambda: 0)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Algorithms for finding the shortest path: Bellman Ford
    # def __init__(self, vertices):
    #     self.V = vertices # No. of vertices
    #     self.graph = []
    # def addEdge(self, u, v, w):
    #     self.graph.append([u, v, w])

    # Algorithms for finding the shortest path: Dijsktra
    # def __init__(self,vertices):
    #     self.distance=[self.INF]*vertices
    #     self.edges=defaultdict(dict)
    # def addEdge(self,u,v,w):
    #     self.edges[u][v]=w

    # Algorithms for finding the shortest path: Floyd Warshall
    # def __init__(self,vertices):
    #     self.distance=defaultdict(lambda:defaultdict(lambda:self.INF))
    #     self.edges=defaultdict(lambda:defaultdict(lambda:self.INF))
    #     for i in range(1,vertices+1):
    #         self.distance[i][i]=0
    #         self.edges[i][i]=0
    # def addEdge(self,u,v,w):
    #     self.edges[u][v]=w

    # Minimum Spanning Trees: Kruskal's Algorithm
    # def __init__(self, vertices):
    #     self.vertices=vertices
    #     self.graph=[]
    # def addEdge(self,node1,node2,weight):
    #     self.graph.append([node1,node2,weight])

    # Ford-Fulkerson Algorithm for Maximum Flow Problem
    # def __init__(self):
    #     self.edges=defaultdict(lambda:defaultdict(lambda:0))
    # def addEdge(self,u,v,w):
    #     self.edges[u][v]=w

    # Bipatite graph
    # def __init__(self):
    #     self.graph=defaultdict(list)
    # def addEdge(self,u,v):
    #     self.graph[u].append(v)
    #     self.graph[v].append(u)

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


n, p = list(map(int, input().split()))
a = list(map(int, input().split()))

g = Graph()
pos = defaultdict(lambda: 0)
for _ in range(p):
    u, v = list(map(int, input().split()))
    g.addEdge(u-1, v-1)

group = g.connectedComponentsBFS(n-1)
for temp in group:
    data = []
    # print(temp)
    z = len(temp)
    for num in temp:
        data.append(a[num])
    temp.sort()
    data.sort()
    for _ in range(z):
        a[temp[_]] = data[_]
stack = 1
data = []
for i in range(1, n):
    if a[i] > a[i-1]:
        stack += 1
        if i == n-1:
            data.append(stack)
    else:
        data.append(stack)
        stack = 1
        if i == n-1:
            data.append(stack)

print(max(data))
