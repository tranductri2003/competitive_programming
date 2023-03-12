class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        n = len(score)
        m = len(score[0])

        data = []
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(score[i][j])
            data.append((temp, score[i][k]))
        data.sort(key=lambda x: x[1], reverse=True)
        res = []
        for i in range(n):
            res.append(data[i][0])
        return (res)


t = Solution()
t.sortTheStudents([[3, 4], [5, 6]], 0)
