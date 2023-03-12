class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        num1 = s.count('1')
        num0 = s.count('0')
        num1SoFar = 0
        num0SoFar = 0
        n = len(s)
        res = 10**9
        for i in range(n):
            res = min(res, num1SoFar+num0-num0SoFar)
            if s[i] == "0":
                num0SoFar += 1
            else:
                num1SoFar += 1
        return min(res, num0, num1)
