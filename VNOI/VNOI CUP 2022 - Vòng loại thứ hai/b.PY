


n,m,k=list(map(int,input().split()))

dptrai=[0]*(n*m+1)
dpphai=[0]*(n*m+1)


a=[]
aa=[]
for i in range(n+1):
    a.append([])
    aa.append([])
z=0
for i in range(1,n+1):
    a[i]=list(map(int,input().split()))
    aa[i]=a[i].copy()
    z+=sum(a[i])
    


for i in range(1,n*m+1):
    maxx=-10**9
    for j in range(1,n+1):
        if len(a[j])!=0:
            if a[j][0]>maxx:
                maxx=a[j][0]
                vitri=j
     
    dptrai[i]=dptrai[i-1]+maxx
    a[vitri].pop(0)


dpphai[n*m]=z
for i in range(n*m-1,0,-1):
    minn=10**9
    for j in range(1,n+1):
        if len(aa[j])!=0:
            if aa[j][-1]<minn:
                minn=aa[j][-1]
                vitri=j
     
    dpphai[i]=dpphai[i+1]-minn
    aa[vitri].pop(-1)
 
res=[0]*(n*m+1)
for i in range(1,n*m+1):
    res[i]=max(dpphai[i],dptrai[i])
print(res[k])
    
    
