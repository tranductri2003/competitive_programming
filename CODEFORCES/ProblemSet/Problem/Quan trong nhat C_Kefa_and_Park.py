from collections import defaultdict
 
class Graph:
    def __init__(self,cat,m):
        self.graph = defaultdict(list)
        self.cat=cat
        self.m=m    
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def DFS(self,vertex):
        stack=[vertex]
        visited=defaultdict(lambda:0)
        ancestor=defaultdict(lambda:0)
        ancestor[1]=1
        leaf=[]
        count=defaultdict(lambda:0)
        while len(stack):
            u=stack.pop(-1)
            visited[u]=1
            if self.cat[u]==1:
                count[u]=count[ancestor[u]]+1
            else:
                count[u]=0
            if count[u]<=self.m:
                if len(self.graph[u])==1 and visited[self.graph[u][0]]==1:
                    leaf.append(u)
                else:
                    for neighbour in self.graph[u]:
                        if visited[neighbour]==0:
                            stack.append(neighbour)
                            ancestor[neighbour] =u
        return leaf
                


#Nếu có quá m con mèo liên tiếp thì đường đi đó sẽ bị hủy bỏ
#In ra số lá mà mình có thể đến được
n,m=list(map(int,input().split()))

a=list(map(int,input().split()))
cat=defaultdict(lambda:False)

for i in range(n):
    if a[i]==1:
        cat[i+1]=1
g=Graph(cat,m)
for i in range(n-1):
    u,v=list(map(int,input().split()))
    g.addEdge(u,v)

leaf=g.DFS(1)

print(len(leaf))

