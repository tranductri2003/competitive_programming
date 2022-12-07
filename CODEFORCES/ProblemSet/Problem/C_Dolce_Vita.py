
#?		 /\_/\
#?		(= ._.)
#?		/ >WA \>AC
#//     WELCOME TO MY CODING SPACE
#!      Filename: C_Dolce_Vita.py
#*      Folder: D:\Code\Python\Codeforces\ProblemSet
#?      Author: TranDucTri2003
#TODO   CreatedAt: 2022-05-06 21:51:08



t=int(input())
for _ in range(t):
    n,x=list(map(int,input().split()))
    a=list(map(int,input().split()))
    a.sort()
    res=0
    # budget=x
    # for i in range(n):
    #     if a[i]<=budget:
    #         start=a[i]
    #         end=budget
    #         res+=(end-start)//(i+1)+1
    #         budget-=a[i]
    #     else:
    #         break
    S=0
    for i in range(n):
        S+=a[i]
        res+=max(0,(x-S)//(i+1)+1)
    print(res)