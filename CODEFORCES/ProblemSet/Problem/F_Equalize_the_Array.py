
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

from collections import defaultdict

t=int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    #in ra số lượng ký tự ít nhất phải xóa để số lần xuất hiện của mỗi ký tự trong a là như nhau
    distribution=defaultdict(lambda:0)
    for num in a:
        distribution[num]+=1
    fre=sorted(list(distribution.values()))   #Mỗi số xuất hiện mấy lần
    
    tanxuat=defaultdict(lambda:0)   #Xuất hiện i lần thì có bao nhiêu số
    for num in fre:
        tanxuat[num]+=1
    # print(tanxuat)
    
    #Chỉ chừa lại một tần xuất cuối cùng
    #Chạy tất cả các tần xuất, khi sử dụng một tần xuất nào đó
    #là ta phải xóa tất cả num*tanxuat[num] trước nó và và phía sau nó chỉ cần xóa
    # tanxuat[số đó] *(sodo-num)

    #? Tức là sẽ chừa lại số lần xuất hiện nhân cho tổng của đám sau
    mangtondon=[0]
    temp=0
    for num in tanxuat:
        temp+=tanxuat[num]
        mangtondon.append(temp)
    # print(mangtondon)
    
    res=10**9
    mang=list(tanxuat.keys())
    for i in range(len(mang)):
        res=min(res,n-mang[i]*(mangtondon[-1]-mangtondon[i]))
    print(res)