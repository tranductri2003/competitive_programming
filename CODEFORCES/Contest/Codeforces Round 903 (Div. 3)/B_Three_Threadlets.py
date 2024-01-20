t=int(input())
for _ in range(t):
    a,b,c = list(map(int,input().split()))
    data = []
    data.append(a)
    data.append(b)
    data.append(c)
    data.sort()
    time =0
    while len(set(data))!=1:
        for i in range(len(data)):
            if data[i]!=data[0]:
                temp = data[i]
                data.pop(i)
                data.append(data[0])
                data.append(temp-data[0])
                time+=1
        data.sort()
        if time>3:
            print("NO")
            break
    else:
        print("YES")