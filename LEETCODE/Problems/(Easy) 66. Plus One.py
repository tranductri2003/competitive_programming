class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = ""
        for num in digits:
            res = res+str(num)

        res = list(str(int(res)+1))
        for i in range(len(res)):
            res[i] = int(res[i])
        return res
