
testcase=int(input())
for test in range(0,testcase):
    n=int(input())
    a=list(map(int,input().split()))
    available=0
    for i in range(0,n):
        for j in range(i+2,i+2-available-1,-1):
            if a[i]%j!=0:
                break
        else:
            print("NO")
            break
        available+=1
    else:
        print("YES")