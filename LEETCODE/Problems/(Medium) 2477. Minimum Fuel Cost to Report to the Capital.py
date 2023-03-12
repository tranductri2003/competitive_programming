import math
from collections import defaultdict


class Solution(object):
    def minimumFuelCost(self, roads, seats):
        """
        :type roads: List[List[int]]
        :type seats: int
        :rtype: int
        """
        graph = defaultdict(list)
        visited = defaultdict(lambda: False)
        n = len(roads)
        count = [1]*(n+1)

        self.res = 0
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        visited[0] = True

        def DFS(node):
            for neighbor in graph[node]:
                if visited[neighbor] == False:
                    visited[neighbor] = True
                    DFS(neighbor)
                    self.res += math.ceil(count[neighbor]/seats)
                    count[node] += count[neighbor]
                    count[neighbor] = 0

        DFS(0)
        return (self.res)


t = Solution()
print(t.minimumFuelCost([[0, 1], [0, 2], [0, 3]], 5))
print(t.minimumFuelCost([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2))
# print(t.minimumFuelCost([[0, 1], [0, 2], [0, 3]], 5))
