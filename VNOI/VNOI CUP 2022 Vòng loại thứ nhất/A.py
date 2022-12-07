n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

i=0
j=0

c=[-10**9]
tmp=0
res=[]
while tmp<2*n:
    if i==n:
        c+=b[j:]
        for i in range(j,n):
            res.append('b')
        break
    elif j==n:
        c+=a[i:]
        for i in range(i,n):
            res.append('a')
        break
    else:
        if i!=n-1:
            if a[i]!=c[-1] and (a[i+1]!=a[i] or b[j]!=a[i]):
                c.append(a[i])
                res.append('a')
                i+=1
                tmp+=1
            else:
                c.append(b[j])
                res.append('b')
                j+=1
                tmp+=1
        else:
            if a[i]!=c[-1] and (b[j]!=a[i]):
                c.append(a[i])
                res.append('a')
                i+=1
                tmp+=1
            else:
                c.append(b[j])
                res.append('b')
                j+=1
                tmp+=1

for i in res:
    print(i, end="")