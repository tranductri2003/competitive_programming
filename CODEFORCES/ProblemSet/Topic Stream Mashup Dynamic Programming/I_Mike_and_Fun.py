
#? -----------------------------------------------------------------------------------------------------
#?　　　　　　　　　　　 ∧＿∧
#?　　　　　 ∧＿∧ 　 （´<_｀ ）　     
#?　　　　 （ ´_ゝ`）　/　 ⌒i        
#?　　　　／　　　＼　 　  |　|       
#?　　　 /　　 /￣￣￣￣/　|　 |
#?　 ＿_(__ﾆつ/　    ＿/ .| .|＿＿＿＿
#?　 　　　＼/＿＿＿＿/　（u　⊃
#?
#?		 /\_/\
#?		(= ._.)
#?		/ >WA \>AC
#?
#       WELCOME TO MY CODING SPACE
#!      Filename: I_Mike_and_Fun.py
#*      Folder: D:\Code\Python\Codeforces\ProblemSet\Topic Stream Mashup Dynamic Programming
#?      Author: TranDucTri2003
#TODO   CreatedAt: 08/09/2022 22:20:01
#? -----------------------------------------------------------------------------------------------------

from collections import defaultdict


n,m,q=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]

data=defaultdict(lambda:0)

for i in range(n):
    stack=0    
    currentMax=0
    for j in range(m):
        if matrix[i][j]==1:
            stack+=1
        else:
            stack=0
        currentMax=max(currentMax,stack)
    data[i]=currentMax


            
for i in range(q):
    r,c=list(map(int,input().split()))
    
    r-=1;c-=1

    matrix[r][c]=1 if matrix[r][c]==0 else 0
    
    stack=0
    currentMax=0
    for j in range(m):
        if matrix[r][j]==1:
            stack+=1
        else:
            stack=0
        currentMax=max(currentMax,stack)
    data[r]=currentMax
    
    print(max(data.values()))

