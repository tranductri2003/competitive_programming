testcase=int(input())

for test in range(0,testcase):
    a,b,c=list(map(int,input().split()))
    s=a+b*2+c*3
    print(s%2)