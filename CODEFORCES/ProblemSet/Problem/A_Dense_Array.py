
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
#//     WELCOME TO MY CODING SPACE
#!      Filename: F_Equalize_the_Array.py
#*      Folder: D:\Code\Python\Codeforces\ProblemSet
#?      Author: TranDucTri2003
#TODO   CreatedAt: 2022-05-07 17:14:12
#? -----------------------------------------------------------------------------------------------------

import math

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=0
    for i in range(n-1):
        if a[i]!=a[i+1]:
            res+=math.ceil(math.log2(max(a[i],a[i+1])/min(a[i+1],a[i])))-1
        
    print(res)
