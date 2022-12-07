import math
M=int(input())
a=[]

for i in range(0,M):
    b=int(input())
    if i==0:
        ucln=b
    a.append(b)
    ucln=math.gcd(ucln,b)
limit=int((math.sqrt(ucln)//1+1))

for i in range(2,limit+1):
    if ucln%i==0:
        print(i,end=" ")
        if i!=math.sqrt(ucln) and ucln//i!=1:
            print(ucln//i,end=" ")

a.sort()
limit=a[1]+1

