from collections import defaultdict


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        n = len(points)
        for i in range(0, n):
            for j in range(0, n):
                temp = 2
                if i != j:

                    for k in range(0, n):
                        if k != i and k != j:
                            print(i, j, k)
                            print(points[k][1]-points[j][1],
                                  points[j][1]-points[i][1])
                            if (points[k][0]-points[j][0])/(points[k][1]-points[j][1]) == (points[j][0]-points[i][0])/(points[j][1]-points[i][1]):
                                temp += 1
                res = max(res, temp)
        print(res)


t = Solution()
t.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]])
