import math
from collections import defaultdict
t = int(input())
for _ in range(t):
    l, r = list(map(int, input().split()))
    res = 0
    left = math.sqrt(l)
    if left % 1 == 0:
        right = math.sqrt(r)
        if right % 1 == 0:
            res = (right-left)*3+1
        else:
            res = (right//1-left)*3
            right //= 1
            if l <= right**2 <= r:
                res += 1
            if l <= right**2+right <= r:
                res += 1
            if l <= right**2+2*right <= r:
                res += 1
            if l <= right**2+3*right <= r:
                res += 1
    else:
        left = left//1+1
        right = math.sqrt(r)
        if right % 1 == 0:
            res = max(0, (right-left)*3+1)
            left -= 1
            if l <= left**2 <= r:
                res += 1
            if l <= left**2+left <= r:
                res += 1
            if l <= left**2+2*left <= r:
                res += 1
            if l <= left**2+3*left <= r:
                res += 1
        else:
            res = max(0, (right//1-left)*3+1)
            left -= 1
            if l <= left**2 <= r:
                res += 1
            if l <= left**2+left <= r:
                res += 1
            if l <= left**2+2*left <= r:
                res += 1
            if l <= left**2+3*left <= r:
                res += 1
            right //= 1
            if l <= right**2 <= r:
                res += 1
            if l <= right**2+right <= r:
                res += 1
            if l <= right**2+2*right <= r:
                res += 1
            if l <= right**2+3*right <= r:
                res += 1
    if "." not in str(res):
        print(res)
    else:
        res = res//1
        res = str(res)[:-2]
        print(res)
