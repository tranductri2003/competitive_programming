testcase=int(input())

for i in range(0,testcase):
    n=int(input())
    if n%2==0:
        print(round(n/2-1))
    else:
        print(n//2)