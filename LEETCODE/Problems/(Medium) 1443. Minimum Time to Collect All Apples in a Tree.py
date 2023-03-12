from collections import defaultdict


class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """

        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        def DFS(node, parent):   # how much time it costs to collect all apples in the subtree of the node
            totalTime = 0
            childrenTime = 0

            for child in tree[node]:
                if child != parent:
                    childrenTime = DFS(child, node)
                    if childrenTime or hasApple[child]:
                        totalTime += childrenTime+2

            return totalTime
        return DFS(0, -1)


# from collections import defaultdict


# class Solution(object):
#     def minTime(self, n, edges, hasApple):
#         """
#         :type n: int
#         :type edges: List[List[int]]
#         :type hasApple: List[bool]
#         :rtype: int
#         """

#         tree = defaultdict(list)
#         for u, v in edges:
#             tree[u].append(v)
#             tree[v].append(u)

#         def DFS(node, parent):
#             res = 0
#             for neighbor in tree[node]:
#                 if neighbor != parent:
#                     res += DFS(neighbor, node)

#             if hasApple[node] == True or res != 0:
#                 res += 2
#             return res

#         res = DFS(0, -1)
#         if DFS(0, -1) == 0:
#             return res
#         else:
#             return res-2
