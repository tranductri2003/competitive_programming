from collections import defaultdict
from math import sqrt, isqrt


# def sqrt(x):

#     left = 0
#     right = 2*10**9
#     while right > left:
#         mid = (left+right)//2
#         if mid**2 == x:
#             return mid
#         elif mid**2 > x:
#             right = mid
#         else:
#             left = mid+1
#     return left-1


t = int(input())
for _ in range(t):
    l, r = list(map(int, input().split()))
    sobatdau = isqrt(l)+1
    soketthuc = isqrt(r)+1

    if sobatdau**2 == l:
        tronbatdau = sobatdau
    else:
        
        

    tronketthuc = soketthuc//1
    res = 0
    res += max(0, (tronketthuc-tronbatdau)*3)
    kiemtra = defaultdict(lambda: 0)
    # print(res)
    if sobatdau % 1 == 0:
        pass
    else:
        d = sobatdau//1
        temp = []
        temp.append(d**2)
        temp.append(d**2+d)
        temp.append(d**2+2*d)
        for num in temp:
            if kiemtra[num] == 0 and l <= num <= r:
                res += 1
                kiemtra[num] = 1

    # print(res)
    if soketthuc % 1 == 0:
        if kiemtra[soketthuc**2] == 0:
            res += 1
    else:
        d = soketthuc//1
        temp = []
        temp.append(d**2)
        temp.append(d**2+d)
        temp.append(d**2+2*d)
        temp.append(d**2+3*d)
        for num in temp:
            if kiemtra[num] == 0 and l <= num <= r:
                res += 1
                kiemtra[num] = 1
    if "." not in str(res):
        print(res)
    else:
        res = res//1
        res = str(res)[:-2]
        print(res)
