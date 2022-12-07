t=int(input())
for _ in range(t):
    s=input()
    s="R"+s+"R"
    data=[]
    for i in range(0,len(s)):
        if s[i]=="R":
            data.append(i)
    res=0
    for i in range(0,len(data)-1):
        res=max(res,data[i+1]-data[i])
    print(res)