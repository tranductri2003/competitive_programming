class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def check(s):
            temp = s.split(".")
            for num in temp:
                if len(num) != 1 and num[0] == "0":
                    return False
                if 0 <= int(num) <= 255:
                    pass
                else:
                    return False
            return True

        n = len(s)
        res = []
        for i in range(1, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    temp = s[:i]+"."+s[i:j]+"."+s[j:k]+"."+s[k:]
                    if check(temp):
                        res.append(temp)
        return res
