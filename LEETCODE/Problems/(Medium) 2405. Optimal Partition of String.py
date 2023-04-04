from collections import defaultdict


class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        res = 0
        check = defaultdict(lambda: False)
        while i < len(s):
            while i < len(s) and check[s[i]] == False:
                check[s[i]] = True
                i += 1
            check = defaultdict(lambda: False)
            res += 1

        return res
