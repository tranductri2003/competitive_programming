"""
Cho tập hợp gồm N số nguyên dương A={a1,a2,...,aN}. Taro và Jiro chơi với nhau một trò chơi như sau:

Ban đầu, chúng ta có một đống đá chứa K viên đá. Hai người chơi sẽ lần lượt thực hiện 1 nước đi như sau, với Taro là người bắt đầu:

Chọn một phần tử x của tập A, và loại bỏ đi chính xác x viên đá từ đống đá.
Người nào không thể thực hiện được nước đi, thì đó là người thua cuộc. Giả sử cả hai người đều chơi tối ưu, xác định người chiến thắng.

Input:
Dòng thứ nhất chứa hai số nguyên dương N,K(1≤N≤100,1≤K≤105).
Dòng thứ hai chứa N số nguyên dương thỏa mãn 1≤a1<a2<a3<...<aN≤K.
Output:
Nếu Taro là người thắng cuộc, in ra First, ngược lại nếu Jiro thắng in ra Second.
"""
#K là số viên đá trong đống đá
N,K=list(map(int,input().split()))
a=list(map(int,input().split()))

#dp[i]: Là kết quả người thắng cuộc với số đá trong đống là i, 
#hay nói một cách khác là kết quả tối ưu đối với người chơi Taro (first)
#Nếu dp[i]=1 thì Taro là người thắng, dp[i]=0 thì Jiro là người thắng

dp=[0]*(K+1)
min=min(a)
#Đang xét theo cách chơi tối ưu nhất của Taro
for i in range(1,K+1):
    if i<min:
        dp[i]=0  #Taro thua vì không thực hiện được bước đi
    else:
        for rock in a:
            if i-rock>=0 and dp[i-rock]==0:
                dp[i]=1 #Taro thắng vì sau khi Taro xong lượt, đổi sang lượt của Jiro thì Jiro chỉ có thua thôi
                break
        else:
            dp[i]=0 #Không có vị trí nào để Jiro thua, hay khi đổi sang lượt Jiro thì Jiro chắc chắn thắng
#print(dp)
if dp[K]==1:
    print("First")
else:
    print("Second")