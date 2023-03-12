from collections import defaultdict
class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        m=defaultdict(lambda:0)
        n=len(basket1)
        x=basket2[-1]
        for i in range(0,n):
            m[basket1[i]]+=1
            m[basket2[i]]-=1
            
        flag=False
        
        mi=x
        for i in m:
            mi=min(mi)



t = Solution()
print(t.minCost([4, 2, 2, 2], [1, 4, 1, 2]))
