

n,k=list(map(int,input().split()))
a=list(map(int,input().split())) 
t=list(map(int,input().split()))

for i in range(k-1):
    a.append(0)
    t.append(0)

tinh=[0]
temp=0
for num in a:
    temp+=num
    tinh.append(temp)

ngu=[0]
temp=0
for i in range(n+k-1):
    if t[i]==1:
        temp+=a[i]
    ngu.append(temp)

res=0
for i in range(n):
    res=max(res,ngu[i]-ngu[0]+tinh[i+k]-tinh[i]+ngu[-1]-ngu[i+k])
print(res)