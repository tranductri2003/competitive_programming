testcase=int(input())
for test in range(testcase):
    n=int(input())
    string=input()
    so1=00
    so0=00
    so1=string.count("1")
    so0=string.count("0")
    if so1<=1 and so0<=1:
        print("YES")
    else:
        print("NO")