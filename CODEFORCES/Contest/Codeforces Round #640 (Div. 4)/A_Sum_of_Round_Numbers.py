t=int(input())

for _ in range(t):
    n=str(input())
    
    res=0
    for i in range(0,len(str(n))):
        if n[i]!="0":
            res+=1
    print(res)
    for i in range(0,len(str(n))):
        if n[i]!="0":
            print(n[i]+"0"*(len(str(n))-i-1),end=' ')
    print()
    