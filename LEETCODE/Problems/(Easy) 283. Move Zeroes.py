class Solution(object):
    def moveZeroes(self, nums):
        i = 0  # Vị trí đang xét
        j = 0  # Vị trí an toàn để dồn các số lên
        for i in range(len(nums)):
            if nums[i] != 0:  # Dồn lên
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
