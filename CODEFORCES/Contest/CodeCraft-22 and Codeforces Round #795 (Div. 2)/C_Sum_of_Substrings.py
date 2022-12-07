def tinh(s,n):
    tong=0
    for i in range(0,n-1):
        tong+=int(s[i]+s[i+1])
    return tong
t=int(input())
for _ in range(t):
    n,k=list(map(int,input().split()))
    s=input()
    
    temp=list(s)
    
    vitringoai=s.find('1')
    vitritrong=s.rfind('1')

    trai=vitringoai
    phai=n-1-vitritrong

    soluong1=s.count('1')
    if soluong1==0:
        print(0)
    elif n==1:
        if n-vitringoai-1<=k:
            temp[vitringoai]='0'
            temp[n-1]='1'
        else:
            if vitringoai<=k:
                temp[vitringoai]='0'
                temp[0]='1'
    else:
        if n-1-vitritrong<=k:
            temp[vitritrong]='0'
            temp[n-1]='1'
            k-=(n-vitritrong-1)
        if vitringoai<=k:
            temp[vitringoai]='0'
            temp[0]='1'
        m="".join(temp)
    print(tinh(m,n))
    
        

