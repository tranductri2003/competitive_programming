class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        l = 0
        r = 2**31-1
        while l <= r:
            m = (l+r) // 2
            print(l, m, r)
            if m**2 == x:
                return m
            elif m**2 > x:
                r = m-1
            else:
                l = m+1
        return r


t = Solution()
t.mySqrt(2)
