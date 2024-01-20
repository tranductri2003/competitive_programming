import math
n = int(input())
res = 1+n*(n-3)//2 +math.comb(n,4)

print(res% 987654321)

