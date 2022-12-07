# from collections import defaultdict


# n, k = list(map(int, input().split()))
# a = list(map(int, input().split()))

# res = []
# vitriso0 = []
# for i in range(n):
#     if a[i] == 0:
#         vitriso0.append(i)

# temp = 0
# check = False
# i = 0
# while i < n:
#     if a[i] == 0:
#         res.append(0)
#         i += 1
#     else:
#         temp = 0
#         for j in range(i, n):
#             if a[j] == 1:
#                 temp += 1
#                 i += 1
#             else:
#                 res.append(temp)
#                 break
#         if i == n:
#             res.append(temp)

# length = len(res)
# pos = []
# for i in range(length):
#     if res[i] == 0:
#         pos.append(i)

# data = []

# count = 0

# for i in range(len(pos)):
#     if pos[i] == 0:
#         if len(res) > 1:
#             data.append((count, res[pos[i]+1]+1))
#         else:
#             data.append((count, 1))
#     elif pos[i] == length-1:
#         data.append((count, res[pos[i]-1]+1))
#     else:
#         data.append((count, res[pos[i]-1]+res[pos[i]+1]+1))
#     count += 1

# data.sort(key=lambda x: -x[1])
# done = []
# for i in range(k):
#     done.append(data[i][0])
# for i in done:
#     a[vitriso0[i]] = 1


# kiemtra = []
# i = 0
# while i < n:
#     if a[i] == 0:
#         kiemtra.append(0)
#         i += 1
#     else:
#         temp = 0
#         for j in range(i, n):
#             if a[j] == 1:
#                 temp += 1
#                 i += 1
#             else:
#                 kiemtra.append(temp)
#                 break
#         if i == n:
#             kiemtra.append(temp)
# print(max(kiemtra))
# print(*a)


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
#!      Filename: O_Hard_Process.py
# *      Folder: D:\Code\Python\Codeforces\ProblemSet\Topic Stream Mashup Dynamic Programming
# ?      Author: TranDucTri2003
# TODO   CreatedAt: 08/26/2022 16:11:51
# ? -----------------------------------------------------------------------------------------------------


#! Tìm đoạn dài nhất có k chữ số 0
def getNum0(a, l, r):
    return a[r+1]-a[l]  # ! Số số 0 trong đoạn [l,r]


n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

preFix = [0]*(n+1)
for i in range(n):
    if a[i] == 0:
        preFix[i+1] = preFix[i]+1
    else:
        preFix[i+1] = preFix[i]


best = [0, (-1, -1)]
for i in range(0, n):
    l = i
    r = n
    while l < r:
        m = (l+r)//2
        if getNum0(preFix, i, m) > k:
            r = m
        else:
            l = m+1

    if r-i > best[0]:
        best[0] = r-i
        best[1] = (i, r-1)

print(best[0])
for i in range(n):
    if best[1][0] <= i <= best[1][1]:
        print(1, end=" ")
    else:
        print(a[i], end=" ")
