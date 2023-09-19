from collections import defaultdict 


N,M = list(map(int,input().split()))
check = defaultdict(lambda: defaultdict(lambda :0))
data=[]
for _ in range(N):
    temp = input()
    data.append(temp)
    for i in range(M):
        check[i][temp[i]]+=1

res=[0]*M

for i in range(M):
    maxx = max(check[i].values())
    for num in check[i]:
        if check[i][num]==maxx:
            res[i]=num

ans=0
for _ in range(N):
    for i in range(M):
        if data[_][i]!=res[i]:
            ans+=1

print(ans)
