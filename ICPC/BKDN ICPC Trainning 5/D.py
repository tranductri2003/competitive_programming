from collections import defaultdict
n, m = list(map(int, input().split()))
graph = []
for i in range(n):
    u, v, w = list(map(int, input().split()))
    graph.append((u, v, w))

graph.sort()
res = 0

check = defaultdict(lambda: 0)


for i in range(n):
    if check[graph[i][0]] == 0:
        check[graph[i][0]] += m-1
        check[graph[i][1]] += m
        res += 1
    else:
        check[graph[i][0]] -= 1
        check[graph[i][1]] += m
print(res)
