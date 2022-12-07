testcase=int(input())
for test in range(testcase):
    n,x,t=list(map(int,input().split()))
    if x>t:
        res=0
    elif x==t:
        res=n-1
    else:
        toida=t//x
        #Đã hiểu:
        #Bởi vì tối đa có thể lớn hơn n. Nên ta phải dùng công thức dưới
        #thay vì res=toida*(n-toida)+(toida)*(toida-1)//2 để toida luôn nhỏ hơn hoặc bằng n
        res=    max(0,toida*(n-toida))    +      min(n,toida)*min(n-1,toida-1)//2
    print(res)