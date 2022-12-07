testcase=int(input())

for test in range(0,testcase):
    n=int(input())
    a=list(map(int,input().split()))

    so0=0
    so1=0
    for num in a:
        if num==0:
            so0+=1
        if num==1:
            so1+=1
    
    print(so1+so1*(2**so0-1))
    