t=int(input())
for _ in range(t):
    n=int(input())
    a = list(map(int,input().split()))
    if n==1:
        print("NO")
    else:
        a.sort(reverse=True)
        temp=0
        for i in range(n-1):
            if a[i]>1:
                temp+=a[i]-1
            else:
                temp-=1
        b=a[-1]
        a[-1]+=temp
        if a[-1]==b or a[-1]<=0:
            print("NO")
        else:
            print("YES")
            
                
        