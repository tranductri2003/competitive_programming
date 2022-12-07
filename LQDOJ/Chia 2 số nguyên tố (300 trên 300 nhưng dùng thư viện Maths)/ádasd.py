from decimal import Decimal, getcontext

a=int(input())
b=int(input())

#Để 102 chữ số sau dấu chấm
getcontext().prec=1002 #Độ chính xác là 100 chữ số sau dấu chấm thập phân
t=Decimal(a) / Decimal(b)



n=int(input())
#Thao tác tách phần thập phân

t=str(t) 
ptp=t[t.index(".")+1:] 

for l in range (1,500):
    s1=ptp[0:l]
    s2=ptp[l:(l*2)]
    if s1==s2:
        break

m=n%l
if m>=1:
    print(ptp[m-1])
if m==0:
    print(ptp[l-1])