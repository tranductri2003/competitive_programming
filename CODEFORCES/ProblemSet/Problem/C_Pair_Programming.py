testcase=int(input())
for test in range(testcase):
    space=input()
    k,n,m=list(map(int,input().split()))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    res=[]
    i=0
    j=0
    current=k
    check=True
    while i<n and j<m:
        if a[i]==0 or b[j]==0:
            if a[i]==0:
                res.append(0)
                i+=1
                current+=1
            else:
                res.append(0)
                j+=1
                current+=1
        else:
            if current>=a[i]:
                res.append(a[i])
                i+=1
            else:
                if current>=b[j]:
                    res.append(b[j])
                    j+=1
                else:
                    check=False
                    break

        if check==True:
            if i==n:
                for k in range(j,m):
                    if b[k]==0:
                        res.append(0)
                        current+=1
                    else:
                        if current>=b[k]:
                            res.append(b[k])
                        else:
                            check=False
                            break
            if j==m:
                for k in range(i,n):
                    
                    if a[k]==0:
                        res.append(0)
                        current+=1
                    else:
                        if current>=a[k]:
                            res.append(a[k])
                        else:
                            check=False
                            break

    if check==False:
        print(-1)
    else:
        print(*res)