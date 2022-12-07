
import bisect

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

c=[]
for i in range(n):
    c.append(a[i]-b[i])
c.sort()
res=0
for i in range(n-1,-1,-1):
    pos=bisect.bisect_left(c,-c[i]+1)
    res+=max(0,i-pos)
print(res)
