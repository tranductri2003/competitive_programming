
import math
def compare(s1,s2):
    res=0
    for i in range(len(s1)):
        res+=abs(ord(s1[i])-ord(s2[i]))
    return res
t=int(input())
for _ in range(t):
    n,m=list(map(int,input().split()))
    data=[]
    for i in range(n):
        data.append(input())
    data.sort()
    
    res=10**9
    for i in range(n-1):
        for j in range(i+1,n):
            res=min(res,compare(data[i],data[j]))
    print(res)
    