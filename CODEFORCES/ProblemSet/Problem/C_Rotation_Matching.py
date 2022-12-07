n=int(input())

a=list(map(int,input().split()))
b=list(map(int,input().split()))


indexA=[0]*(n+1)
indexB=[0]*(n+1)
indexC=[0]*(n+1)

for i in range(n):
    indexA[a[i]]=i+1
    indexB[b[i]]=i+1
res=[0]*(n+1)

for i in range(1,n+1):
    if indexB[i]>=indexA[i]:
        indexC[i]=indexB[i]-indexA[i]
    else:
        indexC[i]=indexB[i]+n-indexA[i]
        
    res[indexC[i]]+=1


ans=max(res)
print(ans)