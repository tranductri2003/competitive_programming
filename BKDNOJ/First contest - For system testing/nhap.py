class Solution:
    def generateParenthesis(self, n: int):
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans
n,k=list(map(int,input().split()))
n=n//2
t=Solution()
res=t.generateParenthesis(n)
print(res[k-1])