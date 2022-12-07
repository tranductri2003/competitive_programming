n,m,d=list(map(int,input().split()))

from collections import defaultdict
data=defaultdict(lambda:0)
for i in range(n):
    a=tuple(map(int,input().split()))
        
    data[(a)]=1

check=[]
for i in range(m):
    a=tuple(map(int,input().split()))

    if data[(a)]==0:
        print("GOOD") 
    else:
        print("BAD")

