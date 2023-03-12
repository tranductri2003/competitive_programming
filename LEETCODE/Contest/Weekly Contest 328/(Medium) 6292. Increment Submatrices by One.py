import numpy as np


class Solution(object):
    def rangeAddQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[List[int]]
        """
        temp = []
        for i in range(n):
            temp.append([])
            for j in range(n):
                temp[i].append(0)
        matrix = np.array(temp)
        for query in queries:
            firstRow = query[0]
            firstCol = query[1]
            secondRow = query[2]
            secondCol = query[3]
            matrix[firstRow:secondRow+1, firstCol:secondCol+1] += 1
        return matrix


t = Solution()
print(t.rangeAddQueries(3, [[1, 1, 2, 2], [0, 0, 1, 1]]))
