from collections import defaultdict


class Solution(object):
    def findAnagrams(self, s, p):
        def check():
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            for cha in alphabet:
                if count[cha] != sample[cha]:
                    return False
            return True
        res = []
        if len(p) > len(s):
            return res
        else:
            count = defaultdict(int)
            sample = defaultdict(int)
            for i in range(len(p)):
                sample[p[i]] += 1
                count[s[i]] += 1
            if check():
                res.append(0)
            for i in range(len(p), len(s)):
                count[s[i-len(p)]] -= 1
                count[s[i]] += 1
                if check():
                    res.append(i-len(p)+1)
            return res
