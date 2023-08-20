t=int(input())
for _ in range(t):
    s = input()
    n=len(s)
    if s=="()":
        print("NO")
    else:
        print("YES")
        data=[]
        i=0
        while i<n:
            start = s[i]
            while i<n and s[i]==start:
                i+=1
            data.append(start)
        if len(data)==1:
            res=""
            for i in range(n):
                res+="()"
        elif len(data)==2:
            if data==['(',')']:
                res=""
                for i in range(n):
                    res+='()'
            else:
                res="("*n+")"*n
        else:
            res=""
            res="("*n+")"*n
        print(res)