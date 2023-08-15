import math
n, X, v = list(map(float,input().split()))

sGio=0
for i in range(int(n)):
    l,r,vi = list(map(float,input().split()))
    sGio+=(r-l)*vi

vanTocY = sGio/X
if abs(vanTocY)>abs(v):
    print("Too hard")
else:
    realVanToc = math.sqrt(v**2-vanTocY**2)
    res=format(X/realVanToc,".3f")
    print(res)
