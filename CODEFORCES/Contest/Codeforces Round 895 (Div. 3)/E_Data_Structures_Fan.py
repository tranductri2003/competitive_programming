t=int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    s=input()
    data=[a[0]]
    so0=[]
    so1=[]
    
    temp=a[0]
    for i in range(1,n):
        temp^=a[i]
        data.append(temp)
    



    for i in range(n):
        if s[i]=='0':
            so0.append(i)        
        else:
            so1.append(i)
            
    temp=a[0]
    for i in so1:
        temp^=a[i]
        data.append(temp)
    
    q = int(input())
    for i in range(q):
        temp = input().split()
        if temp[0]=="1":
            l,r = int(temp[1]), int(temp[2])
        else:
            g = int(temp[1])
        