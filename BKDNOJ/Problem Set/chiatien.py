#https://bkdnoj.dut.udn.vn/contest/problem.php?cid=KTLT2110IF&probid=H

n=int(input())

c=(3*n)/(11/6+7/6+1)
a=11/6*c
b=7/6*c

if a%1!=0 or b%1!=0 or c%1!=0:
    print("NO")
else:
    c=(3*n)/(11/6+7/6+1)
    a=11/6*c
    b=7/6*c
    a=str(a)[:-2]
    b=str(b)[:-2]
    c=str(c)[:-2]
    print(f"{a} {b} {c}")
    
    