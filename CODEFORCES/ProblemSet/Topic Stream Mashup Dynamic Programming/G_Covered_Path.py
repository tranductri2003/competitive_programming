#v first, v fast
#t: thời gian đi hết, d: tốc độ chênh lệch tối đa giữa 2s


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
#!      Filename: G_Covered_Path.py
#*      Folder: D:\Code\Python\Codeforces\ProblemSet\Topic Stream Mashup Dynamic Programming
#?      Author: TranDucTri2003
#TODO   CreatedAt: 08/08/2022 23:16:12
#? -----------------------------------------------------------------------------------------------------

v1,v2=list(map(int,input().split()))
t,d=list(map(int,input().split()))

left=[v1]
right=[v2]

for i in range(t-1):
    left.append(left[-1]+d)
for i in range(t-1):
    right.insert(0,right[0]+d)

res=[]
for i in range(t):
    res.append(min(left[i],right[i]))
print(sum(res))
           