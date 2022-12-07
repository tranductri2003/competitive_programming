
#?		 /\_/\
#?		(= ._.)
#?		/ >WA \>AC
#//     WELCOME TO MY CODING SPACE
#!      Filename: C_Swap_Adjacent_Elements.py
#*      Folder: D:\Code\Python\Codeforces\ProblemSet
#?      Author: TranDucTri2003
#TODO   CreatedAt: 2022-05-04 02:56:42

from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
s=input()
temp=0
for i in range(n):
    temp=max(temp,a[i])
    if temp>i+1 and s[i]=='0':
        print("NO")
        break
else:
    print("YES")
    
    
    

