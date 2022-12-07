from random import randint


t=int(input())
for _ in range(t):
    # n=int(input())
    n=randint(1,100)
    print(n)
    res=0
    
    maxRight=-10**9
    maxLeft=10**9
    maxUp=-10**9
    maxDown=10**9
    for i in range(n):
        # x,y=list(map(int,input().split()))
        if i%4==0:
            x=0
            y=randint(-10**5,10**5)
        if i%4==1:
            x=0
            y=randint(-10**5,10**5)
        if i%4==2:
            y=0
            x=randint(-10**5,10**5)
        if i%4==3:
            y=0
            x=randint(-10**5,10**5)

        if x>=0:
            maxRight=max(maxRight,x)
        else:
            maxLeft=min(maxLeft,x)
        if y>=0:
            maxUp=max(maxUp,y)
        else:
            maxDown=min(maxDown,y)
    res+=abs(maxRight)+abs(maxRight)+abs(maxUp)+abs(maxUp)+abs(maxLeft)+abs(maxLeft)+abs(maxDown)+abs(maxDown)
    print(res)
    
        
    # print(((maxRight-maxLeft) + (maxUp-maxDown))*2)