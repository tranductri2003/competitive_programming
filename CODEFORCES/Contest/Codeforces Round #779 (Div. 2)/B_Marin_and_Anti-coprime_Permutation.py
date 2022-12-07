#  beautiful permutation of length n is a permutation that has the following property:
# gcd(1⋅p1,2⋅p2,…,n⋅pn)>1,\

import math
t=int(input())
for _ in range(t):
    n=int(input())
    MOD=998244353
    #Số chẵn thì được còn số lẻ thì không
    if n%2==0:
        res=math.factorial(n//2)**2%MOD
    else:
        res=0
    print(res)
