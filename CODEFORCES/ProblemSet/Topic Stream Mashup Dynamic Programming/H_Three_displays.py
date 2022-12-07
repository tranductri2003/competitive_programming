
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
#!      Filename: H_Three_displays.py
# *      Folder: D:\Code\Python\Codeforces\ProblemSet\Topic Stream Mashup Dynamic Programming
# ?      Author: TranDucTri2003
# TODO   CreatedAt: 08/09/2022 11:07:21
# ? -----------------------------------------------------------------------------------------------------

n = int(input())
a = list(map(int, input().split()))
p = list(map(int, input().split()))
# res=10**9
# for i in range(n-2):
#     for j in range(i+1,n-1):
#         for k in range(j+1,n):
#             if a[i]<a[j]<a[k]:
#                 res=min(res,p[i]+p[j]+p[k])
# if res==10**9:
#     print(-1)
# else:
#     print(res)


#! Maria Stepanovna wants to rent such three displays with indices i<j<k
#! that the font size increases if you move along the road in a particular direction.
#! Namely, the condition si<sj<sk should be held

res = 10**9

for j in range(1, n-1):
    left = 10**9
    for i in range(0, j):
        if a[i] < a[j]:
            left = min(left, p[i])
    right = 10**9
    for k in range(j+1, n):
        if a[k] > a[j]:
            right = min(right, p[k])

    res = min(res, left+p[j]+right)


if res >= 10**9:
    print(-1)
else:
    print(res)
