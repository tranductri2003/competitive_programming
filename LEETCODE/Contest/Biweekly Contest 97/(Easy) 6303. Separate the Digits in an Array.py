class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            for i in str(num):
                res.append(int(i))
        return res


t = Solution()
print(t.separateDigits([7, 1, 3, 9]))
