import sys
import os
from io import BytesIO, IOBase


input = sys.stdin.readline


N, Q = list(map(int, input().split()))
r = list(map(int, input().split()))
c = list(map(int, input().split()))

checkrow = [0]*(N)

for i in range(1, N):
    if r[i] % 2 == r[i-1] % 2:
        checkrow[i] = checkrow[i-1]
    else:
        checkrow[i] = checkrow[i-1]+1


checkcollumn = [0]*(N)

for i in range(1, N):
    if c[i] % 2 == c[i-1] % 2:
        checkcollumn[i] = checkcollumn[i-1]
    else:
        checkcollumn[i] = checkcollumn[i-1]+1


for _ in range(Q):
    ra, ca, rb, cb = list(map(int, input().split()))
    # ra -= 1
    # ca -= 1
    # rb -= 1
    # cb -= 1

    # hangNho = min(ra, rb)
    # hangLon = max(ra, rb)

    # cotNho = min(ca, cb)
    # cotLon = max(ca, cb)

    # if hangLon-hangNho+1 == checkrow[hangLon]-checkrow[hangNho]+1 and cotLon-cotNho+1 == checkcollumn[cotLon]-checkcollumn[cotNho]+1:
    #     print("YES")
    # else:
    #     print("NO")
    if checkrow[ra-1] == checkrow[rb-1] and checkcollumn[ca-1] == checkcollumn[cb-1]:
        print("YES")
    else:
        print("NO")
