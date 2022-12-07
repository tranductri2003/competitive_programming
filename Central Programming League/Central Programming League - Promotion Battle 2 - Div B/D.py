from collections import defaultdict
from heapq import heappop, heappush

class Graph:
    #Minimum Spanning Trees: Kruskal's Algorithm
    def __init__(self, vertices):
        self.vertices=vertices
        self.graph=[]
    def addEdge(self,node1,node2,weight):
        self.graph.append([node1,node2,weight])


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
        
        for node in range(self.vertices+1):
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

    
class Graph2:
    INF=10**9

    # Algorithms for finding the shortest path: Floyd Warshall    
    def __init__(self,vertices):
        self.vertices=vertices
        self.distance=defaultdict(lambda:defaultdict(lambda:self.INF))
        self.edges=defaultdict(lambda:defaultdict(lambda:self.INF))
        for i in range(1,vertices+1):
            self.distance[i][i]=0
            self.edges[i][i]=0
    def addEdge(self,u,v,w):
        self.edges[u][v]=w
        self.edges[v][u]=w

    def FloydWarshall(self):
        for k in range(1,self.vertices+1):
            for i in range(1,self.vertices+1):
                for j in range(1,self.vertices+1):
                   self.distance[i][j]=min(self.distance[i][j],self.edges[i][k]+self.edges[k][j])
        return self.distance

class Graph3:
    INF=10**9

    # Algorithms for finding the shortest path: Floyd Warshall    
    def __init__(self,vertices):
        self.vertices=vertices
        self.distance=defaultdict(lambda:defaultdict(lambda:self.INF))
        self.edges=defaultdict(lambda:defaultdict(lambda:self.INF))
        for i in range(1,vertices+1):
            self.distance[i][i]=0
            self.edges[i][i]=0
    def addEdge(self,u,v,w):
        self.edges[u][v]=w
        self.edges[v][u]=w

    def FloydWarshall(self):
        for k in range(1,self.vertices+1):
            for i in range(1,self.vertices+1):
                for j in range(1,self.vertices+1):
                   self.distance[i][j]=min(self.distance[i][j],self.edges[i][k]+self.edges[k][j])
        return self.distance
# • Nếu giữa hai địa điểm bất kỳ trong dự án ban đầu có ít nhất một đường đi thì sự sửa đổi này
# không làm ảnh hưởng tới độ dài đường đi ngắn nhất giữa hai địa điểm đó.
# • Tổng độ dài những đường phố được giữ lại là ngắn tối tiểu


n,m=list(map(int,input().split()))
g=Graph(n)
g2=Graph2(n)
data=[]
for i in range(m):
    u,v,c=list(map(int,input().split()))
    g.addEdge(u,v,c)
    g2.addEdge(u,v,c)
    data.append((u,v,c))
    
    
res=g.Kruskal()

t=0
for num in res:
    t+=num[2]

chieudailucdau=g2.FloydWarshall()

g3=Graph3(n)
for num in res:
    u,v,c=num[0],num[1],num[2]
    g3.addEdge(u,v,c)
chieudailucsau=g3.FloydWarshall()

for i in range(1,n):
    for j in range(i+1,n+1):
        if chieudailucdau[i][j]!=chieudailucsau[i][j]:
            t+=g2.edges[i][j]
print(t)
        




