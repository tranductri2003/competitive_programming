import math
goc = 34
radian = math.radians(goc)
h,d = list(map(int,input().split()))
R = d*h/(2*h+d*math.tan(radian))

h1 = R*math.tan(radian)
h2 = h-h1





V1 = 1/3 * math.pi * R**2 * h1
V2 = 1/3 * math.pi * R**2 * h2
print(V1+V2)
