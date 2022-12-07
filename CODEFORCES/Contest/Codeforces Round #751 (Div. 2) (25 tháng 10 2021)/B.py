

testcase=int(input())

for test in range(testcase):
    n=int(input())
    a=list(map(int,input().split()))

    data=[]
    data.append(a)

    for i in range(n):   #Sẽ lặp tối đa là n bằng độ dài của mảng ban đầu
        distributionCounting=dict()
        for j in range(n):
            if a[j] in distributionCounting:
                distributionCounting[a[j]]+=1
            else:
                distributionCounting[a[j]]=1
        
        b=[]
        for j in range(n):
            b.append(distributionCounting[a[j]])
        
        if b==a:
            data.append(b)
            break
        else:
            data.append(b)
            a=b
    limit=len(data)

    queries=int(input())
    for j in range(queries):
        x,time=list(map(int,input().split()))
        if time>=limit:
            print(data[-1][x-1])
        else:
            print(data[time][x-1])
