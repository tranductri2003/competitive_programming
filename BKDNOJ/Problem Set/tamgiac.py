n=int(input())

a=[]
for i in range(n):
    j=int(input())
    a.append(j)

c=0
res=0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if a[i]+a[j]>a[k] and a[i]+a[k]>a[j] and a[j]+a[k]>a[i]:
                c=a[i]+a[j]+a[k]
                res=max(res,c)

print(res)