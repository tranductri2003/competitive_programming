# ai equals 0, if on the i-th day of vacations the gym is closed and the contest is not carried out;
# ai equals 1, if on the i-th day of vacations the gym is closed, but the contest is carried out;
# ai equals 2, if on the i-th day of vacations the gym is open and the contest is not carried out;
# ai equals 3, if on the i-th day of vacations the gym is open and the contest is carried out.




n=int(input())
a=list(map(int,input().split()))

res=0

current=a[0]
if current!=3:
    if current==0:
        res+=1
    for i in range(1,n):
        if current==0:
            if a[i]==0:
                res+=1
                current=-1
            elif a[i]==1:
                current=1
            elif a[i]==2:
                current=2
            else:
                current=-1
        elif current==1:
            if a[i]==0:
                res+=1
                current=-1
            elif a[i]==1:
                res+=1
                current=-1
            elif a[i]==2:
                current=2
            else:
                current=2
        elif current==2:
            if a[i]==0:
                res+=1
                current=-1
            elif a[i]==1:
                current=1
            elif a[i]==2:
                res+=1
                current=-1
            else:
                current=1
        else:
            if a[i]==0:
                res+=1
                current=-1
            elif a[i]==1:
                current=1
            elif a[i]==2:
                current=2
            else:
                current=-1
else:
    current=1
    res1=0
    for i in range(1,n):
        if current==0:
            if a[i]==0:
                res1+=1
                current=-1
            elif a[i]==1:
                current=1
            elif a[i]==2:
                current=2
            else:
                current=-1
        elif current==1:
            if a[i]==0:
                res1+=1
                current=-1
            elif a[i]==1:
                res1+=1
                current=-1
            elif a[i]==2:
                current=2
            else:
                current=2
        elif current==2:
            if a[i]==0:
                res1+=1
                current=-1
            elif a[i]==1:
                current=1
            elif a[i]==2:
                res1+=1
                current=-1
            else:
                current=1
        else:
            if a[i]==0:
                res1+=1
                current=-1
            elif a[i]==1:
                current=1
            elif a[i]==2:
                current=2
            else:
                current=-1


    current=2
    res2=0
    for i in range(1,n):
        if current==0:
            if a[i]==0:
                res2+=1
                current=-1
            elif a[i]==1:
                current=1
            elif a[i]==2:
                current=2
            else:
                current=-1
        elif current==1:
            if a[i]==0:
                res2+=1
                current=-1
            elif a[i]==1:
                res2+=1
                current=-1
            elif a[i]==2:
                current=2
            else:
                current=2
        elif current==2:
            if a[i]==0:
                res2+=1
                current=-1
            elif a[i]==1:
                current=1
            elif a[i]==2:
                res2+=1
                current=-1
            else:
                current=1
        else:
            if a[i]==0:
                res2+=1
                current=-1
            elif a[i]==1:
                current=1
            elif a[i]==2:
                current=2
            else:
                current=-1
    res=min(res1,res2)
print(res)