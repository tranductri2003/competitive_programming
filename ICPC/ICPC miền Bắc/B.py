n=int(input())
a=list(map(int,input().split()))
a.sort()

i=0
j=n-1

while i<=j:
    if a[i]+a[j]==0:
        i+=1
        j-=1
    elif a[i]+a[j]<0:
        print(-a[i])
        break
    else:
        print(-a[j])
        break
        