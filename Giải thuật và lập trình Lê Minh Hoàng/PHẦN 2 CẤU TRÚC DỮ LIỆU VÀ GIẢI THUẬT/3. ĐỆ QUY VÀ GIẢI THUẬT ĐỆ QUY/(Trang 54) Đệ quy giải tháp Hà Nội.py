#n: Số đĩa cần chuyển
#x: cột nguồn
#y: cột đích
def move(n,x,y):
    #Phần neo: Bước cuối chỉ còn xét chuyển đĩa từ cột nguồn sang cột đích
    if n==1:
        print("Chuyển từ cột "+str(x)+" sang cột "+str(y))
    #Để chuyển n>1 đĩa từ cọc x sang cọc y ta chia làm 3 công đoạn:
    else:
       

        move(n-1,x,6-x-y) #Bước 1: ta chuyển n-1 đĩa từ cột x sang cột trung gian
        move(1,x,y)# Bước 2: Chuyển đĩa to nhất từ x sang y
        move(n-1,6-x-y,y)#Bước 3: Chuyển n-1 đĩa từ cọc trung gian sang cọc y

n,x,y=list(map(int,input().split()))

move(n,x,y)



"""
n=3 gặp câu lệnh 1
đệ quy xuống n=2
n=2 đệ quy xuống n=1 thực hiện câu lệnh 1
xong thực hiện câu lệnh 2 của n=2
xong thực hiện câu lệnh 3 của n=2
lúc này lại đệ quy xuống thực hiện cây lệnh 1
xong lại thực hiện câu lệnh 2 n=3

""" 