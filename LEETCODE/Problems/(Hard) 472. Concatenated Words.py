from collections import defaultdict
from functools import lru_cache


class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        #     """
        #     :type words: List[str]
        #     :rtype: List[str]
        #     """
        #     check = defaultdict(lambda: False)
        #     for word in words:
        #         check[word] = True

        #     @lru_cache
        #     def recursion(string, time):
        #         # print(string)
        #         if len(string) == 0:
        #             return 1, time
        #         for i in range(1, len(string)+1):
        #             # print(string[:i])
        #             if check[string[:i]] == True:
        #                 # Printing the word that is being checked.
        #                 # print(string[:i])
        #                 temp, count = recursion(string[i:], time+1)
        #                 if temp == 0:
        #                     pass
        #                 else:
        #                     return 1, count
        #         return 0, time

        #     res = []
        #     for word in words:
        #         # print(word)
        #         status, time = recursion(word, 0)
        #         if status == 1 and time >= 2:
        #             res.append(word)
        #     # recursion("catsdogcats", 0)
        #     return res

        words = set(words)

        @lru_cache
        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in words and suffix in words:
                    return True
                if prefix in words and dfs(suffix):
                    return True
                if dfs(prefix) and suffix in words:
                    return True
            return False

        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        return res


t = Solution()
print(t.findAllConcatenatedWordsInADict(
    ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]))
