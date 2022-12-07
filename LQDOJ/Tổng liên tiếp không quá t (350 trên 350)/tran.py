n,t=list(map(int,input().split()))
a=list(map(int,input().split()))

f=0
j=0
res=1
for i in range (0,n):
    f+=a[i]
    if f>t:
        f-=a[j]
        j+=1
    k=i-j+1
    res=max(k,res)
print(res)

