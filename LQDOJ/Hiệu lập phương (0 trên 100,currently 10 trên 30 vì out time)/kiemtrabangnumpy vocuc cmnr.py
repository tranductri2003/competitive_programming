import sympy
import time


#Tính thời gian tại thời điểm bắt đầu thuật toán
start_time = time.time() 

soluongcauhoi=int(input())

for i in range(0,soluongcauhoi):
    a=int(input())
    if a==1:
        print("0")
    else:
        if sympy.ntheory.primetest.isprime(3*a**2-3*a+1)==True:
            print("1")
        else:
            print("0")

#Tính thời gian tại thời điểm kết thúc thuật toán
end_time = time.time()

#tính thời gian chạy của thuật toán Python
elapsed_time = end_time - start_time
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")