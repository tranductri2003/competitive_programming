from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    check=Counter(a)
    data=list(check.values())
    for i in range(len(data)):
        data[i]-=1
    if sum(data)%2==1:
        print(n-sum(data)-1)
    else:
        print(n-sum(data))