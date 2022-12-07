n=int(input())

res=0
for i in range(n):
    a=list(map(int,input().split()))
    if a.count(1)>=2:
        res+=1
print(res)