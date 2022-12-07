n=int(input())


a0=0
a1=0
a2=0

for i in range(n):
    a=list(map(int,input().split()))
    a0+=a[0]
    a1+=a[1]
    a2+=a[2]
if a0==0 and a1==0 and a2==0:
    print("YES")
else:
    print("NO")
    