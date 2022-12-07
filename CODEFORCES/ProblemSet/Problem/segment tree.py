
#Segment tree node
class Node:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.total = 0
        self.max = 0
        self.min = 0
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self,mang,n):
        self.a=mang
        self.N=n
        self.INF_MIN=-10**9
        self.INF_MAX=10**9
        def buildTree(mang,l,r):
            
            #base case
            if l>r:
                return None
            
            #leaf node
            if l==r:
                n=Node(l,r)
                n.total=mang[l]
                n.max=mang[l]
                n.min=mang[l]
                return n
            
            mid = (l+r)//2

            root=Node(l,r)
            
            #Recursively build the SegmentTree
            root.left=buildTree(mang,l,mid)
            root.right=buildTree(mang,mid+1,r)
            
            #Total stores the sum of all the leaves under root
            #i.e. those elements lying between (start,end)
            root.total=root.left.total+root.right.total
            root.max=max(root.left.max,root.right.max)
            root.min=min(root.left.min,root.right.min)
            
            return root
        self.root=buildTree(mang,0,n-1)
    
    def updateNode(self,i,val):
        def updateVal(root,i,val):
            
            #Base case. The actual value will be updated in a leaf.
            #The total is them propogated upwards
            if root.start==root.end:
                root.total=val
                root.max=val
                root.min=val
                return root
            
            mid = (root.start+root.end)//2
            
            #If the index is less than the mid, that leaf must be in the left subtree
            if i<=mid:
                updateVal(root.left,i,val)
            #Otherwise, the right subtree
            else:
                updateVal(root.right,i,val)
            
            #Propogate the changes after recursive call returns
            root.total=root.left.total+root.right.total
            root.max=max(root.left.max,root.right.max)
            root.min=min(root.left.min,root.right.min)
            
            return root
        return updateVal(self.root,i,val)
    
    def updateRange(self,u,v,val):  #u,v là đoạn cần update; l,r là biến tạm
        #l=root.start
        #r=root.end
        def updateVal(root,u,v,val):
            if u>root.end or v<root.start:
                return
            
            #Base case. The actual value will be updated in a leaf.
            #The total is them propogated upwards
            if root.start==root.end:
                root.total+=val
                root.max+=val
                root.min+=val
                return root
            
            mid = (root.start+root.end)//2
            updateVal(root.left,u,mid,val)
            updateVal(root.right,mid+1,v,val)          
            
            #Propogate the changes after recursive call returns
            root.total=root.left.total+root.right.total
            root.max=max(root.left.max,root.right.max)
            root.min=min(root.left.min,root.right.min)
            
            return root
        return updateVal(self.root,u,v,val)
    
    def sumRange(self,i,j):
        def rangeSum(root,i,j):
            
            #If the range exactly matches the root, we already have the sum
            if root.start ==i and root.end==j:
                return root.total
            
            mid = (root.start+root.end)//2
            
            #If end of the range is less than the mid, the entire interval lies
            #in the left subtree
            if j<=mid:
                return rangeSum(root.left,i,j)
            
            #If start of the interval is greater than the mid, the entire interval lies
            #in the right subtree
            elif i>=mid+1:
                return rangeSum(root.right,i,j)
            
            #Otherwise, the interval is split. So we calculate the sum recursively,
            #by splitting the interval
            else:
                return rangeSum(root.left,i,mid)+rangeSum(root.right,mid+1,j)
            
        return rangeSum(self.root,i,j)
    
    def getMax(self,l,r):   #l,r là đoạn lấy giá trị lớn nhất
        def getValue(root,l,r):
            if l>root.end or r<root.start:
                #Đoạn cần cập nhật nằm ngoài khoảng phạm vi của NODE thì ta bỏ qua
                return self.INF_MIN
            if root.start==l and root.end==r:
                return root.max
            
            mid=(root.start+root.end)//2
            # if r<=mid:
            #     return getValue(root.left,l,r)
            # elif l>mid+1:
            #     return getValue(root.right,l,r)
            # else:
            return max(getValue(root.left,l,mid),getValue(root.right,mid+1,r))
        return getValue(self.root,l,r)
           
    def getMin(self,l,r):   
        def getValue(root,l,r):
            if l>root.end or r<root.start:
                return self.INF_MAX
            if root.start==l and root.end==r:
                return root.min
            
            mid=(root.start+root.end)//2
            # if r<=mid:
            #     return getValue(root.left,l,r)
            # elif l>mid+1:
            #     return getValue(root.right,l,r)
            # else:
            return min(getValue(root.left,l,mid),getValue(root.right,mid+1,r))
        return getValue(self.root,l,r)
    

# n=int(input())
# a=list(map(int,input().split()))

# ST=SegmentTree(a,n)

# Loại 1 có dạng   : Nấu gói mì ở vị trí thứ  và mua gói mì có độ ngon  thay vào đó. ()
# Loại 2 có dạng   : In ra độ ngon lớn nhất của các gói mì từ vị trí  đến  ()

# for _ in range(int(input())):
#     t,l,r=list(map(int,input().split()))
#     if t==1:
#         ST.updateNode(l-1,r)
#     else:
#         print(ST.getMax(l-1,r-1))

from collections import defaultdict
from heapq import heappop, heappush

class Graph:
    INF=10**9
    #Searching Algorithms: DFS, BFS
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
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
    
    
    #Minimum Spanning Trees: Kruskal's Algorithm
    # def __init__(self, vertices):
    #     self.vertices=vertices
    #     self.graph=[]
    # def addEdge(self,node1,node2,weight):
    #     self.graph.append([node1,node2,weight])


    # Ford-Fulkerson Algorithm for Maximum Flow Problem
    def __init__(self):
        self.edges=defaultdict(lambda:defaultdict(lambda:0))
    def addEdge(self,u,v,w):
        self.edges[u][v]=w            
    
    #Bipatite graph
    # def __init__(self):
    #     self.graph=defaultdict(list)  
    # def addEdge(self,u,v):
    #     self.graph[u].append(v)
    #     self.graph[v].append(u)
    
        
    def DFSUtil(self, vertex,visited,path):
        stack=[vertex]
        while len(stack):
            u=stack.pop()
            if visited[u]==0:
                path.append(u)
                visited[u]=1
                for neighbour in self.graph[u]:
                    stack.append(neighbour)
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
    #         u=stack.pop()
    #         if visited[u]==0:
    #             path.append(u)
    #             visited[u]=1
    #             for neighbour in self.graph[u]:
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
    #     queue=[vertex]
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
    
          
    def connectedComponentsDFS(self,numVertex):
        path=[]
        visited=defaultdict(lambda:0)
        for vertex in range(1,numVertex+1):
            if visited[vertex] == 0:
                temp = []
                path.append(self.DFSUtilConnect(temp, vertex, visited))
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




    #Ford-Fulkerson Algorithm for Maximum Flow Problem
        
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

    #Returns the maximum flow from s to t in the given graph
    def FordFulkerson(self,source, sink):
        parent=defaultdict(lambda:-1)
        maxFlow=0

        #Augment the flow while there is path from source to sink
        while self.BFS(source, sink,parent):
            # Find the minimum residual capacity of the edges along 
            #the path filled by BFS. Or we can say find the maximum flow
            #through the path found.
            pathFlow=self.INF
            s=sink
            while (s!=source):
                pathFlow=min(pathFlow,self.edges[parent[s]][s])
                s=parent[s]
            
            #Add path flow to overall flow
            maxFlow+=pathFlow

            #Update residual capatities of the edges and
            #reversed edges along the path
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
            return 2   # graph has a Euler cycle
        elif odd == 2:
            return 1  # graph has a Euler path
        elif odd > 2:
            return 0   # graph is not Euleria
            # '''If odd count is 2, then semi-eulerian.
            # If odd count is 0, then eulerian
            # If count is more than 2, then graph is not Eulerian
            # Note that odd count can never be 1 for undirected graph'''

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
                    if visited[neighbour]==1 and ancestor[u]!=neighbour:  #Nếu đỉnh hàng xóm đã được thăm và tổ tiên của u không phải là đỉnh hàng xóm chứng tỏ có thêm 1 cycle
                        num+=1
                    else:  #Nếu đỉnh đó chưa được thăm thì DFS như bình thường
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
        # Use init and addEdge FordFulkerson
        for i in range(x):
            self.addEdge(0,i+1,1)
        for i in range(y):
            self.addEdge(x+i+1,x+y+1,1)
        return self.FordFulkerson(0,x+y+1)







    
g=Graph()
for i in range(8):
    u,v,w=list(map(int,input().split()))
    g.addEdge(u,v,w)
print(g.FordFulkerson(1,6))