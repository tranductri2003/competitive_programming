t=int(input())
for _ in range(t):
    n,MEX,k = list(map(int,input().split()))
    if MEX>n or k<MEX-1:
        print(-1)
    else:
        data=[]
        have=0
        for i in range(0,MEX):
            data.append(i)
            have+=1
        while have<n:
            if k==MEX:
                data.append(k-1)
                have+=1
            else:
                data.append(k)
                have+=1
        print(sum(data))
            