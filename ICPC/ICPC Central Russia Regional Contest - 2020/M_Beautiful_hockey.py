import math

n=int(input())
res=0
for i in range(0,n+1,2):
    res+=(math.comb(n,i)*math.comb(i,i//2)*2**(n-i))
print(((4**n-res)//2)%(10**9+7))
    