n=int(input())

if n==0:
    print(1)
else:
    res=1
    temp=1
    for i in range(1,n+1):
        temp=temp*i
        res=res+1/temp
    print(res)
