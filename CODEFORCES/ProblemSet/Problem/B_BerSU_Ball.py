n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

a.sort()
b.sort()
i=0
j=0

res=0
while True:
    if abs(a[i]-b[j])<=1:
        res+=1
        i+=1
        j+=1
    else:
        if a[i]<b[j]:
            i+=1
        else:
            j+=1
    
    if i==n or j==m:
        break
print(res)
        