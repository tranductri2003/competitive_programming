from collections import defaultdict
from heapq import heappop, heappush
from collections import deque

class Graph:
    INF=10**9
    def __init__(self):
        self.graph = defaultdict(list)
        self.count=defaultdict(lambda:0)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)  
        

    def BFS(self, numVertex):
        visited = defaultdict(lambda: 0)
        queue = deque()  # Sử dụng deque thay cho danh sách
        for i in range(1, numVertex + 1):
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                while queue:
                    u = queue.popleft()  # Sử dụng popleft() thay cho pop(0)
                    for v in self.graph[u]:
                        if visited[v] == 0:
                            queue.append(v)
                            visited[v] = 1

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
        return self.distance
    
    def FloydWarshall(self,vertices):
        for k in range(1,vertices+1):
            for i in range(1,vertices+1):
                for j in range(1,vertices+1):
                   self.distance[i][j]=min(self.distance[i][j],self.edges[i][k]+self.edges[k][j])
        return self.distance


    def findSubtree(self,parent,i):
        if parent[i]==i:
            return i
        else:
            return self.findSubtree(parent,parent[i])
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
        
    def Kruskal(self):
        res=[]
        
        i=0
        e=0

        self.graph=sorted(self.graph,key=lambda item: item[2])

        parent=[]
        subtreeSize=[]
        
        
        for node in range(self.vertices):
            parent.append(node)
            subtreeSize.append(0)
        
        
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




        
    """
    Return true if there is a path from source 's' to
    residual graph. Also fills parent[] to store the path"""

    def BFS(self,s,t,parent):
        visited=defaultdict(lambda:False)
        queue=[]
        
        queue.append(s)
        visited[s]=True

        while queue:
            u=queue.pop(0)
            for v in list(self.edges[u]):
                if visited[v]==False and self.edges[u][v]>0:
                    queue.append(v)
                    visited[v]=True
                    parent[v]=u
                    if v==t:
                        return True
        return False

    def FordFulkerson(self,source, sink):
        parent=defaultdict(lambda:-1)
        maxFlow=0

        while self.BFS(source, sink,parent):
            pathFlow=self.INF
            s=sink
            while (s!=source):
                pathFlow=min(pathFlow,self.edges[parent[s]][s])
                s=parent[s]
            
            maxFlow+=pathFlow

            v=sink
            while (v!=source):
                u=parent[v]
                self.edges[u][v]-=pathFlow
                self.edges[v][u]+=pathFlow
                v=parent[v]
        return maxFlow
    
    
    
    
    def isEulerian(self):
        path=self.connectedComponentsBFS(self.v)
        for compo in path:
            odd=0
            for vertex in compo:
                if self.degree[vertex]%2==1:
                    odd+=1

        if odd == 0:
        elif odd == 2:
        elif odd > 2:

    def numCycle(self,vertex):
        path=[]
        stack=[vertex]
        visited=defaultdict(lambda:0)
        ancestor=defaultdict(lambda:0)
        num=0
        while len(stack):
            u=stack.pop()
            if visited[u]==0:
                path.append(u)
                visited[u]=1
                for neighbour in self.graph[u]:
                    ancestor[neighbour]=u
                        num+=1
                        stack.append(neighbour)
        return num

    def isBipartite(self,src):
        colorArr=defaultdict(lambda:-1)
        colorArr[src]=1
        queue=[]
        queue.append(src)
        while queue:
            u=queue.pop(0)
            if u in self.graph[u]:
                return False
            for v in self.graph[u]:
                if colorArr[v]==-1:
                    colorArr[v]=1-colorArr[u]
                    queue.append(v)
                elif colorArr[v]==colorArr[u]:
                    return False
        return True
    
    def MaximumBipartiteMatching(self,x,y):
        for i in range(x):
            self.addEdge(0,i+1,1)
        for i in range(y):
            self.addEdge(x+i+1,x+y+1,1)
        return self.FordFulkerson(0,x+y+1)
    def sizeOfsubTree(self,s,e):
        self.count[s]=1
        for u in self.graph[s]:
            if u!=e:
                self.sizeOfsubTree(u,s)
                self.count[s]+=self.count[u]      

