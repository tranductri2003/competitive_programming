
import math
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(math.comb((10-n), 2)*6)
