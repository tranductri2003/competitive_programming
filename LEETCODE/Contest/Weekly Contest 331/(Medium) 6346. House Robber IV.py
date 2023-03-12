from functools import lru_cache
from collections import defaultdict


class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        @lru_cache
        def recur(take, current):
            if take == 0:
                dp[take][current] = 0
                return 0
            else:
                a = min(recur(take-1, current),
                        recur(take-1, current-2)+nums[current])
                dp[take][current] = a
                return a

        dp = defaultdict(lambda: defaultdict(lambda: 10**9))
        print(dict(dp)


t = Solution()
t.minCapability([2, 3, 5, 9], 2)
