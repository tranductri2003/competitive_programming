class Solution(object):
    def xorBeauty(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        key = nums[0]
        for i in range(1, len(nums)):
            key ^= nums[i]
        return key


t = Solution()
print(t.xorBeauty([1, 4]))
