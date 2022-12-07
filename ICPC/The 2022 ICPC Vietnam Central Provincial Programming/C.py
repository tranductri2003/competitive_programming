import math
n, k = list(map(int, input().split()))
sure = 0
notsure = 0
for _ in range(n):
    l, r = list(map(int, input().split()))
    if l == r:
        sure += 1
    else:
        notsure += 1
res = 0
if sure >= k:
    res += math.comb(sure, k)
if sure >= k-1:
    res += math.comb(sure, k-1)*notsure

print(res)
