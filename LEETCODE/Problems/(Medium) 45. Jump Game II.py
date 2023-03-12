from collections import defaultdict


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = defaultdict(lambda: 10**9)
        dp[0] = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, i+nums[i]+1):
                if j >= n:
                    break
                else:
                    dp[j] = min(dp[j], dp[i]+1)
        return dp[n-1]
