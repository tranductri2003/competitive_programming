from collections import defaultdict


class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):

        graph = defaultdict(list)
        self.check = defaultdict(lambda: False)
        res = {}

        n = len(s1)
        for i in range(n):
            graph[s1[i]].append(s2[i])
            graph[s2[i]].append(s1[i])

        def DFS(source, temp):
            for destination in graph[source]:
                if self.check[destination] == False:
                    temp.append(destination)
                    self.check[destination] = True
                    DFS(destination, temp)

        character = "abcdefghijklmnopqrstuvwxyz"
        for cha in character:
            if self.check[cha] == False:
                temp = []
                temp.append(cha)
                DFS(cha, temp)
                temp.sort()
                for chaa in temp:
                    res[chaa] = temp[0]

        ans = []
        for cha in baseStr:
            ans.append(res[cha])
        return "".join(ans)


t = Solution()
t.smallestEquivalentString("aoaoaoao", "oaoaoaoa", "a")
