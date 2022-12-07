from functools import lru_cache


class Solution(object):

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        height, width = len(matrix), len(matrix[0])

        @lru_cache(None)
        def dfs(r, c):
            ans = 1
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                x, y = r + dx, c + dy
                if 0 <= x < height and 0 <= y < width and matrix[x][y] > matrix[r][c]:
                    ans = max(ans, dfs(x, y) + 1)
            return ans
        res = 0
        for i in range(height):
            for j in range(width):
                print(dfs(i, j))
                res = max(res, dfs(i, j))
        return res


t = Solution()
t.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]])
