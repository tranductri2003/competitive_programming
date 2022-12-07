chuoi=input()
N=int(chuoi[0:chuoi.index(" ")])
p=int(chuoi[chuoi.index(" "):])
ketqua=0

def kiemtraucln(a,b):
    t=min(a,b)
    ucln=min(a,b)
    while 1 <= ucln <= t:
        if a%ucln==0 and b%ucln==0:
            return ucln
            break
        else:
            ucln=ucln-1

if N%p!=0:
    print("0")
elif N%p==0:
    m=N/p
    for i in range (1,int(m)+1):
        if kiemtraucln(i*p,N)==p:
            ketqua=ketqua+1     
    print(ketqua)

else:   
    for x in range(p,N+1):
        if kiemtraucln(x,N)==p:
            ketqua=ketqua+1     
    print(ketqua)
