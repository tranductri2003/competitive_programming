MAX=9   #Mảng này có tối đa 10 ô nhớ
stack=[0]*10
top=0

print("Số số muốn nhập:")
n=int(input())
    
for i in range(0,n):
    print("Nhập số thứ "+str(i+1)+" :")
    a=int(input())
    if top+1>MAX:
        print("Stack is full")
        break
    else:
        top+=1
        stack[top]=a
        

print("Số số muốn xuất:")
n=int(input())

for i in range(0,n):
    if top<0:
        print("Stack is empty")
        break
    else:
        print("Số thứ "+str(i+1)+" là:" )
        print(stack[top])
        top-=1



