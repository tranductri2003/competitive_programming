from collections import defaultdict


class Solution(object):
    def distinctNames(self, ideas):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        suffixes = defaultdict(set)
        for word in ideas:
            suffixes[word[0]].add(word[1:])

        res = 0
        for i in range(0, len(alphabet)-1):
            for j in range(i+1, len(alphabet)):
                common = len(suffixes[alphabet[i]] & suffixes[alphabet[j]])
                # common = len(suffixes[alphabet[i]].intersection(suffixes[alphabet[j]]))
                res += 2*(len(suffixes[alphabet[i]])-common) * \
                    (len(suffixes[alphabet[j]])-common)
        return res
