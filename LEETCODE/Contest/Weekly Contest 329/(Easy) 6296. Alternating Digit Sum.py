class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(n)
        res = 0
        for i in range(len(n)):
            if i % 2 == 0:
                res += int(n[i])
            else:
                res -= int(n[i])
        return res


t = Solution()
print(t.alternateDigitSum(886996))
