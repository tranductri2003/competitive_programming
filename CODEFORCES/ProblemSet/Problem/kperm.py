n,k=list(map(int,input().split()))
res=[]
for i in range(1,n-k-1 +1):
    res.append(i)

if res==[]:
    i=1
else:
    
    i=res[-1]+1
j=n
while i<=j:
    if i==j:
        res.append(i)
    else:
        res.append(i)
        res.append(j)
    i+=1
    j-=1
print(*res)
