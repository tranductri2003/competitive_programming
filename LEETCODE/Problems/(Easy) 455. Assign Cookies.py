class Solution(object):
    def findContentChildren(self, g, s):

        g.sort()  # Độ tham lam
        s.sort()  # Size bánh

        i = 0  # Độ tham lam
        j = 0  # Size bánh
        res = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                res += 1
                i += 1

            j += 1
        return res


t = Solution()
t.findContentChildren([1, 2], [1, 2, 3])
