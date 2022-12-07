testcase=int(input())


for testcase in range(0,testcase):
    a,b,c=list(map(int,input().split()))
    stop=False
    sum=a
    total=sum
    stack=1
    while stop==False:
        if stack<b:
            sum=sum+0.5
        else:
            sum=sum-0.5
        if stack<c:
            sum=sum+0.5
        else:
            sum=sum-0.5
        total=total+sum
        stack=stack+1
        if sum==a and stack>=c and stack>=b:  #Điều kiện sau cực kì quan trọng, với trường hợp b hoặc c bằng 1, thì sum chưa kịp tăng rồi giảm mà dừng luôn
            #Ví dụ a,b,c=2,1,3
            stop=True

    print(round(total))
        