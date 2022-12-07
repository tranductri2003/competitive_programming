testcase=int(input())
key=str(input())

for i in range(0,testcase):
    chuoi=input()
    stack=0
    for i in range(0,len(chuoi)):
        if chuoi[i]==key[stack]:
            stack=stack+1
        if stack==len(key):
            print("YES")
            stack=0
            break
    else:
        print("NO")
        stack=0
        