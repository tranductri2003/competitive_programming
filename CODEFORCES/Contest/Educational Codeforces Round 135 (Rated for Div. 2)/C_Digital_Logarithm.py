# from collections import defaultdict
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     res = 0

#     check = defaultdict(lambda: 0)
#     for num in b:
#         check[num] = 1

#     anew = []
#     bnew = []
#     for num in a:
#         if check[num] == 0:
#             anew.append(num)
#         else:
#             check[num] = 2

#     for num in b:
#         if check[num] != 2:
#             bnew.append(num)

#     print(anew)
#     print(bnew)
#     print(res)

#     # Tới đây là ok

#     for i in range(len(anew)):
#         if anew[i] > 9:
#             anew[i] = len(str(anew[i]))
#             res += 1
#         if bnew[i] > 9:
#             bnew[i] = len(str(bnew[i]))
#             res += 1

#     print(anew)
#     print(bnew)
#     check = defaultdict(lambda: 0)
#     for num in bnew:
#         check[num] = 1

#     anewnew = []
#     bnewnew = []

#     for num in anew:
#         if check[num] == 0:
#             anewnew.append(num)
#         else:
#             check[num] = 2

#     for num in bnew:
#         if check[num] != 2:
#             bnewnew.append(num)

#     print(anewnew)
#     print(bnewnew)
#     print(res)

#     print()
#     print()

# #   2 3
# #   1 100
import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = 0

    for i in range(n):
        a[i] = -a[i]
        b[i] = -b[i]

    heapq.heapify(a)
    heapq.heapify(b)
    while a and b:
        tempa = -a[0]
        tempb = -b[0]
        if tempa == tempb:
            heapq.heappop(a)
            heapq.heappop(b)
        if tempa < tempb:
            heapq.heappop(b)
            heapq.heappush(b, -len(str(tempb)))
            res += 1
        if tempa > tempb:
            heapq.heappop(a)
            heapq.heappush(a, -len(str(tempa)))
            res += 1

    print(res)
