n,p=list(map(int,input().split()))

demphanphoi=[True]*(n+1)   #Mọi phần tử đều là tự do
a=[0]*(p+1)


def chinhhop(i):
    for v in range(1,n+1):
        demphanphoi[a[i-1]]=False    #Phần tử trước nó đã được chọn, lặp lại trên một đống số sẽ không bị lặp
        if demphanphoi[v]==True:  #Nếu phần tử vẫn còn tự do
            demphanphoi[a[i]]=True   #Số hiện tại thành tự do (số sắp sửa sẽ bị đổi)           
            a[i]=v     #Thay đổi giá trị
            if i==p:
                print(*a[1:p+1])
            else:
                chinhhop(i+1)
    demphanphoi[a[i]]=True    #Sau khi hết vòng lặp thì số hiện tại cũng trả về tự do



chinhhop(1)
