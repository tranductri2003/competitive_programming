t=int(input())

for _ in range(t):
    n,s=list(map(int,input().split()))
    a=list(map(int,input().split()))
    
    
    tongcanxoa=sum(a)-s
    if tongcanxoa==0:
        print(0)
    elif tongcanxoa<0:
        print(-1)
    else:
        vitriso1=[0]
        for i in range(0,n):
            if a[i]==1:
                vitriso1.append(i+1)

        vitriso1.append(n+1)
        maxn=0
        for i in range(1,10**9):
            if i+s>=len(vitriso1):
                break
            
            maxn=max(maxn,vitriso1[i+s]-vitriso1[i-1]-1)

        print(n-maxn)
        
