n,k = list(map(int,input().split()))
data = []

temp=n
while temp!=1:
    for i in range(9,1,-1):
        if temp%i==0:
            data.append(i)
            temp = temp//i
            break
    else:
        data.append(-1)
        break
    
if n==1:
    res = k*'1'
    print(res)
else:
    if data[-1]==-1:
        print(-1)
    else:
        data.sort()
        res=""
        for num in data:
            res+=str(num)
        if len(res)>k:
            print(-1)
        elif len(res)==k:
            print(res)
        else:
            res='1'*(k-len(res))+res
            print(res)