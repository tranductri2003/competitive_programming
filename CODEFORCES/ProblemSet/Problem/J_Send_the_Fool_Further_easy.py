
#?		 /\_/\
#?		(= ._.)
#?		/ >WA \>AC
#//     WELCOME TO MY CODING SPACE
#!      Filename: J_Send_the_Fool_Further_easy.py
#*      Folder: D:\Code\Python\Codeforces\ProblemSet
#?      Author: TranDucTri2003
#TODO   CreatedAt: 2022-05-02 23:55:13



from collections import defaultdict
from heapq import heappop, heappush

class Graph:
    INF=10**9
    #Searching Algorithms: DFS, BFS
    def __init__(self):
        self.graph = defaultdict(list)
        self.edges=defaultdict(lambda:defaultdict(lambda:0))
        self.distance=defaultdict(lambda:0)

        
    #DFS,BFS
    def addEdge(self,u,v,w):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.edges[u][v]=w
        self.edges[v][u]=w

                            
    # 2. BFS from a vertex
    def BFS(self,vertex):
        visited = defaultdict(lambda:0)
        queue=[vertex]
        visited[vertex]=1
        while queue:
            u=queue.pop(0)
            for v in self.graph[u]:
                if visited[v]==0:
                    self.distance[v]=self.distance[u]+self.edges[u][v]
                    queue.append(v)
                    visited[v]=1
        self.distance[0]=0
        return self.distance
 
n=int(input())
g=Graph()

for i in range(n-1):
    u,v,w=list(map(int,input().split()))
    g.addEdge(u,v,w)
    
path=g.BFS(0)
print(max(path.values()))