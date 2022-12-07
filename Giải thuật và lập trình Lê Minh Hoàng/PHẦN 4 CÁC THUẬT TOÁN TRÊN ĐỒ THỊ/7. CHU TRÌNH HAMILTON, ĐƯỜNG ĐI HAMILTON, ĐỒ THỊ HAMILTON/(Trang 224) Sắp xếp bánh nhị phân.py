#Đổi list sang str
def listToStr(list):
    a=""
    for i in list:
        a=a+str(i)
    return a

#Thuật toán liệt kê các dãy nhị phân có độ dài n
data=[]
def backtrack(i): 
    for value in range(0,2):
        a[i]=value
        if i==n-1:
            data.append(listToStr(a))
        else:
            backtrack(i+1)

#Thuật toán kiểm tra hai xâu cạnh nhau có chỉ khác nhau đúng 1 bit hay không
def check(a,b):
    temp=0
    for i in range(0,n):
        if a[i]!=b[i]:
            temp+=1
        if temp==2:
            return False
    if temp==1:
        return True
    return False
        
#Thuật toán quay lui chu trình hamilton tìm ra cách đặt các xâu nhị phân đúng chỗ
def Try(i):
    for j in data:
        if free[j]==True and check(route[i-1],j)==True:
            route[i]=j
            if i<(2**n):
                free[j]=False
                Try(i+1)
                free[j]=True
            else:
                if check(j,route[1])==True:
                    print(f"Thứ tự sắp xếp các xâu nhị phân độ dài là n={n} là:")
                    print(*route[1:2**n+1],end=" ")
                    print(data[0])
                    quit()



print("Mời bạn nhập độ dài n các xâu nhị phân:")
n=int(input())
a=[0]*n
backtrack(0)

free={}
for i in data:
    free[i]=True
free[data[0]]=False

route=[0]*(2**n+1)
route[1]=data[0]

Try(2)
print(route)
print(data)
print(free)