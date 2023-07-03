def differ(s1,s2):
    res=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            res+=1
    return res
for _ in range(int(input())):
    N=int(input())
    so=[]
    for i in range(N):
        so.append(int(input()))

    data=[]
    for num in so:
        data.append(bin(num)[2:])
    dodailonnhat=0
    for i in data:
        dodailonnhat =max(dodailonnhat,len(i))
    for i in range(len(data)):
        data[i]='0'*(dodailonnhat-len(data[i]))+data[i]
    res=0
    for i in range(0,len(data)-1):
        for j in range(i+1,len(data)):
            res=max(res,differ(data[i],data[j]))
    print(res)
