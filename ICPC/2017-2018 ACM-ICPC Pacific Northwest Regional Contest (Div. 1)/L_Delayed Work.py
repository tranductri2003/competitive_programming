K,P,X = list(map(int,input().split()))
res=10**9
for i in range(1,100001):
    res = min(res, i*X+(K/i)*P)

print(format(res,".3f"))
    