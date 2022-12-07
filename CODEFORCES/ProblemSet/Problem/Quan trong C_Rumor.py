
from collections import defaultdict
 
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def DFSUtil(self, v,visited):
        visited[v]=1
        print(v,end=" ")
        for neighbour in self.graph[v]:
            if visited[neighbour]==0:
                self.DFSUtil(neighbour,visited)
                
    #DFSUtil in case finding Connected components
    def DFSUtilConnect(self, currentCost, v, visited):
        visited[v] = 1
        currentCost = min(currentCost,a[v-1])
        for neighbour in self.graph[v]:
            if visited[neighbour]==0:
                self.DFSUtilConnect(currentCost,neighbour,visited)
        return currentCost
                
    # 1.Handling A Disconnected Graph: 
    def DFS(self,numVertex):
        visited=defaultdict(lambda:0)
        for vertex in range(1,numVertex+1):
            if visited[vertex]==0:
                self.DFSUtil(vertex,visited)        
    # 2.DFS from a vertex 
    # def DFS(self,vertex):
    #     visited=defaultdict(lambda:0)
    #     self.DFSUtil(vertex,visited)
                
    # 1. Handling A Disconnected Graph:
    def BFS(self,numVertex):
        res=0
        visited=defaultdict(lambda:0)
        queue=[]
        for i in range(1,numVertex+1):
            if visited[i]==0:
                temp=10**18
                queue.append(i)
                visited[i]=1
                while queue:
                    u=queue.pop()
                    temp=min(temp,a[u-1])
                    for v in self.graph[u]:
                        if visited[v]==0:
                            queue.append(v)
                            visited[v]=1
                res+=temp
                print()
        return res
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
    
    def connectedComponents(self,numVertex):
        cost=0
        visited=defaultdict(lambda:0)
        for vertex in range(1,numVertex+1):
            if visited[vertex] == 0:
                currentCost=10**14
                cost+=self.DFSUtilConnect(currentCost,vertex,visited)
        return cost
import sys
# sys.stdin=open('so0.txt','r')
n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
g=Graph()
for i in range(m):
    u,v=list(map(int,input().split()))
    g.addEdge(u,v)
    g.addEdge(v,u)
# res=0
# res+=g.connectedComponents(n)
# print(res)
res=g.BFS(n)
print(res)

"""
!
from collections import defaultdict
 
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def DFSUtil(self, v,visited):
        visited[v]=1
        print(v,end=" ")
        for neighbour in self.graph[v]:
            if visited[neighbour]==0:
                self.DFSUtil(neighbour,visited)
                
    #DFSUtil in case finding Connected components
    def DFSUtilConnect(self, temp, v, visited):
        visited[v] = 1
        # Store the vertex to list
        temp.append(v)
        for neighbour in self.graph[v]:
            if visited[neighbour]==0:
                # Update the list
                temp = self.DFSUtilConnect(temp, neighbour, visited)
        return temp
    
    
    # 1.Handling A Disconnected Graph: 
    def DFS(self,numVertex):
        visited=defaultdict(lambda:0)
        for vertex in range(1,numVertex+1):
            if visited[vertex]==0:
                self.DFSUtil(vertex,visited)        
    # 2.DFS from a vertex 
    # def DFS(self,vertex):
    #     visited=defaultdict(lambda:0)
    #     self.DFSUtil(vertex,visited)
                
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
    def connectedComponentsBFS(self,numVertex):
        visited=defaultdict(lambda:0)
        stack=[]
        connectedComponents=defaultdict(list)
        for i in range(1,numVertex+1):
            if visited[i]==0:
                stack.append(i)
                visited[i]=1
                while stack:
                    u=stack.pop()
                    connectedComponents[i].append(a[u-1])
                    for v in self.graph[u]:
                        if visited[v]==0:
                            stack.append(v)
                            visited[v]=1
        return connectedComponents
                
    
    def connectedComponentsDFS(self,numVertex):
        path=[]
        visited=defaultdict(lambda:0)
        for vertex in range(1,numVertex+1):
            if visited[vertex] == 0:
                temp = []
                path.append(self.DFSUtilConnect(temp, vertex, visited))
        return path
    
    

n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
g=Graph()
for i in range(m):
    u,v=list(map(int,input().split()))
    g.addEdge(u,v)
    g.addEdge(v,u)
res=0
path=g.connectedComponentsBFS(n)
for num in path:
    res+=min(path[num])
print(res)
"""