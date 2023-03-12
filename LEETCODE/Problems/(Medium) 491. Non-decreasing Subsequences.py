from itertools import combinations


class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        data = []
        for i in range(0, n+1):
            data .extend(list(combinations(nums, i)))
        res = []
        for num in data:
            num = list(num)
            if num == sorted(num) and len(num) >= 2:
                res.append(list(num))
        ans = []
        for num in res:
            if num not in ans:
                ans.append(num)
        print(ans)
        return ans


t = Solution()
t.findSubsequences([4, 6, 7, 7])
