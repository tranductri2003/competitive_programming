#n: số thành phố
#m: số tuyến đường

n,m=list(map(int,input().split()))
MAX=10**6
table=[]
table.append([])   #Thành phố thứ 0 không tính
for i in range(1,n+1):
    table.append([])  #Mỗi lần thêm vào một thành phố mới, đại diện là một [] còn đang trống
    table[i].append(0)  #Đến thành phố thứ 0 ta thêm cho có
    for j in range(1,n+1):   #Ở mỗi thành phố, giá tiền đến tới các thành phố khác tạm thời là MAX
        table[i].append(MAX)

for i in range(0,m):
    city1,city2,money=list(map(int,input().split()))
    table[city1][city2]=money    #Truy cập vào thành phố 1, nhập money là giá tiền đi từ thành phố 1 đến thành phố 2
    table[city2][city1]=money   #Truy cập vào thành phố 2, nhập money là giá tiền đi từ thành phố 2 đến thành phố 1

free=[True]*(n+1)  #Mọi thành phố tạm thời chưa được chọn
free[1]=False       #Thành phố 1 được chọn rồi
cost=[0]*(n+1)      #Tạo ra n+1 ô giá tiền tương ứng từ thành phố 0 đến thành phố n, giá tiền cost[i] là số tiền cần để đến thành phố thứ i
cost[1]=0    #Thiết lập giá tiền đến thành phố 1 là 0
route=[0]*(n+1)     #Con đường đang xét hiện tại từ thành phố thứ i=0 đến i=n
route[1]=1      #Đương nhiên thành phố đang xét i=1 luôn là thành phố 1
minSpending=MAX
bestWay=[0]*(n+1)   #Đường tối ưu nhất
def travel(i):
    global minSpending  #Biến toàn cục vì cái này cập nhật từ đầu đến khi xuất ra kết quả
    global bestWay
    for city in range(2,n+1):
        if free[city]==True:  #thành phố chưa được chọn
            route[i]=city   #Ta đi thử: thành phố có i là city đó
            cost[i]=cost[i-1]+table[route[i-1]][route[i]]   #Đến i thành phố bằng tổng i-1 và đến thành phố i
            if cost[i]<minSpending:     #Kỹ thuật nhánh cận nhỏ hơn mới xét
                if i<n:
                    free[city]=False    #Chính thức khóa chọn
                    travel(i+1) # Xét tiếp tới i+1 thành phố
                    free[city]=True    #Đệ quy xong thì ta gỡ chọn vì vị trí đó giờ đây đã không được nữa, hết vòng for. Tức là ta xét hết i+1 không cái nào thỏa thì ta phải gỡ vị trí hiện tại của i và thay nó bằng một i mới
                else:
                    if cost[i]+table[route[i]][1]<minSpending:  #Nếu tới được n thành phố thì tổng i và đến thành phố đầu nhỏ hơn minspending mới xét
                        for k in range(1,n+1):
                            bestWay[k]=route[k]                            
                        minSpending=cost[i]+table[route[i]][1]
                       


    
travel(2)
print("####################################################")
if minSpending==MAX:
    print("NO SOLUTION")
else:
    print("Cost: "+str(minSpending))
    for i in range (1,n+1):
        print(bestWay[i],end="->")
    print(1)
"""
Testcase:
6 12
2 5 5
2 6 4
1 2 9
2 4 2
1 4 8
1 3 3
3 6 1
5 4 3
3 4 1
3 5 5
5 6 7
4 6 6
"""