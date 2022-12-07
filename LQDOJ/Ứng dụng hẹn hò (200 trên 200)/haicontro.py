nu,nam,k=list(map(int,input().split()))
chuoinu=list(map(int,input().split()))
chuoinam=list(map(int,input().split()))


chuoinu.sort()
chuoinam.sort()

i=0
j=0
ans=0
while i<nu and j<nam:
    if -k<=chuoinu[i]-chuoinam[j]<=k:
        ans+=1
        i+=1
        j+=1
    else:
        if chuoinu[i]>chuoinam[j]:
            j=j+1
        else:
            i=i+1

print(ans)