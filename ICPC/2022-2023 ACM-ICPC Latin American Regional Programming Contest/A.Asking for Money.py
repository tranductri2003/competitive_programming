
from collections import defaultdict


def dfs(node, ancestor):
    visited[node] = 1
    for neighbor in graph[node]:
        if neighbor != ancestor and not visited[neighbor]:
            dfs(neighbor, ancestor)


n = int(input())
visited = [0] * 1005
graph = defaultdict(list)
edges = []
for _ in range(n):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((u, v))
    graph[u].append(_)
    graph[v].append(_)

for i in range(n):
    count = [0] * n
    for node in [i, edges[i][0], edges[i][1]]:
        visited = [0] * 1005
        dfs(node, i)
        for j in range(n):
            count[j] += visited[j]

    can = 0
    print(count)
    for j in range(n):
        if count[j] == 3:
            can = 1
            break
    # print("Y" if can else "N", end="")
