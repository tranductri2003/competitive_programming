t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    for num in a:
        if num==(sum(a)-num)/(n-1):
            print("YES")
            break
    else:
        print("NO")