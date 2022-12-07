import math
n,m,a,b=list(map(int,input().split()))

res=min(n*a,   math.ceil(n/m)*b   ,n//m*b +max(0,(n-n//m*m)*a)   ,max(0,(n-m))*a+b)
print(res)