class Solution(object):

    def vowelStrings(self, words, queries):
        vowels = ['a', 'e', 'i', 'o', 'u']
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        data = [0]
        temp = 0
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                temp += 1
            data.append(temp)

        res = []
        for l, r in queries:
            res.append(data[r+1]-data[l])
        return res


t = Solution()
print(t.vowelStrings(["a", "e", "i"], [[0, 2], [0, 1], [2, 2]]))
