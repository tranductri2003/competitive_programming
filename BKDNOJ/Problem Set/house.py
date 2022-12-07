#https://bkdnoj.dut.udn.vn/public/practice_problem.php?id=FC51_HOUSE

N=int(input())
a=list(map(int,input().split()))

res=0


res=-10**9
mangmin=[0]*(N)
minn=min(a)
for i in range(N-1):
    if a[i]!=minn:
        mangmin[i]=minn
    else:
        mangmin[i]=minn
        minn=min(a[i+1:])
mangmin[N-1]=a[N-1]
    
for i in range(N):
    if a[i]-mangmin[i]>0:
        res=max(res,a[i]-mangmin[i])
if res<0:
    print("Lo nang roi!")
else:
    print(res)