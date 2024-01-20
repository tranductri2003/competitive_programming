from collections import defaultdict 
import math


def recur(n):
    if count[n]!=0:
        return count[n]
    if n==1:
        return 1
    for i in range(len(data)-1, -1, -1):
        if n%data[i]==0:
            print(data[i], n//data[i])
            if count[n//data[i]]!=0:
                if data[i]==n//data[i]:
                    temp = count[data[i]]
                    return ((temp+1)*temp//2)
            else:
                return count[data[i]]*recur(n//data[i])
    else:
        return 0
    

            
data = [1,1]
for i in range(82):
    data.append(data[-1]+data[-2])
data = data[2:]
count = defaultdict(lambda: 0)
check = defaultdict(lambda:False)

for num in data:
    check[num] = True
    count[num]+=1

for i in range(len(data)):
    ini = data[i]
    temp =data[i]
    for j in range(60):
        for k in range(i):
            if temp%data[k]==0:
                temp//=data[k]
                break
        if temp==1:
            count[ini]+=1
            break
count[1]=1
print(recur(512))
for _ in range(int(input())):
    n = int(input())
    gone = defaultdict(lambda: False)
    res=0
    # print("Input", n, end=" ")
    if count[n]!=0:
        print(count[n])
    else:
        canBacHai = int(math.sqrt(n))
        for i in range(len(data)-1,-1,-1):
            if data[i]<=canBacHai and n%data[i]==0:
                temp1 = recur(data[i])
                temp2 = recur(n//data[i])
                tempRes=0
                print(data[i], n//data[i])
                print(temp1, temp2)
                if temp1==temp2:
                    tempRes=((temp1+1)*temp1//2)
                else:
                    tempRes=(temp1*temp2)
                if tempRes==0:
                    pass
                else:
                    res+=tempRes
                    print(res)
                    break
        else:
            print(0)