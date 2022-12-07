
t=int(input())
for _ in range(t):
    n=int(input())
    if n==1:
        print(1)
    else:
        ans=[i for i in range(1,n+1)]
        for i in range(n-1,0,-2):
            ans[i],ans[i-1]=ans[i-1],ans[i]
        print(*ans)