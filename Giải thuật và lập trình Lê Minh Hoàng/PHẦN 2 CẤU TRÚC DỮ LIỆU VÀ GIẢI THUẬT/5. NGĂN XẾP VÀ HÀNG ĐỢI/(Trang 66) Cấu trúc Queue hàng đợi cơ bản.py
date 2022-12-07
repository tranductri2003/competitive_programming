MAX=9   #Mảng này có tối đa 10 ô nhớ
queue=[0]*10
front=0
rear=-1

print("Số số muốn nhập:")
n=int(input())
    
for i in range(0,n):
    print("Nhập số thứ "+str(i+1)+" :")
    a=int(input())
    if rear+1>MAX:
        print("Overflow")
        break
    else:
        rear+=1
        queue[rear]=a
        

print("Số số muốn xuất:")
n=int(input())

for i in range(0,n):
    if front>rear:
        print("Queue is Empty")
        break
    else:
        print("Số thứ "+str(i+1)+" là:" )
        print(queue[front])
        front+=1

"""
Quá MAX sẽ bị overflow ngay dù ta đã xóa đi các phần tử rồi tiếp tục thêm vào


print("Số số muốn nhập:")
n=int(input())
    
for i in range(0,n):
    print("Nhập số thứ "+str(i+1)+" :")
    a=int(input())
    if rear+1>MAX:
        print("Overflow")
        break
    else:
        rear+=1
        queue[rear]=a
        

print("Số số muốn xuất:")
n=int(input())

for i in range(0,n):
    if front>rear:
        print("Queue is Empty")
        break
    else:
        print("Số thứ "+str(i+1)+" là:" )
        print(queue[front])
        front+=1


"""
