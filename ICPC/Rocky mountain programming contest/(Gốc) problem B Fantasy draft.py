
import time


soluongchu,soluongthanhvien=list(map(int,input().split()))
#n                  #k

danhsachuutien=[0]*(soluongchu+1)
soluonguutien=[0]*(soluongchu+1)
danhsach=[0]*(soluongchu+1)

for i in range(1,soluongchu+1):
    danhsachuutien[i]=list(map(str,input().split()))
    soluonguutien[i]=danhsachuutien[i][0]
    danhsachuutien[i].remove(soluonguutien[i])


    


tongthanhvien=int(input())
danhsachthanhvien=list()
for i in range(0,tongthanhvien):
    tenthanhvien=str(input())
    danhsachthanhvien.append(tenthanhvien)

soluong=0

for i in range(1,soluongchu+1):
    danhsach[i]=list()





#Tính thời gian tại thời điểm bắt đầu thuật toán
start_time = time.time()



for k in range(0,soluongthanhvien):

    for i in range(1,soluongchu+1):        
        if danhsachuutien[i]!=[]:
            danhsach[i].append(danhsachuutien[i][0])
            danhsachthanhvien.remove(danhsachuutien[i][0])
            for j in range(1,soluongchu+1):
                if j!=i and danhsachuutien[i][0] in danhsachuutien[j]:
                    danhsachuutien[j].remove(danhsachuutien[i][0])
            danhsachuutien[i].remove(danhsachuutien[i][0])
        else:
            danhsach[i].append(danhsachthanhvien[0])
            for j in range(1,soluongchu+1):
                if j!=i and danhsachthanhvien[0] in danhsachuutien[j]:
                    danhsachuutien[j].remove(danhsachthanhvien[0])
            danhsachthanhvien.remove(danhsachthanhvien[0])
            
 

for i in range(1,soluongchu+1):
    for ten in danhsach[i]:
        print(ten,end=" ")
    print(" ")


#Tính thời gian tại thời điểm kết thúc thuật toán
end_time = time.time()

#tính thời gian chạy của thuật toán Python
elapsed_time = end_time - start_time
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
