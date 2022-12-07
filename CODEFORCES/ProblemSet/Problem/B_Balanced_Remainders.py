
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


#Được thêm 1
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c0=0
    c1=0
    c2=0

    for num in a:
        if num%3==0:
            c0+=1
        elif num%3==1:
            c1+=1
        else:
            c2+=1
    muctieuchung=(c0+c1+c2)//3
    
    res=0
    if c0==c1==c2==muctieuchung:
        print(0)
    else:
        if c0==min(c1,c2,c0):
            res+=muctieuchung-c0
            c0+=muctieuchung-c0
            c2-=muctieuchung-c0
        elif c1==min(c2,c0,c1):
            res+=muctieuchung-c1
            c1+=muctieuchung-c1
            c0-=muctieuchung-c1
        else:
            res+=muctieuchung-c2
            c2+=muctieuchung-c2
            c1-=muctieuchung-c2
            
        if c0==c1==c2==muctieuchung:
            print(0)
        else:
            if c0==min(c1,c2,c0):
                res+=muctieuchung-c0
                c0+=muctieuchung-c0
                c2-=muctieuchung-c0
            elif c1==min(c2,c0,c1):
                res+=muctieuchung-c1
                c1+=muctieuchung-c1
                c0-=muctieuchung-c1
            else:
                res+=muctieuchung-c2
                c2+=muctieuchung-c2
                c1-=muctieuchung-c2
            if c0==c1==c2==muctieuchung:
                print(0)
            else:
                if c0==min(c1,c2,c0):
                    res+=muctieuchung-c0
                    c0+=muctieuchung-c0
                    c2-=muctieuchung-c0
                elif c1==min(c2,c0,c1):
                    res+=muctieuchung-c1
                    c1+=muctieuchung-c1
                    c0-=muctieuchung-c1
                else:
                    res+=muctieuchung-c2
                    c2+=muctieuchung-c2
                    c1-=muctieuchung-c2             
                print(res)