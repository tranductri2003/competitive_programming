from collections import defaultdict


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.check = defaultdict(lambda: -1)
        for num in nums:
            self.check[num] = 1
        i = 1
        while self.check[i] == 1:
            i += 1
        return i


t = Solution()
print(t.firstMissingPositive([7, 8, 9, 11, 12]))
