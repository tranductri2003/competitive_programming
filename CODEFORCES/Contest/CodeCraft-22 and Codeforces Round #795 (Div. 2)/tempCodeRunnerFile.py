t=int(input())
for _ in range(t):
    n,k=list(map(int,input().split()))
    s=input()
    
    tong=0
    for i in range(0,n-1):
        tong+=int(s[i]+s[i+1])
    vitringoai=s.find('1')
    vitritrong=s.rfind('1')

    trai=vitringoai
    phai=n-1-vitritrong

    if k>=phai and k!=0:
        tong-=10
        k-=phai
    if k>=trai and k!=0:
        tong-=1
    
    if s.count('1')==0:
        tong=0
    elif s.count('1')==1:
        tong=max(tong,1)
    else:
        tong=max(tong,11)
    print(tong)
