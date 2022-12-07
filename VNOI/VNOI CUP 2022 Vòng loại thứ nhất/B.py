
import math


n=int(input())
a=list(map(int,input().split()))

thoigianchamdat=[]
for i in range(n-1):
    for j in range(i+1,n):
        thoigianchamdat.append(math.gcd(a[i],a[j]))
        

for nguoiNhay in a:
    res=0
    for dayNhay in thoigianchamdat:
        if dayNhay%nguoiNhay==0:
            tmp=dayNhay//nguoiNhay
            if tmp%2==0:
                res+=1
    print(res,end =" ")