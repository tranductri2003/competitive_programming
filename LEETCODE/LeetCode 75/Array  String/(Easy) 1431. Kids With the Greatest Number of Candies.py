class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        maxCandies = max(candies)
        res = [False] * len(candies)
        for i in range(len(res)):
            if candies[i] + extraCandies >= maxCandies:
                res[i] = True
        return res