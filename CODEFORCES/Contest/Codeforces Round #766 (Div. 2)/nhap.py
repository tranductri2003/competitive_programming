# Using a Python dictionary to act as an adjacency list

from collections import defaultdict

visited={}
visited=defaultdict(lambda:0,visited)

graph={}
graph=defaultdict(lambda:[],graph)

for i in range(6):
      x,y=list(map(int,input().split()))
      if graph[str(x)]==0:
            graph[str(x)]=[str(y)]
      else:
            graph[str(x)].append(str(y))
 
      
print(graph)
def dfs(visited, graph, node):  #function for dfs 
    if visited[node]==0:  
        print (node)
        visited[node]=1
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')