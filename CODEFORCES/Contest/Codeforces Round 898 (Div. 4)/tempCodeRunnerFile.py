t=int(input())
for _ in range(t):
    s = input()
    n=len(s)
    res=0
    i=0
    while i<n:
        if s[i]=="A":
            temp=0
            while i<n and s[i]!="B":
                temp+=1
                i+=1
            if i==n:
                break
            else:
                res+=temp
                i+=1
        else:
            if i==n-1:
                break
            else:
                i+=1
                while i<n and s[i]=="A":
                    res+=1
                    i+=1
    print(res)
                
                
                    