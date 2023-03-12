import math


class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        gifts.sort(reverse=True)
        i = 0
        while i < k:
            temp = max(gifts)
            pos = gifts.index(temp)
            gifts[pos] = math.sqrt(gifts[pos])//1
            i += 1
        res = int(sum(gifts))
        return res


t = Solution()
print(t.pickGifts([25, 64, 9, 4, 100], 4))
