testcase=int(input())
key="hello"

for i in range(0,testcase):
    chuoi=input()
    stack=0
    for i in range(0,len(chuoi)):
        if chuoi[i]==key[stack]:
            stack=stack+1
        if stack==5:
            print("YES")
            stack=0
            break
    else:
        print("NO")
        stack=0
        