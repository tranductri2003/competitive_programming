testcase=int(input())

for i in range(0,testcase):
    a,b,c=list(map(int,input().split()))
    if min(a,b,c)==a:
        print("First")
    if min(a,b,c)==b:
        print("Second")
    if min(a,b,c)==c:
        print("Third")