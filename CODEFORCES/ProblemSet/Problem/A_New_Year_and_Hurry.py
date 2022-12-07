n,k=list(map(int,input().split()))
rest=4*60-k
res=0
for i in range(1,n+1):
    if rest>=(res+1)*5:
        rest-=(res+1)*5
        res+=1
    else:
        break
print(res)