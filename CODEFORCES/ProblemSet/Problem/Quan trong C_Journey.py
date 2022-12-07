from collections import defaultdict
from operator import ne
 
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
             
    # 2.DFS from a vertex 
    def DFS(self,vertex):
        res=0
        depth=defaultdict(lambda:0)
        ancestor=defaultdict(lambda:0)
        stack=[vertex]
        visited=defaultdict(lambda:0)
        probability=defaultdict(lambda:0)
        probability[1]=1
        while len(stack):
            u=stack.pop(-1)
            if visited[u]==0:
                visited[u]=1
            if len(self.graph[u])==1 and visited[self.graph[u][0]]==1:
                res+=probability[u]*depth[u]
            else:
                for neighbour in self.graph[u]:
                    if visited[neighbour]==0:
                        stack.append(neighbour)
                        ancestor[neighbour]=u
                        depth[neighbour]=depth[u]+1
                        if u==1:
                            probability[neighbour]=probability[u]/len(self.graph[u])
                        else:
                            probability[neighbour]=probability[u]/(len(self.graph[u])-1)
    
        return res
                

 
n=int(input())
g=Graph()
for i in range(n-1):
    u,v=list(map(int,input().split()))
    g.addEdge(u,v)
leaf=g.DFS(1)

print(leaf)


