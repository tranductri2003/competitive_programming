"""
AGAME
Cho một dãy gồm N phần tử phân biệt. Bạn Đức và Mạnh cùng chơi một trò chơi: mỗi lượt chọn hai
phần tử khác nhau bất kì X và Y sao cho giá trị |X − Y | chưa xuất hiện trong dãy rồi thêm giá trị đó
vào dãy. Ai không thể thực hiện lượt chơi sẽ thua. Biết rằng bạn Đức đi trước, hãy cho biết ai là người
thắng nếu cả hai bạn chơi tối ưu.
Dữ liệu
• Dòng đầu tiên gồm một số nguyên dương T là số bộ dữ liệu.
• Mỗi bộ dữ liệu gồm:
– Dòng thứ nhất gồm một số nguyên dương N.
– Dòng thứ hai gồm N số nguyên dương là các phần tử trong dãy.
Kết quả
• In ra T dòng, mỗi dòng là "M" nếu bạn Mạnh thắng và "DD" nếu bạn Đức thắng.
Giới hạn
• 1 ≤ T ≤ 20.
• 1 ≤ N ≤ 1000.
• Mỗi phần tử trong dãy có giá trị tuyệt đối không quá 109
.
"""
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


testcase=int(input())
for test in range(0,testcase):
    n=int(input())
    a=list(map(int,input().split()))
    solonnhat=max(a)
    ucln=0
    for i in a:
        ucln=gcd(i,ucln)
    sonhonhat=ucln
    sosotatca=(solonnhat-sonhonhat)/ucln+1
    sosophaidien=sosotatca-n
    if sosophaidien%2==1:
        print("DD")
    else:
        print("M")
