testcase=int(input())
for test in range(testcase):
    n,k=list(map(int,input().split()))
    string=input()
    if string==string[::-1] or k==0:
        print(1)
    else:
        print(2)