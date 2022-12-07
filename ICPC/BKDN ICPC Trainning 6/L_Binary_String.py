# from random import randint
# # K = int(input())
# # s = input()
# for _ in range(10000):
#     K = randint(1, 2**60)
#     s = ""
#     for i in range(1, 61):
#         temp = randint(1, 2)
#         if temp == 1:
#             s = s+'1'
#         else:
#             s = s+"0"
#     print(K)
#     print(s)

#     res = 0
#     while int(s, 2) > K:
#         print("gia tri la", int(s, 2))
#         pos = -1
#         for i in range(1, len(s)):
#             if s[i] == '1':
#                 pos = i

#         if pos != -1:
#             s = list(s)
#             s.pop(pos)
#             s = "".join(s)
#             res += 1
#         else:
#             s = list(s)
#             s.pop(1)
#             s = "".join(s)
#             res += 1

#     if int(s, 2) <= K:
#         print("ddunga")
#     else:
#         print("sai")
#         print(K, s)
#         break

# # print(res)
K = int(input())
s = input()

res = 0
while int(s, 2) > K:
    pos = -1
    if len(s) == 1:
        break
    for i in range(1, len(s)):
        if s[i] == '1':
            pos = i
            break

    if pos != -1:
        s = list(s)
        s.pop(pos)
        s = "".join(s)
        res += 1
    else:
        s = list(s)
        s.pop(1)
        s = "".join(s)
        res += 1
print(res)
