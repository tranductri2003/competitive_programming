
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
#!      Filename: D_Walking_Between_Houses.py
# *      Folder: D:\Code\Python\Codeforces\ProblemSet\Topic Stream Mashup Constructives
# ?      Author: TranDucTri2003
# TODO   CreatedAt: 08/28/2022 22:37:47
# ? -----------------------------------------------------------------------------------------------------


# n, k, s = list(map(int, input().split()))


# # 1->n ->1 ->n:   tong cong la k lan
# toiDa = (n-1)*k
# toiThieu = k

# if s > toiDa or s < toiThieu:
#     print("NO")
# else:
#     print("YES")

#     if k == 1:
#         res = [1+s]
#         print(*res)
#     else:
#         if s == toiThieu:
#             for i in range(k):
#                 if i % 2 == 0:
#                     print(2, end=" ")
#                 else:
#                     print(1, end=" ")
#         elif s == toiDa:
#             for i in range(k):
#                 if i % 2 == 0:
#                     print(n, end=" ")
#                 else:
#                     print(1, end=" ")
#         else:
#             res = []
#             for i in range(k):
#                 if i % 2 == 0:
#                     res.append(2)
#                 else:
#                     res.append(1)
#             # print(res)
#             pos = 0
#             rest = s-k

#             if k % 2 == 1:   # 2 1 2 1 2
#                 for i in range(0, k-1, 2):

#                     up = min((rest-rest % 2)//2, n-2)
#                     rest -= up*2
#                     res[i] += up
#                     if rest <= 0:
#                         break
#                     if rest <= n-2:
#                         res[-1] += rest
#                         break
#             else:     # 1 2 1 2 1 2

#                 for i in range(0, k, 2):
#                     if rest <= 0:
#                         break
#                     if rest <= 2*(n-2):
#                         if rest % 2 == 0:
#                             res[-2] += rest//2
#                             break
#                         else:
#                             res[-2] += rest//2+1
#                             res[-1] += 1
#                             break

#                     up = min((rest-rest % 2)//2, n-2)
#                     rest -= up*2
#                     res[i] += up
#             print(*res)


n, k, s = list(map(int, input().split()))


if s < k or s > k*(n-1):
    print("NO")
else:

    dis = [1]*k  # Mặc định mỗi bước phải di chuyển ít nhất là 1

    rest = s-k
    for i in range(k):
        temp = min(n-2, rest)  # Đi thêm n-2 hoặc là quãng đường còn lại
        dis[i] += temp
        rest -= temp
    # print(dis)  # Khoảng cách phải đi ở bước thứ i
    cur = 1

    res = [0]*k
    for i in range(k):
        if dis[i]+cur <= n:
            res[i] = cur+dis[i]
            cur = res[i]
        else:
            res[i] = cur-dis[i]
            cur = res[i]

    print("YES")
    print(*res)


# def step(cur, x):
#     if(cur - x > 0):
#         return cur - x
#     else:
#         return cur + x


# n, k, s = map(int, input().split())
# cur = 1

# if(k > s or k * (n - 1) < s):
#     print('NO')
# else:
#     print('YES')
#     while(k > 0):
#         l = min(n - 1, s - k +1)
#         cur = step(cur, l)
#         print(cur, end = ' ')
#         s -= l
#         k -= 1
