import math
n=int(input())
do=[]
vang=[]
res=0

for i in range(0,n+1,2):
    for j in range(0,n+1,3):
        res+=math.comb(n,i)*math.comb(n-i,j)
        res=res%(10**9+7)
print(res)
