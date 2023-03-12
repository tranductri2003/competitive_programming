from collections import defaultdict


class Solution(object):
    def checkInclusion(self, s1, s2):
        def check():
            for cha in alphabet:
                if count[cha] != sample[cha]:
                    return False
            return True
        if len(s1) > len(s2):
            return False
        else:
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            count = defaultdict(lambda: 0)
            sample = defaultdict(lambda: 0)
            for i in range(len(s1)):
                sample[s1[i]] += 1
                count[s2[i]] += 1

            if sample == count:
                return True
            else:
                for i in range(len(s1), len(s2)):
                    count[s2[i-len(s1)]] -= 1
                    count[s2[i]] += 1
                    if check():
                        return True
                return False
