from collections import defaultdict
 
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        

    # 2.DFS from a vertex 
    def DFS(self,vertex):
        path=[]
        stack=[vertex]
        visited=defaultdict(lambda:0)
        while len(stack):
            u=stack.pop(-1)
            if visited[u]==0:
                path.append(u)
                visited[u]=1
            for neighbour in self.graph[u]:
                if visited[neighbour]==0:
                    stack.append(neighbour)
        return path
                


    
t=int(input())
for _ in range(t):
    n=int(input())
    g=Graph()
    
    edges=[]
    for i in range(n-1):
        u,v=list(map(int,input().split()))
        g.addEdge(u,v)
        if u>v:
            edges.append((v,u))
        else:
            edges.append((u,v))
    data=g.graph
    for vertex in data:
        if len(data[vertex])>=3:
            print(-1)
            break
    else:
        path=g.DFS(1)
        path=g.DFS(path[-1])

        res=defaultdict(lambda:0)
        for i in range(n-1):
            if i%2==0:
                if path[i]<path[i+1]:
                    res[(path[i],path[i+1])]=2
                else:
                    res[(path[i+1],path[i])]=2
            else:
                if path[i]<path[i+1]:
                    res[(path[i],path[i+1])]=3
                else:
                    res[(path[i+1],path[i])]=3
        for num in edges:
            print(res[num],end=" ")
        print()
                
        