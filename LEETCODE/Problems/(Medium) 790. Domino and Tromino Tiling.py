class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(1001)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = 2*dp[i-1]+dp[i-3]
        return dp[n] % (10**9+7)
