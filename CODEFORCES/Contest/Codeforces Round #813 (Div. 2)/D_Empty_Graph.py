import networkx as nx
import random

# Create graph
G = nx.fast_gnp_random_graph(10, 0.3)

# Pick a random node
source = random.choice(list(G.nodes))

# Find the longest shortest path from the node
shortest_paths = nx.shortest_path(G, source=source)
target = max(shortest_paths, key=lambda i: len(shortest_paths[i]))
l_s_path = shortest_paths[target]
l_s_path_edges = list(zip(l_s_path, l_s_path[1:]))

# Draw the graph, then draw over the required edges in red.
pos = nx.spring_layout(G)

nx.draw(G, pos=pos, with_labels=True)
nx.draw_networkx_edges(G, edge_color='r', edgelist=l_s_path_edges, pos=pos)