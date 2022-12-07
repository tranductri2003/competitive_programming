import time

testcase=int(input())
solvedcase=0
quantity=0

def tinhtong(n):
    if n%9==0:
        return 9
    else:
        return n%9 


#Tính thời gian tại thời điểm bắt đầu thuật toán


while solvedcase<testcase:
    l,r=list(map(int,input().split()))
    start_time = time.time()

    for i in range(l,r+1):
        if tinhtong(i)==9:
            quantity=quantity+1
    print(quantity)
    quantity=0


    solvedcase=solvedcase+1
    
#Tính thời gian tại thời điểm kết thúc thuật toán
end_time = time.time()

#tính thời gian chạy của thuật toán Python
elapsed_time = end_time - start_time
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")