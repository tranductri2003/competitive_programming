
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
#!      Filename: B_EhAb_AnD_gCd.py
# *      Folder: D:\Code\Python\Competitive Programming\CODEFORCES\ProblemSet\Topic Stream Mashup Number Theory
# ?      Author: TranDucTri2003
# TODO   CreatedAt: 09/12/2022 10:45:50
# ? -----------------------------------------------------------------------------------------------------

# You are given a positive integer x. Find any such 2 positive integers a and b such that GCD(a,b)+LCM(a,b)=x.

t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        print(n//2, n//2)
    else:

        print(1, n-1)
