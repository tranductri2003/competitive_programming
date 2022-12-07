def tohop(n,k):
    if k==0 or k==n:
        return 1
    else:
        return tohop(n-1,k-1)+tohop(n-1,k)

a,b=list(map(int,input().split()))
print(tohop(a,b))