t=int(input())

for _ in range(t):
    n=int(input())
    #Thay 2 số bằng khoảng cách của chúng mà tổng mới lớn hơn hoặc bằng thì in YES
    #Còn lại in NO
    if n<=19:
        print("YES")
        res=[1]
        for i in range(1,n):
            res.append(res[-1]*3)
        print(*res)
    else:
        print("NO")