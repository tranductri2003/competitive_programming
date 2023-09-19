t=int(input())
import math
for _ in range(t):
    a,b,c = list(map(int,input().split()))
    res = math.ceil(abs(a-b)/(2*c))
    print(res)