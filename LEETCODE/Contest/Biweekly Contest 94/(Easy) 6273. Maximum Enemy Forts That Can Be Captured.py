class Solution(object):
    def captureForts(self, forts):
        """
        :type forts: List[int]
        :rtype: int
        """
        data = []
        for i in range(0, len(forts)):
            if forts[i] == 1:
                data.append(i)

        res = 0
        for num in data:
            temp1 = 0
            if -1 in forts[num:]:
                for i in range(num+1, len(forts)):
                    if forts[i] == 0:
                        temp1 += 1
                    if forts[i] == 1:
                        temp1 = 0
                    if forts[i] == -1:
                        break
            temp2 = 0
            if -1 in forts[0:num]:
                for i in range(num-1, -1, -1):
                    if forts[i] == 0:
                        temp2 += 1
                    if forts[i] == 1:
                        temp2 = 0
                    if forts[i] == -1:
                        break
            res = max(res, temp1, temp2)
        return res


t = Solution()
print(t.captureForts([-1, -1, 0, 1, 0, 0, 1, -1, 1, 0]))
