class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        posS = 0
        posT = 0
        while posS < len(s) and posT < len(t):
            if s[posS] == t[posT]:
                posT += 1
                posS += 1
            else:
                posS += 1
        return len(t)-posT


t = Solution()
print(t.appendCharacters("z", "abcde"))
