from collections import defaultdict


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = defaultdict(lambda: defaultdict(lambda: 0))
        pascal[1][1] = 1
        for i in range(2, numRows+1):
            for j in range(1, i+1):
                pascal[i][j] = pascal[i-1][j-1]+pascal[i-1][j]

        res = []
        for i in range(1, numRows+1):
            temp = []
            for j in range(1, i+1):
                temp.append(pascal[i][j])
            res.append(temp)
        return res
