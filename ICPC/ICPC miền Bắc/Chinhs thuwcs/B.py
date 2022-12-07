N=int(input())
a=list(map(int,input().split()))

a.sort()


i=0
j=N-1
while a[i]+a[j]==0:
    i+=1
    j-=1

if abs(a[j])>abs(a[i]):
    print(-(a[j]))
else:
    print(-a[i])
    
    