from collections import defaultdict


class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        check = defaultdict(lambda: True)
        for num in banned:
            check[num] = False

        res = 0
        current = 0
        i = 1
        while current < maxSum:
            if i > n:
                break
            if current+i <= maxSum:
                if check[i] == True:
                    res += 1
                    current += i
                    check[i] = False
            else:
                break
            i += 1
        return res


t = Solution()
print(t.maxCount([11], 7, 50))
