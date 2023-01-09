class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        # Sort based on end points
        points.sort(key=lambda x: x[1])
        res = 1
        curEnd = points[0][1]
        for start, end in points:
            if start > curEnd:
                curEnd = end
                res += 1
        return res
