from collections import defaultdict


class Solution(object):
    def numberOfGoodPaths(self, vals, edges):
        def find(i):
            if root[i] != i:
                root[i] = find(root[i])
            return root[i]
            # while root[i] != i:   got TLE
            #     i = root[i]
            # return i

        n = len(vals)
        edges.sort(key=lambda x: max(vals[x[0]], vals[x[1]]))
        root = [i for i in range(n)]
        size = [1]*n

        goodPaths = n
        for u, v in edges:
            rootU = find(u)
            rootV = find(v)
            if vals[rootU] == vals[rootV]:
                goodPaths += size[rootU]*size[rootV]
                root[rootV] = rootU
                size[rootU] += size[rootV]
            elif vals[rootU] < vals[rootV]:
                root[rootU] = rootV
            else:
                root[rootV] = rootU
        return goodPaths


t = Solution()
t.numberOfGoodPaths([1, 3, 2, 1, 3], [[0, 1], [0, 2], [2, 3], [2, 4]])
