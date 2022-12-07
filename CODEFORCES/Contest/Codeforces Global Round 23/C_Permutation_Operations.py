for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    l = []
    for i in range(1,n):
        if a[i]<a[i-1]:
            l.append([a[i-1]-a[i],i])
    l.sort()
    ans = [1 for i in range(n)]
    t = 1
    for i,j in l:
        while i>0:
            ans[t-1]=j+1
            i-=t
            t+=1
    print(*ans)