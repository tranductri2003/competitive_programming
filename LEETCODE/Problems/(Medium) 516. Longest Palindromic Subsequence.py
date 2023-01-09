from collections import defaultdict


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
    # Let dp[i][j] = length of longest palindromic subsequence of substring s[i:j] (i<j), then

        dp = defaultdict(lambda: defaultdict(lambda: 0))
        for i in range(0, len(s)):  # ending point
            dp[i][i] = 1
            for j in range(i-1, -1, -1):  # starting point
                if s[i] == s[j]:
                    dp[i][j] = dp[i-1][j+1]+2
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j+1])

        return (dp[len(s)-1][0])


t = Solution()
print(t.longestPalindromeSubseq("bbbab"))
