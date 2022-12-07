n=int(input())

res=[]
for i in range(0,n+1):
    res.append([])

a=[True]*(n+1)  #Collumn
b=[True]*(2*n+1)  #Chéo đông bắc
c=dict()   #Chéo tây nam
for i in range(1-n,n):
    c[i]=True

def vitriquanhau(row):   #row chính là hàng đang xét
    for collumn in range(1,n+1):
        if a[collumn]==b[row+collumn]==c[row-collumn]==True:  #Nếu cột đó, chéo đông bắc tại vị trí đó và chéo đông nam tại vị trí đó còn tự do      
            res[row].append(collumn)
            res[row].append(row)
            a[collumn]=b[collumn+row]=c[row-collumn]=False  #Các cột, đường chéo chỗ đặt quân hậu bị khóa
            if row==n:
                print(*res[1:n+1])
                a[res[row][0]]=b[row+res[row][0]]=c[row-(res[row][0])]=True   #Vị trí quân hậu thứ cuối cùng sẽ được reset lại
                res[row]=[]  #Con hậu thứ i lúc này (thứ cuối cùng) đã được đặt xuống nên phải reset       
            else:
                vitriquanhau(row+1)
                #Sau khi gọi đệ quy tìm cách đặt quân hậu thứ i+1, có nghĩa là sắp tới ta lại thử một cách đặt khác cho quân hậu thứ i, nên ta bỏ đánh dấu cột và 2 đường chéo bị quân hậu vừa rồi thử đặt khống chế
                a[res[row][0]]=b[row+res[row][0]]=c[row-(res[row][0])]=True
                res[row]=[] 
    if row==1:  #Duyệt hết mọi vị trí khả thi ở dòng đầu rồi
        quit()
   

vitriquanhau(1)





































"""
n=int(input())

res=[]
for i in range(0,n+1):
    res.append([])

a=[True]*(n+1)  #Collumn
b=[True]*(2*n+1)  #Chéo đông bắc
c=dict()   #Chéo tây nam
for i in range(1-n,n):
    c[i]=True

def vitriquanhau(row):   #row chính là hàng đang xét
    for collumn in range(1,n+1):
        if a[collumn]==b[row+collumn]==c[row-collumn]==True:  #Nếu cột đó, chéo đông bắc tại vị trí đó và chéo đông nam tại vị trí đó còn tự do      
            res[row].append(collumn)
            res[row].append(row)
            a[collumn]=b[collumn+row]=c[row-collumn]=False  #Các cột, đường chéo chỗ đặt quân hậu bị khóa
            if row==n:
                print(*res[1:n+1])
                a[res[row][0]]=b[row+res[row][0]]=c[row-(res[row][0])]=True   #Vị trí quân hậu thứ cuối cùng sẽ được reset lại
                res[row]=[]  #Con hậu thứ i lúc này (thứ cuối cùng) đã được đặt xuống nên phải reset       
            else:
                vitriquanhau(row+1)
    if row==1:  #Duyệt hết mọi vị trí khả thi ở dòng đầu rồi
        quit()
    a[res[row-1][0]]=b[row-1+res[row-1][0]]=c[row-1-(res[row-1][0])]=True  #Mỗi lần chạy hết vòng for tức là con hậu thứ i đang xét không thể tìm được vị trí thỏa đề, nên ta phải reset lại vị trí của con hậu thứ i-1
    #Con hậu thứ i không cần reset vì nó chưa được đặt xuống
    res[row-1]=[] 

vitriquanhau(1)

"""





