

#Dạng 1 tìm p,q biết số thứ tự
#Dạng 2 tìm số thứ tự biết p,q

def solve1(n):
    t=n

    a=1
    b=1
    temp=1
    data=[]
    while n>=1:
        data.append(n)
        n//=2
    data=data[::-1]
    a=1
    b=1
    for i in range(1,len(data)):
        if data[i]==data[i-1]*2:
            a=a
            b=a+b
        else:
            a=a+b
            b=b
    return (a,b)

def solve2(p,q):
    if p==1 and q==1:
        return 1
    else:
        if p<q:
            return solve2(p,q-p)*2
        else:
            return solve2(p-q,q)*2+1
            
t=int(input())
for _ in range(t):
    a=list(map(int,input().split()))
    if a[0]==1:
        a,b=solve1(a[1])
        print(a,b)
    else:
        n=solve2(a[1],a[2])
        print(n)