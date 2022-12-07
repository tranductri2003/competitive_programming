

n=int(input())

a=list(range(1,n+1))
i=n-2
print(*a)
while i>=0:
    if a[i]<a[i+1]: #Kết thúc chuỗi giảm dần
        for j in range(n-1,i,-1): #Tìm vị trí để swap
            if a[j]>a[i]: #Vị trí nhỏ nhất lớn hơn a[i]
                a[i],a[j]=a[j],a[i] #Swap
                start=i+1 #Thiết lập đảo    
                end=n-1   #Thiết lập đảo
                while start<end:  #Sắp xếp theo thứ tự tăng dần từ sau vị trí i+1 đến hết
                    a[start],a[end]=a[end],a[start]
                    start+=1
                    end-=1
                print(*a) #Dấu * làm mất đi dấu ngoặc vuông ở ngoài
                i=n-1
                break
    i-=1



#Có thể hiểu là chèn sao cho từ dãy ban đầu là nhỏ nhất: 1234 thành lớn nhất 4321 

#Chèn các chữ số vào đúng các vị trí thích hợp của nó. Sắp xếp tăng dần trong quá trình giải để liệt kê mọi trường hợp khả thi của thuật toán

