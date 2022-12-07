testcase=int(input())
for test in range(testcase):
    n,x,y=list(map(int,input().split()))
    a=list(map(int,input().split()))
    s=sum(a)
    #Tổng hoặc XOR của cả dãy thì tính chẵn lẻ không thay đổi
    if (x+s)%2==y%2:
        print("Alice")
    else:
        print("Bob")