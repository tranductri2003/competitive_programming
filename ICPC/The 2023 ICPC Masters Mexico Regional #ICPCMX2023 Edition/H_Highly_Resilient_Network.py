# Python3 program for above approach

# Graph class represents an undirected graph
# using adjacency list representation
class Graph:
    def __init__(self, V):
        # No. of vertices
        self.V = V
        # Pointer to an array containing
        # adjacency lists
        self.adj = [[] for i in range(self.V)]

    # Function to return a list of connected components
    def connectedComponents(self):
        # Mark all the vertices as not visited
        visited = [False for i in range(self.V)]
        # List to store connected components
        components = []

        for v in range(self.V):
            if not visited[v]:
                component = []
                self.DFSUtil(v, visited, component)
                components.append(component)

        return components

    def DFSUtil(self, v, visited, component):
        # Mark the current node as visited
        visited[v] = True
        component.append(v)

        # Recur for all the vertices
        # adjacent to this vertex
        for i in self.adj[v]:
            if not visited[i]:
                self.DFSUtil(i, visited, component)

    def isBridge(self, u, v):
        # Remove edge (u, v) from the graph
        self.adj[u].remove(v)
        self.adj[v].remove(u)

        # Check if the graph is still connected
        visited = [False for i in range(self.V)]
        component = []
        self.DFSUtil(u, visited, component)

        # Add the edge back to the graph
        self.adj[u].append(v)
        self.adj[v].append(u)

        # If the graph is not connected, then (u, v) is a bridge
        return len(component) != self.V

    # Add an undirected edge
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)


# Input the number of vertices (N) and edges (M)
N, M = list(map(int, input().split()))

# Create a graph
g = Graph(N)

# Add edges to the graph
for _ in range(M):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    g.addEdge(u, v)

# Get the connected components
components = g.connectedComponents()

# Print the connected components and check for bridges
for component in components:
    temp = 0
    if len(component) > 1:
        for u in component:
            for v in g.adj[u]:
                if u < v and g.isBridge(u, v):
                    temp += 1
                    print(f"Edge ({u + 1}, {v + 1}) is a bridge in component {component}")

# Nếu bạn muốn in ra số lượng cầu trong mỗi thành phần liên thông, bạn có thể thêm dòng sau vào cuối vòng lặp:
# print(f"Number of bridges in component {component}: {temp}")
