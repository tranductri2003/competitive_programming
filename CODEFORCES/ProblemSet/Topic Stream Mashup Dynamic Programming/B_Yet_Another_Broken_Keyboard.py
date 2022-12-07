from collections import defaultdict

check=defaultdict(lambda:-1)
n,k=list(map(int,input().split()))
s=input()
a=input().split()
for i in a:
    check[i]=1


res=0
stack=0
for i in range(n):
    if check[s[i]]==1:
        stack+=1
    else:
        res+=(stack+1)*stack//2
        stack=0
res+=stack*(stack+1)//2
print(res)



