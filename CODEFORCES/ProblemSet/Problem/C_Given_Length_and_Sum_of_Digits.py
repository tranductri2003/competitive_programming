#length m and sum of digit s


m,s=list(map(int,input().split()))
if s==0:
    if m==1:
        print(0,0)
    else:
        print(-1, -1)
else:
    if s>9*m:
        print(-1, -1)
    else:
        s1=s2=s
        
        res1=[0]*m
        for i in range(0,m):
            res1[i]=max(0,min(9,s1))
            s1-=res1[i]
        
        res2=[0]*m
        for i in range(m-1,-1,-1):
            res2[i] = max(0,min(9,s2))
            s2-=res2[i]
        
        if res2[0]==0:
            for i in range(0,m):
                if res2[i] >0:
                    res2[i] -=1
                    res2[0]+=1
                    break
        
        for i in range(0,m):
            res1[i]=str(res1[i])
            res2[i]=str(res2[i])
        res1="".join(res1)
        res2="".join(res2)
        print(res2,res1)