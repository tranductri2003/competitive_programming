import math
n=int(input())

a=list(map(int,input().split()))
b=a[0]
multi=1
for num in a:
    multi*=num%(10**9+7)
    b=math.gcd(b,num)

print(pow(multi,b,10**9+7))