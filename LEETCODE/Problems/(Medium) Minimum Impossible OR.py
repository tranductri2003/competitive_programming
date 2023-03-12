from collections import defaultdict


class Solution(object):
    def minImpossibleOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        check = defaultdict(lambda: False)
        for num in nums:
            check[num] = True

        i = 1
        while check[i] == True:
            i *= 2
        return i


t = Solution()
print(t.minImpossibleOR([2, 1]))
