
#?		 /\_/\
#?		(= ._.)
#?		/ >WA \>AC
#// WELCOME TO MY CODING SPACE
#!  Filename: nhap.py
#?  Author: TranDucTri2003
#*  CreatedAt: 2022-05-01 19:05:07


 
# from collections import defaultdict
# from heapq import heappop, heappush
# from queue import PriorityQueue
# class Graph:
#     INF=10**9
#     #Searching Algorithms: DFS, BFS
#     def __init__(self):
#         self.graph = defaultdict(list)
#     def addEdge(self,u,v):
#         self.graph[u].append(v)
#         self.graph[v].append(u)
    
#     #! Using Priority Queue slower
#     def DFS(self,vertex):
#         path=[]
#         stack=PriorityQueue()
#         stack.put((vertex,vertex))
#         visited=defaultdict(lambda:0)
#         while stack.qsize():
#             u=stack.get()
#             if visited[u[1]]==0:
#                 path.append(u[1])
#                 visited[u[1]]=1
#                 for neighbour in self.graph[u[1]]:
#                     stack.put((neighbour,neighbour))
#         return path

#     #!Using Heapq faster
#     # 2.DFS from a vertex 
#     # def DFS(self):
#     #     were = set()
#     #     ans = []
#     #     # heap=[1]
#     #     heap=[]
#     #     heappush(heap,1)
#     #     while heap:
#     #         vertex=heappop(heap)
#     #         if vertex not in were:
#     #             ans.append(vertex)
#     #             were.add(vertex)
#     #             for neighbour in self.graph[vertex]:
#     #                 heappush(heap,neighbour)
#     #     print(*ans)
                    
# g=Graph()
# n,m=list(map(int,input().split()))
# for i in range(m):
#     u,v=list(map(int,input().split()))
#     g.addEdge(u,v)
# a=g.DFS(1)
# print(*a)


#! ORIGINAL
from collections import defaultdict
from heapq import heappop, heappush

class Graph:
    INF=10**9
    #Searching Algorithms: DFS, BFS
    def __init__(self):
        self.graph = defaultdict(list)
        
    # Algorithms for finding the shortest path: Bellman Ford
    # def __init__(self, vertices):
    #     self.V = vertices # No. of vertices
    #     self.graph = []

    # Algorithms for finding the shortest path: Dijsktra
    # def __init__(self,vertices):
    #     self.distance=[self.INF]*vertices
    #     self.edges=defaultdict(dict)

    # Algorithms for finding the shortest path: Floyd Warshall    
    # def __init__(self,vertices):
    #     self.distance=defaultdict(lambda:defaultdict(lambda:self.INF))
    #     self.edges=defaultdict(lambda:defaultdict(lambda:self.INF))
    #     for i in range(1,vertices+1):
    #         self.distance[i][i]=0
    #         self.edges[i][i]=0
    
    #Minimum Spanning Trees: Kruskal's Algorithm
    # def __init__(self, vertices):
    #     self.vertices=vertices
    #     self.graph=[]
    

        
    #DFS,BFS
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    #Bellman Ford
    # def addEdge(self, u, v, w):
    #     self.graph.append([u, v, w])
    
    #Dijsktra
    # def addEdge(self,u,v,w):
    #     self.edges[u][v]=w
        
    #Floyd Warshall
    # def addEdge(self,u,v,w):
    #     self.edges[u][v]=w
    
    #:Kruskal's Algorithm finding MST
    # def addEdge(self,node1,node2,weight):
    #     self.graph.append([node1,node2,weight])
    
    #Finds the root of a subtree containing node 'i'
    def findSubtree(self,parent,i):
        if parent[i]==i:
            return i
        else:
            return self.findSubtree(parent,parent[i])
    #Connects subtrees containing node 'x' and 'y'
    def connectSubtree(self,parent,subtreeSize,x,y):
        xroot=self.findSubtree(parent,x)
        yroot=self.findSubtree(parent,y)
        if subtreeSize[xroot]<subtreeSize[yroot]:
            parent[xroot]=yroot
        elif subtreeSize[xroot]>subtreeSize[yroot]:
            parent[yroot]=xroot
        else:
            parent[yroot]=xroot
            subtreeSize[xroot]+=1

        

        
    def DFSUtil(self, vertex,visited,path):
        stack=[vertex]
        while len(stack):
            u=stack.pop()
            if visited[u]==0:
                path.append(u)
                visited[u]=1
            for neighbour in self.graph[u]:
                if visited[neighbour]==0:
                    stack.append(neighbour)
                
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
        stack=[vertex]
        visited=defaultdict(lambda:0)
        while len(stack):
            u=heappop(stack)
            if visited[u]==0:
                path.append(u)
                visited[u]=1
                for neighbour in self.graph[u]:
                    heappush(stack,neighbour)
        return path
                

                
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
    #     path=[]
    #     while queue:
    #         u=queue.pop(0)
    #         path.append(u)
    #         for v in self.graph[u]:
    #             if visited[v]==0:
    #                 queue.append(v)
    #                 visited[v]=1
    #     return path
                  
    
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
    
    def BellmanFord(self, S):
        d=defaultdict(lambda:self.INF)
        trace=defaultdict(lambda:-1)
        d[S]=0
 
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if d[u]!=self.INF and d[v]>d[u]+w:
                    d[v]=d[u]+w
                    trace[v]=u

        #Trả về đường đi từ đỉnh S đến u nào đó
        #return trace
        # if u!=S and trace[u]==-1:
        #     return -1 #Không có đường đi
        # else:
        #     path=[]
        #     while u!=-1:
        #         path.append(u)
        #         u=trace[u]
        #     path.reverse()
        #     return path

        #Nhận biết đường đi âm vô cực trong trường hợp có chu trình âm:
        
        # Chạy thuật toán Bellman-Ford thêm một lần nữa với N vòng lặp, những đỉnh nào vẫn còn tối ưu được ở lần chạy thứ hai
        # sẽ tối ưu được mãi mãi, và đó là các đỉnh không tồn tại đường đi ngắn nhất.
        
        for _ in range(self.V):
            for u, v, w in self.graph:
                if d[u]!=self.INF and d[v]>d[u]+w:
                    d[v]=-self.INF  # vẫn còn tối ưu được --> âm vô cực
                    trace[v]=u
        return d
    
    def Dijsktra(self,S):
        self.distance[S]=0
        queue=[(0,S)]
        trace=defaultdict(lambda:-1)
        while queue:
            cost,vertex=heappop(queue)
            for neighbour, weight in self.edges[vertex].items():
                if cost+weight<self.distance[neighbour]:
                    self.distance[neighbour]=cost+weight
                    heappush(queue, (cost + weight, neighbour))
                    trace[neighbour]=vertex
        #Trả về đường đi từ đỉnh S đến u nào đó
        #return trace
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
    
    def FloydWarshall(self,vertices):
        for k in range(1,vertices+1):
            for i in range(1,vertices+1):
                for j in range(1,vertices+1):
                   self.distance[i][j]=min(self.distance[i][j],self.edges[i][k]+self.edges[k][j])
        return self.distance
    
    def Kruskal(self):
        #Resulting tree
        res=[]
        
        #Iterator
        i=0
        #Number of edges in MST
        e=0

        #Sort edges by their weight
        self.graph=sorted(self.graph,key=lambda item: item[2])

        #Auxiliary arrays
        parent=[]
        subtreeSize=[]
        
        #initialize parent and subtreeSize arrays
        
        for node in range(self.vertices):
            parent.append(node)
            subtreeSize.append(0)
        
        #Number of edges in a MST is (node-1)
        
        while e<self.vertices-1:
            node1,node2,weight=self.graph[i]
            i+=1

            x=self.findSubtree(parent,node1)
            y=self.findSubtree(parent,node2)
            
            if x!=y:
                e+=1
                res.append([node1,node2,weight])
                self.connectSubtree(parent,subtreeSize,node1,node2)
        return res

    def isEulerian(self):
        path=self.connectedComponentsBFS(self.v)
        for compo in path:
            odd=0
            for vertex in compo:
                if self.degree[vertex]%2==1:
                    odd+=1

        if odd == 0:
            return 2
        elif odd == 2:
            return 1
        elif odd > 2:
            return 0
            # '''If odd count is 2, then semi-eulerian.
            # If odd count is 0, then eulerian
            # If count is more than 2, then graph is not Eulerian
            # Note that odd count can never be 1 for undirected graph'''
    def test(self):
        res = self.isEulerian()
        if res == 0:
            print("graph is not Eulerian")
        elif res == 1:
            print("graph has a Euler path")
        else:
            print("graph has a Euler cycle")
            
g=Graph()
n,m=list(map(int,input().split()))
for i in range(m):
    u,v=list(map(int,input().split()))
    g.addEdge(u,v)
a=g.DFS(1)
print(*a)



