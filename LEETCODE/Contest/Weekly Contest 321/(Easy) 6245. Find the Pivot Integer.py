class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        for x in range(1, n+1):
            temp1 = 0
            temp2 = 0
            for i in range(1, x+1):
                temp1 += i
            for i in range(x, n+1):
                temp2 += i
            if temp1 == temp2:
                return x
        return -1


t = Solution()
print(t.pivotInteger(4))
