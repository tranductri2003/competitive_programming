class Solution(object):
    def makeStringsEqual(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: bool
        """
        n = len(s)
        if target == '0'*n and '1' in s:
            return False
        elif s == '0'*n and '1' in target:
            return False
        else:
            return True


t = Solution()
print(t.makeStringsEqual("1010", "0110"))
