class Solution(object):

    def lengthOfLIS(self, nums):

        data = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    data[i] = max(data[i], data[j]+1)
        return max(data)
