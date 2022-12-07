testcase=int(input())

for i in range(0,testcase):
    n=int(input())
    if n==1:
        print("1")
    elif n==0 or n==2 or n==4:
        print("0")
    else:
        print("2")