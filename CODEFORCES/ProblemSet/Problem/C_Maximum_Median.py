n,k=list(map(int,input().split()))
a=list(map(int,input().split()))

a.sort()
a=a[n//2:]
#Nếu ô i=0 giống i=0 thì để lên 1 cần 1 
#Nếu ô i=0 giống i=1 thì để lên 1 cần 2

#Thuật toán:
# Chạy i=0 tới hết 
# Với mỗi i sẽ nhìn xem nó kém cái trước mặt nó bao nhiêu, tới
# khi nó bằng được cái sau nó thì mỗi lần tăng res lên i sẽ tốn (i+1) của k

res=a[0]
n=len(a)
for i in range(0,n):
    if k<=0:
        break
    if i==n-1:
        res+=k//(i+1)
        break
    else:
        dis=a[i+1]-a[i]
        if k//(i+1)>dis:
            res+=dis
            k-=dis*(i+1)
        else:
            res+=k//(i+1)
            k-=res*(i+1)

print(res)
        
        

            
        
    