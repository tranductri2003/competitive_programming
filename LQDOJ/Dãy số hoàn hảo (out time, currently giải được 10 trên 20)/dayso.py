
n,k=list(map(int,input().split()))

chuoi=list(map(int,input().split()))
i=0
j=1
lengthmax=0
while j<n:
    length=len(set(chuoi[i:j+1]))
    if length<=k:
        if length>lengthmax:
            lengthmax=length
            l=i+1
            r=j+1
        j=j+1

    else:
        i=i+1

print(str(l)+str(" ")+str(r))
