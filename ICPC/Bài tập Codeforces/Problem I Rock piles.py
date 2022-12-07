testcase=int(input())

for i in range(0,testcase):
    a,b=list(map(int,input().split()))
    if a%2==0 and b%2==0:
        print("abdullah")
    else:
        print("hasan")