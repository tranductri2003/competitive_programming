class Solution(object):
    def minimizeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        data = []
        data.append(nums[-2]-nums[1])
        data.append(nums[-1]-nums[2])
        data.append(nums[-3]-nums[0])
        return min(data)


t = Solution()
print(t.minimizeSum([31, 25, 72, 79, 74, 65]))
