from collections import defaultdict

#?		 /\_/\
#?		(= ._.)
#?		/ >WA \>AC
#//     WELCOME TO MY CODING SPACE
#!      Filename: E_Accidental_Victory.py
#*      Folder: D:\Code\Python\Codeforces\ProblemSet
#?      Author: TranDucTri2003
#TODO   CreatedAt: 2022-05-07 16:56:38



t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=a.copy()
    a.sort() 
    prefixSum=[0]
    temp=0
    for num in a:
        temp+=num
        prefixSum.append(temp)
    #Nếu một người chơi ăn hết được những người chơi nhỏ hơn hoặc bằng mình và tăng dần lên thì người đó có cơ hội thắng
    allowed=defaultdict(lambda:False)
    allowed[a[-1]]=True
    for i in range (n-1,-1,-1):
        # if prefixSum[i]*2>=prefixSum[i+1]:
        if prefixSum[i]>=(prefixSum[i+1]-prefixSum[i]):
            allowed[prefixSum[i]-prefixSum[i-1]]=True
        else:
            break
    res=[]
    for i in range(n):
        if allowed[b[i]]==True:
            res.append(i+1)
    print(len(res))
    print(*res)
    