n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
a.sort()
for i in range(0,n):
    if a[i]==1:
        a[i]=0
        
min=sum(a[0:k])
max=sum(a[n-k:])
print(min,max)