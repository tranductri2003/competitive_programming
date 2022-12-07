t=int(input())
for _ in range(t):
    n,m,k=list(map(int,input().split()))
    s1=list(input())
    s1.sort()
    s2=list(input())
    s2.sort()
    
    contro1=0
    contro2=0

    stack1=0
    stack2=0
    res=[]
    while contro1<=n and contro2<=m:
        if stack1>=k:
            res.append(s2[contro2])
            stack1=0
            stack2+=1
            contro2+=1
        elif stack2>=k:
            res.append(s1[contro1])
            stack2=0
            stack1+=1
            contro1+=1
        else:
            if s1[contro1]<=s2[contro2]:
                res.append(s1[contro1])
                contro1+=1
                stack1+=1
                stack2=0
            else:
                res.append(s2[contro2])
                contro2+=1
                stack2+=1
                stack1=0
        if contro1==n or contro2==m:
            break
    res="".join(res)
    print(res)
        
        
        
        