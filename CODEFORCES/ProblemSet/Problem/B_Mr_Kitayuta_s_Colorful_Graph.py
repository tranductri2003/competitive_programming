
#?		 /\_/\
#?		(= ._.)
#?		/ >WA \>AC
#//     WELCOME TO MY CODING SPACE
#!      Filename: B_Mr_Kitayuta_s_Colorful_Graph.py
#*      Folder: D:\Code\Python\Codeforces\ProblemSet
#?      Author: TranDucTri2003
#TODO   CreatedAt: 2022-05-04 15:42:00


from collections import defaultdict,Counter
from heapq import heappop, heappush

class Graph:
    INF=10**9
    #Searching Algorithms: DFS, BFS
    def __init__(self):
        self.graph = defaultdict(list)
        self.color=defaultdict(lambda:defaultdict(list))


        
    #DFS,BFS
    def addEdge(self,u,v,w):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.color[u][v].append(w)
        self.color[v][u].append(w)
 
    def DFS(self,vertex,destination):
        path=[]
        stack=[vertex]
        visited=defaultdict(lambda:0)
        while len(stack):
            u=stack.pop()
            if visited[u]==0:
                path.append(u)
                visited[u]=1
                for neighbour in self.graph[u]:
                    stack.append(neighbour)
        index=path.index(destination)
        return path[:index+1]
    def res(self,path):
        l=len(path)
        temp=[]
        for i in range(0,l-1):
            for num in self.color[path[i]][path[i+1]]:
                temp.append(num)
        z=Counter(temp)
        res=0
        for num in z.values():
            if num==l-1:
                res+=1
        return res

     
            
# Find the number of the colors that satisfy the following condition: the edges of
# that color connect vertex ui and vertex vi directly or indirectly.
g=Graph()
n,m=list(map(int,input().split()))
for i in range(m):
    a,b,c=list(map(int,input().split()))
    g.addEdge(a,b,c)
q=int(input())
for i in range(q):
    u,v=list(map(int,input().split()))
    a=g.DFS(u,v)
    print(g.res(a))
