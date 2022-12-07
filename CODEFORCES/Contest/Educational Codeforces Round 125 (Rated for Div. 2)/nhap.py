t=int(input())

import math
for _ in range(t):
    x,y=list(map(int,input().split()))
    if x==0 and y==0:
        print(0)
    elif math.sqrt(x**2+y**2)%1==0:
        print(1)
    else:
        print(2)