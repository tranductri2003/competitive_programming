n,s=list(map(int,input().split()))


#Nếu tìm được 1 mảng dương có n phần tử và tổng tất cả các phần tử bằng s
#Nếu tồn tại một số k mà không có mảng con nào có tổng bằng k hoặc s-k thì in YES và in mảng đó và k
#Còn lại in NO

if n==1:
    if s==1:
        print("NO")
    else:
        print("YES")
        print(s)
        print(s-1)
else:
    if (n-1)+n<s:
        print("YES")
        res=[1]*(n-1)
        res.append(s-(n-1))
        print(*res)
        print(n)
    else:
        print("NO")