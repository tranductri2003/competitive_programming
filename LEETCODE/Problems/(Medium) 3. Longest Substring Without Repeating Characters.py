from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res = 0
        i = 0
        lastPos = defaultdict(lambda: -1)
        while i < len(s):
            temp = 0
            while i < len(s) and lastPos[s[i]] == -1:
                lastPos[s[i]] = i
                temp += 1
                i += 1
                res = max(res, temp)
            if i == len(s):
                break
            else:
                i = lastPos[s[i]]+1
                lastPos = defaultdict(lambda: -1)
        return res
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         longest_string = []
#         current_string = []

#         for c in s:

#             if c in current_string:
#                 index = current_string.index(c) + 1
#                 current_string = current_string[index:]
#                 current_string.append(c)
#             else:
#                 current_string.append(c)
#                 if len(current_string) > len(longest_string):
#                     longest_string = current_string

#         return len(longest_string)
