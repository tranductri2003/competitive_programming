
# Each of the following n lines contains a string of n characters. 
# The j-th character of the i-th such line (1≤i,j≤n) is 0 if (i,j) is land or 1 if (i,j) is water.

#0 là đất, 1 là nước

# Let S be the set of cells accessible from (r1,c1).

# Similarly, let T be the set of cells accessible from (r2,c2).

# We can find S and T using a search algorithm such as a DFS or a BFS.

# If S=T, then a tunnel is not needed, so the answer is 0.

# Otherwise, we need to create a tunnel with an endpoint in A and the other in B. Now, we can simply iterate through all possible pairs of cells ((x1,y1),(x2,y2)) where (x1,y1)∈S and (x2,y2)∈T to find one that minimizes the cost (i.e., (x1−x2)2+(y1−y2)2).

# The time complexity is O(n4).


from collections import defaultdict
import math

 
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def BFS(self,vertex):
        visited = defaultdict(lambda:0)
        queue=[]
        queue.append(vertex)
        path=[]
        visited[vertex]=1
        while queue:
            u=queue.pop(0)
            path.append(u)
            for v in self.graph[u]:
                if visited[v]==0:
                    queue.append(v)
                    visited[v]=1
        return path
                  
    

    
    
def coordinateToNum(x,y,n):
    return (x-1)*n+y
def numTonCoordinate(num,n):
    y=math.ceil(num/n)
    x=num-n*(y-1)
    return x,y
    
 
g= Graph()
 
 
n=int(input())
matrix=[]
for i in range(n+2):
    matrix.append([])
    for j in range(n+2):
        matrix[i].append(1) #Ban đầu mặc định là nước
 
 
r1,c1=list(map(int,input().split()))
r2,c2=list(map(int,input().split()))
 
for i in range(1,n+1):
    s=input()
    for j in range(1,n+1):
        matrix[i][j]=int(s[j-1])
 
for i in range(1,n+1):
    for j in range(1,n+1):
        if matrix[i][j]==0 and matrix[i][j+1]==0:
            num1=coordinateToNum(i,j,n)
            num2=coordinateToNum(i,j+1,n)
            g.addEdge(num1,num2)
        if matrix[i][j]==0 and matrix[i+1][j]==0:
            num1=coordinateToNum(i,j,n)
            num2=coordinateToNum(i+1,j,n)
            g.addEdge(num1,num2)
 
 
 
start=coordinateToNum(r1,c1,n)
end=coordinateToNum(r2,c2,n)
 
S=g.BFS(start)     #Tập hợp những điểm có thể đến từ ô đầu
T=g.BFS(end)       #Tập hợp những điểm có thể đến từ đích 


if S==T:
    print(0)
else:
    res=10**9
    for num1 in S:
        for num2 in T:
            coor1x,coor1y=numTonCoordinate(num1,n)
            coor2x,coor2y=numTonCoordinate(num2,n)
            res=min(res,(coor1x-coor2x)**2+(coor1y-coor2y)**2)  
    print(res)
 
# for i in range(1,n+1)    :
#     for j in range(1,n+1) :
#         matrix[i][j]=coordinateToNum(i,j,n)
# for i in range(1,n+1) :
#     print(matrix[i][1:-1])