from collections import defaultdict


class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):

        root = {}
        for cha in "abcdefghijklmnopqrstuvwxyz":
            root[cha] = cha

        def find(c):
            while root[c] != c:
                c = root[c]
            return c

        for i in range(len(s1)):
            r1 = find(s1[i])
            r2 = find(s2[i])
            if r1 > r2:
                root[r1] = r2
            else:
                root[r2] = r1

        res = ""
        for cha in baseStr:
            res += str(find(cha))
        return res
