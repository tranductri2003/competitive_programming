testcase=int(input())

for i in range(0,testcase):
    n=int(input())

    line1=str(input())
    line2=str(input())

    for i in range(0,n):
        if line1[i]=="1" and line2[i]=="1":
            print("NO")
            break
    else:
        print("YES")