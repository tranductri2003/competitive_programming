# The first line of the input will contain three integers n,k,m (1≤n,k≤500000, 0≤m≤250000, n⋅k≤500000),
# the number of jobs in the system, the number of runs Mike had triggered, and the number of dependencies.

# The following m lines will contain a pair ai,bi (1≤ai,bi≤n,ai≠bi, for all 1≤i≤m) 
# describing a dependency of kind: "job ai must be executed before job bi".

# Finally, the last line of the input contains n⋅k integers ci (1≤ci≤n, for all 1≤i≤n⋅k),
# the job ids that have been printed in the log file, in order.

from collections import defaultdict


n,k,m=list(map(int,input().split()))
for i in range(m):
    a,b=list(map(int,input().split()))

count=defaultdict(lambda:0)

res=[]
a=list(map(int,input().split())) 
for j in range(n*k):
    temp=a[j]
    count[temp]+=1
    res.append(count[temp])
print(*res)

