n,w=list(map(int,input().split()))


weight=[0]*n
value=[0]*n

for i in range(0,n):
    weight[i],value[i]=list(map(int,input().split()))

check=[0]*(w+1)
check[0]=1

money=[0]*(w+1)
money[0]=0

for i in range(0,n):
    for j in range(w,weight[i]-1,-1):

        if check[j]==0 and check[j-weight[i]]==1:
            check[j]=1
            money[j]=max(money[j],money[j-weight[i]]+value[i])

print(max(money))