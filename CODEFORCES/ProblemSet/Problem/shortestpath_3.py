from collections import defaultdict

 
class Graph:
    # def __init__(self):
    #     self.graph = defaultdict(list)
        
    # Algorithms for finding the shortest path
    
    def __init__(self, vertices):
        self.V = vertices # No. of vertices
        self.graph = []
 
    # def addEdge(self,u,v):
    #     self.graph[u].append(v)
    #     self.graph[v].append(u)
        
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
        
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
    def DFS(self,numVertex):
        visited=defaultdict(lambda:0)
        path=[]
        for vertex in range(1,numVertex+1):
            if visited[vertex]==0:
                self.DFSUtil(vertex,visited,path)        
        return path
                
    # 2.DFS from a vertex 
    # def DFS(self,vertex):
    #     path=[]
    #     stack=[vertex]
    #     visited=defaultdict(lambda:0)
    #     while len(stack):
    #         u=stack.pop(-1)
    #         if visited[u]==0:
    #             path.append(u)
    #             visited[u]=1
    #         for neighbour in self.graph[u]:
    #             if visited[neighbour]==0:
    #                 stack.append(neighbour)
    #     return path
                

                
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
        INF=10**9
        d=defaultdict(lambda:INF)
        trace=defaultdict(lambda:-1)
        d[S]=0
 
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if d[u]!=INF and d[v]>d[u]+w:
                    d[v]=d[u]+w
                    trace[v]=u

        #Trả về đường đi từ đỉnh S đến u nào đó
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
                if d[u]!=INF and d[v]>d[u]+w:
                    d[v]=-INF  # vẫn còn tối ưu được --> âm vô cực
                    trace[v]=u
        return d

stop=False
while stop==False:
    n,m,q,s=list(map(int,input().split()))
    if n==0 and m==0 and q==0 and s==0:
        stop=True
        quit()
    # n  is the numbers of nodes in the graph, m the number of edges, q the number of queries and s the index of the starting node
    g=Graph(n)
    for i in range(m):
        u,v,w=list(map(int,input().split()))
        g.addEdge(u,v,w)
    path=g.BellmanFord(s)    
    for i in range(q):
        n=int(input())
        if path[n]==10**9:
            print("Impossible")
        elif path[n]==-10**9:
            print("-Infinity")
        else:
            print(path[n])
    print()


