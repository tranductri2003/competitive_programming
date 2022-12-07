

t=int(input())
for _ in range(t):
    n=int(input())
    w=list(map(int,input().split()))
    # w.insert(0,0)
    # l=0
    # r=n+1
    # left=0
    # right=0
    # res=0
    # while l<r:
    #     if left==right:
    #         res=l-0+n+1-r
        
    #     if left<=right:
    #         l+=1
    #         left+=w[l]
    #     else:
    #         r-=1
    #         right+=w[r]
    # print(res)
    l,r,=0,n-1
    left=w[l]
    right=w[r]
    res=0
    while l<r:
        if left==right:
            res=l-0+1+n-r
        if left<=right:
            l+=1
            left+=w[l]
        else:
            r-=1
            right+=w[r]
    print(res)