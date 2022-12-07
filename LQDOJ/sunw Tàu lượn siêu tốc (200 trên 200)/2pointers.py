
n,x=list(map(int, input().split()))
chuoi=list(map(int, input().split()))
chuoi.sort()

ans=0
i=0
j=n-1
stop=False
while stop==False:
    if chuoi[i]+chuoi[j]<=x:   #Cộng một hàng cho số cuối
        ans=ans+1
        i=i+1
        j=j-1
    else:   #Cộng một hàng cho hai số vừa thỏa mãn
        j=j-1
        ans=ans+1
    if i==j:       #Nếu hai số i và j đâm xầm vào nhau thì cộng một hàng
        ans=ans+1
        stop=True
    if i>j:        #Bọn hắn bước qua nhau, đổi vai trò thì không cộng gì cả vì đủ rồi
        stop=True


print(ans)