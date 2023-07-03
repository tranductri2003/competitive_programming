from collections import defaultdict


for _ in range(int(input())):
    check = defaultdict(lambda: ["A", "B", "C", "D"])
    res = defaultdict(lambda: "?")
    Q,M=list(map(int,input().split()))
    for hocsinh in range(M):
        a=input().split()
        for i in range(0,2*Q,2):
            if a[i+1]=="T":
                res[i//2]=a[i]
            else:
                if a[i] in check[i//2]:
                    check[i//2].remove(a[i])
    for i in range(Q):
        if len(check[i])==1:
            res[i]=check[i][0]

    ans=[]
    for i in range(Q):
        ans.append(res[i])
    print(*ans)
