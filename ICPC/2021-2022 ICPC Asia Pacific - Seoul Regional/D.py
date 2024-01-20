from collections import defaultdict

def find_min_difference(graph):
    n = len(graph)
    visited = set()
    min_difference = float('inf')

    for start_vertex in range(n):
        if start_vertex not in visited:
            # Perform DFS to find a connected component
            component = dfs(graph, start_vertex, visited)

            # Initialize DP array
            dp = [False] * (n // 2 + 1)
            dp[0] = True

            # Calculate DP array
            for vertex in component:
                for j in range(n // 2, 0, -1):
                    if j >= vertex and dp[j - vertex]:
                        dp[j] = True

                # Print dp array for each vertex in the component
                print(f"DP array for vertex {vertex}: {dp}")

            # Find the minimum difference for this component
            for j in range(n // 2 + 1):
                if dp[j]:
                    min_difference = min(min_difference, abs(n - 2 * j))

    return min_difference

def dfs(graph, start, visited):
    component = set()
    stack = [start]

    while stack:
        current_vertex = stack.pop()
        if current_vertex not in visited:
            visited.add(current_vertex)
            component.add(current_vertex)
            stack.extend(graph[current_vertex] - visited)

    return component

# Example usage:
n, m = list(map(int, input().split()))
edges = []
for _ in range(m):
    u, v = list(map(int, input().split()))
    edges.append((u, v))

graph = defaultdict(set)

for edge in edges:
    graph[edge[0]].add(edge[1])
    graph[edge[1]].add(edge[0])

result = find_min_difference(graph)

if result == float('inf'):
    print(-1)
else:
    print(result)
