N=int(input())
res=0
for i in range(N):
    s=input()
    so1=int(s[:-1])
    so2=int(s[-1])
    res+=so1**so2
print(res)