from collections import defaultdict, deque


class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        red = defaultdict(lambda: False)
        blue = defaultdict(lambda: False)
        visited = defaultdict(lambda: False)
        res = [10**9]*n
        res[0] = 0
        for u, v in redEdges:
            red[(u, v)] = True
            graph[u].append(v)
        for u, v in blueEdges:
            blue[(u, v)] = True
            graph[u].append(v)
        queue = deque()

        # -1: red
        # 0: whatever
        # 1: blue
        # current node, previous edge 's color, maxDistance
        queue.append((0, 0, 0))
        while queue:
            u, c, d = queue.popleft()
            for v in graph[u]:
                if visited[(u, v, c)] == False:
                    if c == 0:  # whatever
                        if red[(u, v)] and blue[(u, v)]:
                            color = 0
                        elif red[(u, v)] and not blue[(u, v)]:
                            color = -1
                        elif not red[(u, v)] and blue[(u, v)]:
                            color = 1
                        queue.append((v, color, d+1))
                        res[v] = min(res[v], d+1)
                        visited[(u, v, c)] = True
                    elif c == -1 and blue[(u, v)]:
                        queue.append((v, 1, d+1))
                        res[v] = min(res[v], d+1)
                        visited[(u, v, c)] = True
                    elif c == 1 and red[(u, v)]:
                        queue.append((v, -1, d+1))
                        res[v] = min(res[v], d+1)
                        visited[(u, v, c)] = True
        for i in range(n):
            if res[i] == 10**9:
                res[i] = -1
        return res


t = Solution()
# t.shortestAlternatingPaths(5, [[0, 1], [1, 2], [2, 3], [3, 4]], [
#                            [1, 2], [2, 3], [3, 1]])
t.shortestAlternatingPaths(3, [[0, 1], [0, 2]], [[1, 0]])
