def tinhDienTich(a,b,c):
    p=(a+b+c)/2
    area=(p*(p-a)*(p-b)*(p-c))**0.5
    return area
    
a,b,c=input().split()
a=float(a)
b=float(b)
c=float(c)
S1=tinhDienTich(a,b,c)

a,b,c=input().split()
a=float(a)
b=float(b)
c=float(c)
S2=tinhDienTich(a,b,c)

a,b,c=input().split()
a=float(a)
b=float(b)
c=float(c)
S3=tinhDienTich(a,b,c)

print("Dien tich tam giac lon nhat:",format(max(S1,S2,S3),".2f"))

