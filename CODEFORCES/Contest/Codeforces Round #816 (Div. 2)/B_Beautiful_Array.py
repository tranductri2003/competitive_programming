
t=int(input())
for _ in range(t):
    n,k,b,s=list(map(int,input().split()))
    gioihantren=(b+1)*k-1
    gioihanduoi=b*k

    
    
    if k==1:
        if s!=b:
            print(-1)
        else:
            res=[s]+[0]*(n-1)
            print(*res)
    else:
        if gioihanduoi<=s<=gioihantren:
            res=[0]*(n-1)
            res.append(s)
            print(*res)
        elif s>gioihantren:
            res=[gioihantren]
            conlai=s-gioihantren
                
            time=conlai//((k-1))
            rest=conlai-time*(k-1)
        
            if time+1>n :
                print(-1)
            else:
                for i in range(time):
                    res.append(k-1)
                
                if sum(res)==s:
                    for i in range(n-len(res)):
                        res.append(0)
                else:
                    res.append(conlai-time*(k-1))
                    for i in range(n-len(res)):
                        res.append(0)
                
                if len(res)==n:
                    print(*res)
                else:
                    print(-1)
        else:
            print(-1)
            
        
        