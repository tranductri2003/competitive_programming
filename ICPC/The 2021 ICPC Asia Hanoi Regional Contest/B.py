import math
n = int(input())
res = math.comb((n-1), 2)
print(res)
for i in range(2, n+1):
    print(1, i)
