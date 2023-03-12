class Solution(object):
    def singleNonDuplicate(self, nums):
        l = 0
        n = len(nums)
        if n == 1:
            return nums[0]
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if (m == 0 and nums[m] != nums[m+1]) or (m == n-1 and nums[m] != nums[m-1]):
                return nums[m]
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            else:
                if nums[m] == nums[m-1]:
                    secondNum = m
                else:
                    secondNum = m-1
                if secondNum % 2 == 1:
                    l = m+1
                else:
                    r = m-1


t = Solution()
print(t.singleNonDuplicate([1]))
