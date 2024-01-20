class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1+str2 != str2+str1:
            return ""
        else:
            from math import gcd
            return str1[:gcd(len(str1), len(str2))]