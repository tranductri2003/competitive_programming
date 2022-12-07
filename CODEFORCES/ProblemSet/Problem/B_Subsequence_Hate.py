t=int(input())

for _ in range(t):
    s=input()
    num1=[0]*len(s)
    if s[0]=='1':
        num1[0]=1
    for i in range(1,len(s)):
        if s[i]=='1':
            num1[i]=num1[i-1]+1
        else:
            num1[i]=num1[i-1]
    
    res=10**9
    for i in range(len(s)):
        num1Left=num1[i]
        num0Left=i+1-num1Left
        
        num1Right=num1[-1]-num1Left
        num0Right=len(s)-num1Left-num0Left-num1Right
        
        res=min(res,min(num1Left,num0Left)+min(num1Right,num0Right))
    print(res)
    