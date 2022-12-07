testcase=int(input())
for testcase in range(testcase):
    s=input()
    if len(s)>10:
        print(s[0]+str(int(len(s)-2))+s[-1])
    else:
        print(s)