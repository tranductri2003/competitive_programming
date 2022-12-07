from functools import cache


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        M = len(word1)
        N = len(word2)

        @cache
        def recursion(i, j):
            if i == M and j == N:
                return 0
            if i == M:
                return N-j
            if j == N:
                return M-i

            if word1[i] == word2[j]:
                return recursion(i+1, j+1)

            insert = recursion(i, j+1)+1
            delete = recursion(i+1, j)+1
            replace = recursion(i+1, j+1)+1

            return min(insert, delete, replace)
        return recursion(0, 0)


t = Solution()
print(t.minDistance("horse", "ros"))
