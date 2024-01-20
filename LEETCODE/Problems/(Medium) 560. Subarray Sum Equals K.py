from collections import defaultdict 

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        count = 0
        tempSum = 0
        
        dict = defaultdict(lambda: 0)
        dict[0] = 1

        for i in range(len(nums)):
            tempSum += nums[i]
            count += dict[tempSum - k]
            dict[tempSum] += 1
        
        return count


        
                

        