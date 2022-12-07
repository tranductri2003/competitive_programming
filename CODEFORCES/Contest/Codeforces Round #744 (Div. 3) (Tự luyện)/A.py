testcase=int(input())

for test in range(0,testcase):
    s=input()
    soAC=0
    soB=0
    for chu in s:
        if chu=="A" or chu=="C":
            soAC+=1
        else:
            soB+=1
    if soAC==soB:
        print("YES")
    else:
        print("NO")
