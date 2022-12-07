t=int(input())

for _ in range(t):
    n,B,x,y=list(map(int,input().split()))
    res=0
    temp=0
    for i in range(0,n):
        if temp+x<=B:
            temp+=x
            res+=temp

        else:

            temp-=y
            res+=temp
    print(res)