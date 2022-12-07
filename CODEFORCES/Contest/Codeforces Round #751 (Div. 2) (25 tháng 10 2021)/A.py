testcase=int(input())

for test in range(0,testcase):
    s=input()
    a=min(s)
    vitri=s.index(a)
    print(a,end=" ")
    for i in range(0,len(s)):
        if i!=vitri:
            print(s[i],end="")
    print(" ")