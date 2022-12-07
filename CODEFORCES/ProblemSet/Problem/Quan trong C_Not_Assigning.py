from collections import defaultdict
 
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.path = []
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def DFSUtil(self, v,visited):
        visited[v]=1
        self.path.append(v)
        for neighbour in self.graph[v]:
            if visited[neighbour]==0:
                self.DFSUtil(neighbour,visited)
                
    # 1.Handling A Disconnected Graph: 
    # def DFS(self,numVertex):
    #     visited=defaultdict(lambda:0)
    #     for vertex in range(1,numVertex+1):
    #         if visited[vertex]==0:
    #             self.DFSUtil(vertex,visited)        
    # 2.DFS from a vertex 
    def DFS(self,vertex):
        visited=defaultdict(lambda:0)
        self.DFSUtil(vertex,visited)
                
    # 1. Handling A Disconnected Graph:
    def BFS(self,numVertex):
        visited=defaultdict(lambda:0)
        queue=[]
        for i in range(1,numVertex+1):
            if visited[i]==0:
                queue.append(i)
                visited[i]=1
                while queue:
                    u=queue.pop(0)
                    print(u,end=' ')
                    for v in self.graph[u]:
                        if visited[v]==0:
                            queue.append(v)
                            visited[v]=1
    # 2. BFS from a vertex
    # def BFS(self,vertex):
    #     visited = defaultdict(lambda:0)
    #     queue=[]
    #     queue.append(vertex)
    #     visited[vertex]=1
    #     while queue:
    #         u=queue.pop(0)
    #         print(u,end=' ')
    #         for v in self.graph[u]:
    #             if visited[v]==0:
    #                 queue.append(v)
    #                 visited[v]=1

t=int(input())
for _ in range(t):
    n=int(input())
    g=Graph()
    edges=[]
    ans={}
    for i in range(n-1):
        u,v=list(map(int,input().split()))
        edges.append((u,v))
        g.addEdge(u,v)
        g.addEdge(v,u)
    for i in range(1,n+1):
        if (len(g.graph[i]))>=3:
            print(-1)
            break
    else:
        g.DFS(1)
        dinhdau=g.path[-1]
        g.path=[]
        g.DFS(dinhdau)
        duongdi=g.path
        for j in range(n-1):
            dinh1,dinh2=duongdi[j],duongdi[j+1]
            if j%2==0:
                ans[(dinh1,dinh2)]=2
                ans[(dinh2,dinh1)]=2
            else:
                ans[(dinh1,dinh2)]=3
                ans[(dinh2,dinh1)]=3
                
        for e in edges:
            print(ans[e],end=" ")
        print()


                
                