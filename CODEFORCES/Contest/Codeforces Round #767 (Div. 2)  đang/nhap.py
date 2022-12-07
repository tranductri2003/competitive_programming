'''Python program to print DFS traversal for complete graph'''
from collections import defaultdict

# this class represents a directed graph using adjacency list representation


class Graph:
	# Constructor
	def __init__(self):
		# default dictionary to store graph
		self.graph = defaultdict(list)

	# Function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)
	# A function used by DFS

	def DFSUtil(self, v, visited):
		# Mark the current node as visited and print it
		visited[v]=1
		print(v)

		# recur for all the vertices adjacent to this vertex
		for neighbour in self.graph[v]:
			if visited[neighbour]==0:
				self.DFSUtil(neighbour, visited)
		# The function to do DFS traversal. It uses recursive DFSUtil

	def DFS(self):
		# create a set to store all visited vertices
		visited=defaultdict(lambda:0)
        
  
		# call the recursive helper function to print DFS traversal starting from all
		# vertices one by one
		for vertex in self.graph:
			if visited[vertex]==0:
				self.DFSUtil(vertex, visited)
# Driver code
# create a graph given in the above diagram


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.DFS()

# Improved by Dheeraj Kumar
