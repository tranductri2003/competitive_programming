
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
#!      Filename: A_3_-palindrome.py
# *      Folder: D:\Code\Python\Codeforces\ProblemSet\Topic Stream Mashup Constructives
# ?      Author: TranDucTri2003
# TODO   CreatedAt: 08/27/2022 09:48:06
# ? -----------------------------------------------------------------------------------------------------


#! Không có palindrome độ dài 3
# => aabbaabbaabb
n = int(input())
res = []
for i in range(n):
    if i % 4 == 0 or i % 4 == 1:
        res.append('a')
    else:
        res.append('b')
res = "".join(res)
print(res)
