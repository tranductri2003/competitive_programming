import time

testcase=int(input())
solvedcase=0
quantity=0

def dequy(n):
    sum=0
    if n<10:
        return n
    else:
        n=n
        while n>0:
            sum = sum + n % 10
            n = n // 10
        return dequy(sum)

#Tính thời gian tại thời điểm bắt đầu thuật toán


while solvedcase<testcase:
    l,r=list(map(int,input().split()))
    start_time = time.time()

    for i in range(l,r+1):
        if dequy(i)==9:
            quantity=quantity+1
    print(quantity)
    quantity=0


    solvedcase=solvedcase+1
    
#Tính thời gian tại thời điểm kết thúc thuật toán
end_time = time.time()

#tính thời gian chạy của thuật toán Python
elapsed_time = end_time - start_time
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")