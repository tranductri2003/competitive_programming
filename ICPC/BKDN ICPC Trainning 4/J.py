
import math

def div(x):
    ans=[]
    for i in range(1,math.floor(math.sqrt(x))+1):
        if x%i==0:
            ans.append(i)
            if x//i!=i:
                ans.append(x//i)
    
    return ans


            
t=int(input())
for _ in range(t):
    w,l=list(map(int,input().split()))
    res=[]
    
    # x=max(w-1,l-2,l)
    # res.append(math.gcd(w-1,l-2,l))
    
    # x=max(w,w-2,l-1)
    # res.append(math.gcd(w,w-2,l-1))
    
    #! Điều kiện này không cần vì chỉ có thể là a=2
    

    res.append(math.gcd(w,l-2))
    
    
    res.append(math.gcd(w-2,l))
            
    res.append(math.gcd(w-1,l-1))
    
    
    ans=[]
    for num in res:
        ans+=div(num)

    ans.append(2)
    ans=list(set(ans))
    ans.sort()
    print(len(ans),end=" ")
    print(*ans)
            