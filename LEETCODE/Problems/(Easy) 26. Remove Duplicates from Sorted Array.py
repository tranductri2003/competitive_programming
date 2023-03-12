class Solution(object):
    def removeDuplicates(self, nums):
        temp = sorted(list(set(nums)))
        for i in range(len(temp)):
            nums[i] = temp[i]
        return len(temp)
