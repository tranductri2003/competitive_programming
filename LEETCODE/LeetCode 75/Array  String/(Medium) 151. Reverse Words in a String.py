class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = list(map(str, s.split()))
        s = s[::-1]
        return " ".join(s).strip()
