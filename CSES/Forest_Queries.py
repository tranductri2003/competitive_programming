
# ? -----------------------------------------------------------------------------------------------------
# ?　　　　　　　　　　　 ∧＿∧
# ?　　　　　 ∧＿∧ 　 （´<_｀ ）
# ?　　　　 （ ´_ゝ`）　/　 ⌒i
# ?　　　　／　　　＼　 　  |　|
# ?　　　 /　　 /￣￣￣￣/　|　 |
# ?　 ＿_(__ﾆつ/　    ＿/ .| .|＿＿＿＿
# ?　 　　　＼/＿＿＿＿/　（u　⊃
# ?
# ?		 /\_/\
# ?		(= ._.)
# ?		/ >WA \>AC
# ?
#       WELCOME TO MY CODING SPACE
#!      Filename: Forest_Queries.py
# *      Folder: D:\Code\Python\Competitive Programming\CSES
# ?      Author: TranDucTri2003
# TODO   CreatedAt: 09/04/2022 19:24:50
# ? -----------------------------------------------------------------------------------------------------

n, q = list(map(int, input().split()))

forest = []
dp = []
for i in range(n+1):
    forest.append([])
    dp.append([])
    for j in range(n+1):
        forest[i].append(".")
        dp[i].append(0)
for i in range(n):
    s = input()
    for j in range(n):
        forest[i+1][j+1] = s[j]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1]
        if forest[i][j] == "*":
            dp[i][j] += 1

# for i in range(n+1):
#     print(*dp[i])

for i in range(q):
    a, b, c, d = list(map(int, input().split()))
    print(dp[c][d]-dp[a-1][d]-dp[c][b-1]+dp[a-1][b-1])
    # print("dp[c][d]", dp[c][d])
    # print("dp[c-1][d]", dp[c-1][d])
    # print("dp[c][d-1]", dp[c][d-1])
    # print("dp[a-1][b-1]", dp[a-1][b-1])
