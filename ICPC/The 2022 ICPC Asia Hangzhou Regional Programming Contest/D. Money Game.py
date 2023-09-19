n = int(input())
a =list(map(int, input().split()))

each = sum(a)/(n+1)
res=[]
res.append(2*each)
for i in range(n-1):
    res.append(each)
print(*res)