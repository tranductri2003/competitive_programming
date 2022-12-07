MAX=9   #Mảng này có tối đa 10 ô nhớ
queue=[0]*10
front=0
rear=-1 #   Hoặc rear=MAX
temp=0
print("Số số muốn nhập:")
n=int(input())
    
for i in range(0,n):
    print("Nhập số thứ "+str(i+1)+" :")
    a=int(input())
    if temp+1>MAX+1:
        print("Overflow")
        break
    else:
        rear=(rear+1)%(MAX+1)
        queue[rear]=a
        temp+=1
        

#Thêm rồi xóa cũng chả bị gì cả



print("Số số muốn xuất:")
n=int(input())

for i in range(0,n):
    if temp==0:
        print("Queue is Empty")
        break
    else:
        print("Số thứ "+str(i+1)+" là:" )
        print(queue[front])
        front=(front+1)%(MAX+1)
        temp-=1

print("Số số muốn nhập:")
n=int(input())
    
for i in range(0,n):
    print("Nhập số thứ "+str(i+1)+" :")
    a=int(input())
    if temp+1>MAX+1:
        print("Overflow")
        break
    else:
        rear=(rear+1)%(MAX+1)
        queue[rear]=a
        temp+=1
        

print("Số số muốn xuất:")
n=int(input())

for i in range(0,n):
    if temp==0:
        print("Queue is Empty")
        break
    else:
        print("Số thứ "+str(i+1)+" là:" )
        print(queue[front])
        front=(front+1)%(MAX+1)
        temp-=1





