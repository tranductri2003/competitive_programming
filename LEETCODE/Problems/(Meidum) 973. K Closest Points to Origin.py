
import math


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        length = len(points)
        data = []
        for num in points:
            data.append((num, math.sqrt(num[0]**2+num[1]**2)))
        data = sorted(data, key=lambda x: x[1])

        res = []
        for i in range(k):
            res.append(data[i][0])
        return res


t = Solution()
print(t.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
