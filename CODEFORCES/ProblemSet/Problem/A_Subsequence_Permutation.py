testcase=int(input())
for test in range(testcase):
    n=int(input())
    string=input()
    new=sorted(string)
    res=0
    for i in range(n):
        if new[i] != string[i]:
            res+=1
    print(res)