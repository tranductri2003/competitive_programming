t=int(input())
for _ in range(t):
    s=int(input())
    
    res=[]
    temp=9
    while s>0:
        res.insert(0,min(temp,s))
        s-=temp
        temp-=1
    ans=""
    for num in res:
        ans+=str(num)
    print(ans)

