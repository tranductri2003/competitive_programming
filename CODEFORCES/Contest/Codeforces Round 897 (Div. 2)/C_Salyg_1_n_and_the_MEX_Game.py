t=int(input())

from collections import defaultdict 

for _ in range(t):
    n = int(input())
    s = list(map(int,input().split()))
    check = defaultdict(lambda:-1)
    
    maxNum=s[0]
    for num in s:
        maxNum = max(maxNum,num)
        check[num] =1

    for i in range(maxNum+2):
        if check[i]==-1:
            mex = i
            break

    print(i)
    
    while True:
        temp = int(input())
        if temp==-1:
            break
        else:
            print(temp)

    