n,k=list(map(int,input().split()))

a=list(map(int,input().split()))

pos=0
for i in range(n-1,-1,-1):
    if a[i]==a[k-1]:
        pos=i
        break
res=0
for i in range(pos+1):
    if a[i]>0:
        res+=1
print(res)
