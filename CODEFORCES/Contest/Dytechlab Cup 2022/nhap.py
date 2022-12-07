import math


def sqrt(x):

    left = 0
    right = 2*10**9
    while right > left:
        mid = (left+right)//2
        if mid**2 == x:
            return mid
        elif mid**2 > x:
            right = mid
        else:
            left = mid+1
    return left-1


n = int(input())
print(math.sqrt(n))
print(sqrt(int(n)))
print(math.isqrt(n))
