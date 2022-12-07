testcase=int(input())
for test in range(testcase):
    string=input()
    so0=string.count("0")
    so1=string.count("1")
    if so0==so1:
        print(max(min(so1,so0)-1,0))
    else:
        print(max(min(so1,so0),0))