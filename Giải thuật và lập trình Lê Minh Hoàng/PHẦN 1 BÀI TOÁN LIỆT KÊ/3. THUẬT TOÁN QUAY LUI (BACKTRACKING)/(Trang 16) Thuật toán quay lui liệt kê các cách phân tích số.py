n=int(input())

a=[0]*(n+2)
t=0

def phantichso(i):
    global t
    for v in range(1,n-t+1):
        if v>=a[i-1]:  #Số được chọn thỏa mãn điều kiện nó lớn hơn hoặc bằng số phía trước thì mới được chọn
            t-=a[i]  #Trừ số cũ
            a[i]=v   #Gắn vô
            t +=a[i] #Cập nhật tổng mới
            if t==n: #Tổng mới bằng n thì in ra
                """
                print(str(n)+str("="),end="")
                for k in range(1,n+2):
                    print(a[k],end="")
                    if a[k+1]==0:
                        break
                    else:
                        print("+",end="")
                print(" ")
                """
                print(*a[1:n+1])                
            if t<n:
                phantichso(i+1)  #Nhỏ hơn thì làm tiếp trường hợp tiếp
    t-=a[i]   #Hết vòng lặp thì tổng xóa số ở cuối cùng
    a[i]=0     #Đặt số cuối cùng bằng 0

phantichso(1)