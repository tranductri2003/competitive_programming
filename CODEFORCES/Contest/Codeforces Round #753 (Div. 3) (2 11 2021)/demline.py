testcase=int(input())

for test in range(testcase):
    n=int(input())
    a=list(map(int,input().split()))
    color=input()

    blue=[]
    red=[]

    for i in range(0,n):
        if color[i]=="R":
            red.append(a[i])
        else:
            blue.append(a[i])
    
    blue.sort()
    red.sort(reverse=True)


    left=1
    right=n

    stop=False
    for num in blue:
        if num>=left:
            left+=1
        else:
            print("NO")

            stop=True
            break
    
    if stop==False:
        for num in red:
            if num<=right:
                right-=1
            else:
                print("NO")
                break
        else:
            print("YES")

