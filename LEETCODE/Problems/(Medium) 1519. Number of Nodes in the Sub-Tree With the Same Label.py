from collections import defaultdict
import string


class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        alphabet = string.ascii_lowercase
        count = defaultdict(lambda: defaultdict(lambda: 0))

        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        def DFS(node, parent):
            for child in tree[node]:
                if child != parent:
                    DFS(child, node)
                    for character in alphabet:
                        count[node][character] += count[child][character]
            count[node][labels[node]] += 1
        DFS(0, -1)
        res = []
        for i in range(n):
            res.append((count[i][labels[i]]))
        return res


t = Solution()
t.countSubTrees(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], "abaedcd")
