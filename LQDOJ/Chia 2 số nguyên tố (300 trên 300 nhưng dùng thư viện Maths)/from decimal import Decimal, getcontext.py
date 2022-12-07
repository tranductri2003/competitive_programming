from decimal import Decimal, getcontext

a=int(input())
b=int(input())

#Để 102 chữ số sau dấu chấm
getcontext().prec=102 #Độ chính xác là 100 chữ số sau dấu chấm thập phân
thuong=Decimal(a) / Decimal(b)



n=int(input())
#Thao tác tách phần thập phân

thuong=str(thuong) #Đổi sang dạng str mới cắt được
phanthapphan=thuong[thuong.index(".")+1:] #Cắt được


dolonphantuanhoan=0
for dolonphantuanhoan in range (1,50):
    chuoi1=phanthapphan[0:dolonphantuanhoan]
    chuoi2=phanthapphan[dolonphantuanhoan:dolonphantuanhoan*2]
    if chuoi1==chuoi2:
        break

m=n%dolonphantuanhoan
if m>=1:
    print(phanthapphan[m-1])
if m==0:
    print(phanthapphan[dolonphantuanhoan-1])