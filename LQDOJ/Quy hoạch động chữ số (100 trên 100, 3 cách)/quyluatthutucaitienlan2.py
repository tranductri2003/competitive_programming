import time

testcase=int(input())
solvedcase=0


def tinhtong(n):
    if n%9==0:
        return 9
    else:
        return n%9 


#Tính thời gian tại thời điểm bắt đầu thuật toán


while solvedcase<testcase:
    l,r=list(map(int,input().split()))
    start_time = time.time()

    khoangcach=r-l
    sotrongkhoangcach=khoangcach//9
    sodu=khoangcach%9

    if sodu==0:
        if tinhtong(l)==9:
            print(sotrongkhoangcach+1)
        else: #tinhtong(l!=9)
            print(sotrongkhoangcach)
    else:  #sodu!=0
        if sodu<9-tinhtong(l):
            print(sotrongkhoangcach)
        else: #sodu=>9-tinhtong(l)
            print(sotrongkhoangcach+1)
    
    solvedcase=solvedcase+1
    
#Tính thời gian tại thời điểm kết thúc thuật toán
end_time = time.time()

#tính thời gian chạy của thuật toán Python
elapsed_time = end_time - start_time
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")