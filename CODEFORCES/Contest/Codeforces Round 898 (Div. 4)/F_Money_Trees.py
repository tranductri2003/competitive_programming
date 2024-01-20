def check(n, k, a):
    start = finish = current_sum = output = 0

    while finish < n:
        current_sum += a[finish]
        finish += 1
        while current_sum > k:
            current_sum -= a[start]
            start += 1
        if output < finish - start:
            output = finish - start
    return output
import random

for _ in range(int(input())):
    # n, k = map(int, input().split())
    # a = list(map(int, input().split()))
    # h = list(map(int, input().split()))
    n = random.randint(1,10)
    k = random.randint(1,20)
    a=[]
    h=[]
    for i in range(n):
        a.append(random.randint(1,5))
        h.append(random.randint(1,5))
    
    print(n,k)
    print(a)
    print(h)
    i = 0
    data=[]
    while i < n:
        lenn=1
        temp=[]
        temp.append(a[i])
    
        if i==n-1:
            break
        elif h[i]%h[i+1]==0:
            while h[i]%h[i+1]==0:
                temp.append(a[i+1])
                i+=1
                lenn+=1
                if i>=n-1:
                    break
        i+=1
        data.append(check(lenn,k,temp))
    if data==[]:
        print(0)
    else:
        print(max(data))
            



