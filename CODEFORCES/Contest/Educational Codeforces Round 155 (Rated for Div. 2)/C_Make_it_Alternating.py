
import math

t=int(input())
for _ in range(t):
    s=input()
    n=len(s)
    soCach = 0
    soChuoi = 1
    soChon = 1
    soPhan=0
    for i in range(n-1):
        if s[i]==s[i+1]:
            soCach +=1
    
    distinct=[s[0]]
    current=s[0]
    for i in range(1,n):
        if s[i]==current:
            pass
        else:
            current=s[i]
            distinct.append(current)
    
    
    pointerDistinct =0
    i=0
    temp=0
    data=[]
    while i<n:
        if s[i]==distinct[pointerDistinct]:
            temp+=1
            i+=1
        else:
            soChon *=temp
            soPhan+=temp-1
            pointerDistinct+=1            
            temp=0
    soChon*=temp
    soPhan+=temp-1
    
    
    res=soChon*math.factorial(soPhan)%998244353
    print(soCach,res%998244353)

        