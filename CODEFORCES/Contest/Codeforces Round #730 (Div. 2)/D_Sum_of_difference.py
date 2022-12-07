n=int(input())
a=list(map(int,input().split()))

a.sort()
prefixSum=[]
temp=0
for num in a:
    temp+=num
    prefixSum.append(temp)


res=0
for i in range(0,n):
    res+=(prefixSum[n-1]-prefixSum[i])-a[i]*(n-1-i)
print(res)