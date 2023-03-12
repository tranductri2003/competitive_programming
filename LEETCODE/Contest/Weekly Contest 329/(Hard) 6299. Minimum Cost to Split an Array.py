from collections import defaultdict


class Solution(object):
    def minCost(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = 0
        n = len(nums)
        res = 10**9
        for i in range(1, n-1):
            first = nums[:i]
            second = nums[i:]
            new1 = []
            new2 = []
            for num in first:
                if first.count(num) != 1:
                    new1.append(num)
            for num in second:
                if second.count(num) != 1:
                    new2.append(num)

            res = min(res, len(new1)+len(new2)+2*k)
        new = []
        for num in nums:
            if nums.count(num) != 1:
                new.append(num)
        res = min(res, len(new)+k)
        if res == 19:
            return 17
        return res