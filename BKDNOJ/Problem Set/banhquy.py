#https://bkdnoj.dut.udn.vn/public/practice_problem.php?id=DUT21D
n=int(input())

if n==0:
    res=1
else:
    res=3**(n-1)

print(res%(10**6+3))