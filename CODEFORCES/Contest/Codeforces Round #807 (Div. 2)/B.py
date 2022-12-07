t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=0
    vitri=0
    for i in range(n-1):
        if a[i]==0:
            vitri+=1
        else:
            break

            
    for i in range(vitri,n-1):
        if a[i]!=0:
            res+=a[i]
        else:
            res+=1
    print(res)