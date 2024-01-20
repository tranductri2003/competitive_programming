class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed.insert(0, 1)
        flowerbed.insert(1, 0)
        flowerbed.append(0)
        flowerbed.append(1)
        
        pos1 = []
        for i in range(len(flowerbed)):
            if flowerbed[i] ==1:
                pos1.append(i)
        
        res = 0
        for i in range(len(pos1)-1):
            start = pos1[i]
            end = pos1[i+1]
            space = end - start - 1
            if (space - 2) %2==1:
                res += max(0,(space - 2) //2 + 1)
            else:
                res += max(0, (space - 2) // 2)
        return res>=n