
n,c=list(map(int,input().split()))
a=[0]*(c+1)
res=0
def tohop(i):
    global res
    for v in range(a[i-1]+1,n-c+i+1):
        a[i]=v
        if i==c:
            print(*a[1:c+1])
            res+=1
        else:
            tohop(i+1)

tohop(1)

print(res)
