
t=int(input())
for _ in range(t):
    s=list(input())
    n=len(s)
    pos=-1
    for i in range(n):
        if int(s[i])>=5:
            pos=i
            break
    if pos==-1:
        print("".join(s))
    else:
        for i in range(pos,-1,-1):
            if i==0:
                if int(s[i])>=5:
                    res=['1']+['0']*n
                    break
                else:
                    res=s[:i+1]+['0']*(n-i-1)
                    break
            else:
                if int(s[i])>=5:
                    s[i-1]=str(int(s[i-1])+1)
                else:
                    res=s[:i+1]+['0']*(n-i-1)
                    break
        res="".join(res)
        print(res)