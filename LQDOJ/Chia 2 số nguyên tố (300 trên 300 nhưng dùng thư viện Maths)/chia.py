from decimal import Decimal, getcontext

a=int(input("Số thập phân thứ nhất: "))
b=int(input("Số thập phân thứ hai: "))

#Để 102 chữ số sau dấu chấm
getcontext().prec=1002 #Độ chính xác là 100 chữ số sau dấu chấm thập phân
thuong=Decimal(a) / Decimal(b)



n=int(input("Mời bạn nhập n: "))
#Thao tác tách phần thập phân

thuong=str(thuong) #Đổi sang dạng str mới cắt được
phanthapphan=thuong[thuong.index(".")+1:] #Cắt được
print("Phần thập phân để bạn dễ kiểm tra nè: " +phanthapphan) #In ra dưới dạng chuỗi để dễ sử dụng mảng

dolonphantuanhoan=0
for dolonphantuanhoan in range (1,500):
    chuoi1=phanthapphan[0:dolonphantuanhoan]
    chuoi2=phanthapphan[dolonphantuanhoan:dolonphantuanhoan*2]
    if chuoi1==chuoi2:
        print("Thương có độ lớn vòng tuần hoàn là "+str(dolonphantuanhoan)+" số")
        break

m=n%dolonphantuanhoan
if m>=1:
    print("Số chữ số thứ n sau dấu chấm mà bạn cần tìm là: "+phanthapphan[m-1])
if m==0:
    print("Số chữ số thứ n sau dấu chấm mà bạn cần tìm là: "+phanthapphan[dolonphantuanhoan-1])