r,x1,y1,x2,y2=list(map(int,input().split()))

import math

res=math.ceil(math.sqrt(abs(x2-x1)**2+abs(y2-y1)**2)/(2*r))
print(res)
