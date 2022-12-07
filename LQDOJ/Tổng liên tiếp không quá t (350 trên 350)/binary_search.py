n,t=list(map(int,input().split()))
chuoi=list(map(int,input().split()))

def binary_search(chuoinhatbien,giatricanxacdinhvitri):
    bottom=0
    top=len(chuoinhatbien)-1

    while bottom<=top:
        middle=(bottom+top)//2

        if chuoinhatbien[middle]==giatricanxacdinhvitri:
            return middle
    
        elif chuoinhatbien[middle]>giatricanxacdinhvitri:
            top=middle-1
        else:
            bottom=middle+1
    return middle






mangtong=list()
#Mảng tổng phải có số 0 đầu tiên đề phòng mangtong[i-1]
mangtong.append(0)
tong=0





for i in range(0,n):
    tong=tong+chuoi[i]
    mangtong.append(tong)



length=0
lengthmax=0
if mangtong[n]<=t:
    print(n)

else:

    for j in range(n,0,-1):  #j là biến chạy vị trí bắt đầu, i là biến chạy bổ trợ

        i=binary_search(mangtong,mangtong[j]-t)+1  #Công thức tính tổng: tổng từ i tới j là bằng a[j] -a[i-1]
        length=j-i+1
        if length>lengthmax and mangtong[j]-mangtong[i-1]<=t:   #Khi binary_search một giá trị không có, nó sẽ trả về giá trị gần nhất nên làm vậy để đề phòng tìm tổng lớn hơn k
            lengthmax=length
    print(lengthmax)