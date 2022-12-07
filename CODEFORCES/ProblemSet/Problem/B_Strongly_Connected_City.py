from collections import defaultdict
 
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def DFSUtil(self, v,visited,path):
        visited[v]=1
        path.append(v)
        for neighbour in self.graph[v]:
            if visited[neighbour]==0:
                self.DFSUtil(neighbour,visited,path)
                
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
    # def DFS(self,numVertex):
    #     visited=defaultdict(lambda:0)
    #     path=[]
    #     for vertex in range(1,numVertex+1):
    #         if visited[vertex]==0:
    #             self.DFSUtil(vertex,visited,path)        
    #     return path
                
    # 2.DFS from a vertex 
    def DFS(self,vertex):
        path=[]
        visited=defaultdict(lambda:0)
        self.DFSUtil(vertex,visited,path)
        return path
                
    # 1. Handling A Disconnected Graph:
    # def BFS(self,numVertex):
    #     visited=defaultdict(lambda:0)
    #     queue=[]
    #     for i in range(1,numVertex+1):
    #         if visited[i]==0:
    #             queue.append(i)
    #             visited[i]=1
    #             while queue:
    #                 u=queue.pop(0)
    #                 print(u,end=' ')
    #                 for v in self.graph[u]:
    #                     if visited[v]==0:
    #                         queue.append(v)
    #                         visited[v]=1
    # 2. BFS from a vertex
    def BFS(self,vertex):
        visited = defaultdict(lambda:0)
        queue=[]
        queue.append(vertex)
        visited[vertex]=1
        path=[]
        while queue:
            u=queue.pop(0)
            path.append(u)
            for v in self.graph[u]:
                if visited[v]==0:
                    queue.append(v)
                    visited[v]=1
        return path
                  
    
    def connectedComponentsBFS(self,numVertex):
        visited=defaultdict(lambda:0)
        stack=[]
        path=[]
        for i in range(1,numVertex+1):
            if visited[i]==0:
                stack.append(i)
                visited[i]=1
                temp=[]
                while stack:
                    u=stack.pop()
                    temp.append(u)
                    for v in self.graph[u]:
                        if visited[v]==0:
                            stack.append(v)
                            visited[v]=1
                path.append(temp)
        return path
                  
    
    def connectedComponentsDFS(self,numVertex):
        path=[]
        visited=defaultdict(lambda:0)
        for vertex in range(1,numVertex+1):
            if visited[vertex] == 0:
                temp = []
                path.append(self.DFSUtilConnect(temp, vertex, visited))
        return path

g=Graph()

n,m=list(map(int,input().split()))

s1=input()
for i in range(n):
    if s1[i]=="<":
        for j in range(m*(i+1),m*i+1,-1):
            g.addEdge(j,j-1)
    else:
        for j in range(i*m+1,(i+1)*m):
            g.addEdge(j,j+1)
            
s2=input()
for i in range(m):
    if s2[i]=="v":
        for j in range(i+1,i+1+(n-2)*m+1,m):
            g.addEdge(j,j+m)
    else:
        for j in range(i+1+(n-1)*m,i+1,-m):
            g.addEdge(j,j-m)

for i in range(1,n*m+1):
    path=g.BFS(i)
    if len(path)<n*m:
        print("NO")
        break
else:
    print("YES")
        

