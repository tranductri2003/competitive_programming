n=int(input())
a=list(map(int,input().split()))
a.sort()
res=10**9
for i in range(0,n-1):
    res=min(res,abs(a[i+1]-a[i]))
print(res)

