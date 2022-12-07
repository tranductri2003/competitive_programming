t=int(input())
for _ in range(t):
    n=int(input())
    res=0
    
    maxRight=0
    maxLeft=0
    maxUp=0
    maxDown=0
    for i in range(n):
        x,y=list(map(int,input().split()))
        if x>=0:
            maxRight=max(maxRight,x)
        else:
            maxLeft=min(maxLeft,x)
        if y>=0:
            maxUp=max(maxUp,y)
        else:
            maxDown=min(maxDown,y)
    res+=abs(maxLeft)+abs(maxDown)+maxUp+maxRight

    print(2*res)
    
        
    # print(((maxRight-maxLeft) + (maxUp-maxDown))*2)