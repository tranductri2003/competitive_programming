v=int(input())


"""
Quy ước:
dp[1]=dòng hiện tại đã có full dữ kiện, dùng để tính những dòng tiếp theo
dp[2]=dòng tiếp theo mà ta đang tính
"""

#Thiết lập dòng hiện tại dp[1] đầu tiên

dp=[[],[],[]]
dp[1]=[0]*(v+1)
dp[1][0]=1
dp[2]=[0]*(v+1)
#Phân tích số v bằng những số nhỏ hơn bằng m
#i chính là m
#j chính là v

x=1
y=2

for i in range(1,v+1):
    for j in range(0,v+1):
        if i>j: #Phân tích số v mà không dùng số m
            dp[y][j]=dp[x][j]
        else: #Phân tích số v mà dùng ít nhất một số m, nên khi ta bỏ m ra sẽ được dp[m,v-m]
            dp[y][j]=dp[x][j]+dp[y][j-i]
    x=3-x
    y=3-y #Đảo giá trị và tính xoay lại

print(dp[2]) 
print(dp[x])
#Phải in dp[2] vì 2 lúc nào cũng đại diện cho hàng mình đang cần tính. 
#Vì kết thúc vòng lặp nên xong hàng cuối là dừng luôn chứ không tính thêm nữa.
#print(dp[x]) vì thực tế trước khi kết thúc, x chính là hàng current nhưng vì lệnh swap nên giờ x như là hàng next