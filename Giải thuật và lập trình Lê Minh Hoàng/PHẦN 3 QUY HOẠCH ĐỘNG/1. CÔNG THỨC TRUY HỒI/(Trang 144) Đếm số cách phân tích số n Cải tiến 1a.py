v=int(input())

current=[0]*(v+1)
current[0]=1
next=[0]*(v+1)
#Phân tích số v bằng những số nhỏ hơn bằng m
#i chính là m
#j chính là v


#Current là hàng đã có full dữ liệu để tính tiếp các hàng sau
#Next là hàng đang cần tìm (đang tính)

for i in range(1,v+1):
    for j in range(0,v+1):
        #Xét lần lượt các hàng, trong mỗi hàng xét lần lượt các cột trong hàng
        if i>j:  #Tức là m lớn hơn v, hay là khi phân tích số v ta không dùng số m
            next[j]=current[j]
        else:
            next[j]=current[j]+next[j-i]
    current=next #Cập nhật như hai con trỏ


print(current)


#Cách này hơi chậm vì phải dùng phép gán mảng