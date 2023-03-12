class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        res1 = []
        res2 = []

        num = str(num)

        for i in range(0, 10):
            temp = ""
            for j in range(len(num)):
                if num[j] == str(i):
                    temp += "9"
                else:
                    temp += num[j]
            res1.append(int(temp))

        for i in range(0, 10):
            temp = ""
            for j in range(len(num)):
                if num[j] == str(i):
                    temp += "0"
                else:
                    temp += num[j]
            res2.append(int(temp))
        return (max(res1)-min(res2))


t = Solution()
print(t.minMaxDifference(90))
