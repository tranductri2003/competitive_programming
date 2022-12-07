# https://bkdnoj.dut.udn.vn/public/practice_problem.php?id=DUT21C

s=input()


if set(s)=={"/"}:
    print("/")
else:

    n=len(s)
    available=True
    res=[]
    for i in range(0,n):
        if s[i]!="/":
            res.append(s[i])
            available=True
        else:
            if available==True:
                res.append("/")
                available=False
    if res[-1]=="/":
        res.pop()
    for i in res:
        print(i,end="")