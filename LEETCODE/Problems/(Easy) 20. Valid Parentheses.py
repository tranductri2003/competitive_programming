class Solution(object):
    def isValid(self, s):

        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if (s[i] == ')' and stack[-1] == "(") or (s[i] == ']' and stack[-1] == "[") or (s[i] == '}' and stack[-1] == "{"):
                    stack.pop(-1)
                else:
                    return False
        if stack:
            return False
        else:
            return True
