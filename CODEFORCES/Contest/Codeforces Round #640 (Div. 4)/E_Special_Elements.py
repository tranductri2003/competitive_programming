t=int(input())
for _ in range(t):
    n=int(input())
    
    a=list(map(int,input().split()))
    
    
    check={}
    res=0

    for num in a:
        if num not in check:
            check[num]=1
        else:
            check[num]+=1
    for i in range(n):
        temp=a[i]
        for j in range(i+1,n):
            temp+=a[j]
            if temp in check:
                res+=check[temp]        
                check[temp]=0
    print(res)
