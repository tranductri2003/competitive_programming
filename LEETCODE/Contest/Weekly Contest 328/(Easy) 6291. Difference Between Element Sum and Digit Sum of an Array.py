class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res1 = sum(nums)
        res2 = 0
        for num in nums:
            num = str(num)
            for i in range(len(num)):
                res2 += int(num[i])
        return abs(res1-res2)


t = Solution()
print(t.differenceOfSum([1, 2, 3, 4]))
