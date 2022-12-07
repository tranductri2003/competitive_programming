t=int(input())
for _ in range(t):
    n=int(input())
    c=list(map(int,input().split()))

    
    #Nếu c[i] bằng 1 thì có nghĩa là n đang ở đầu dãy
    #! Chỉ có 1 số 1
    #! Chệnh lệch 2 số

    if c.count(1)!=1:
        print("NO")
    else:
        if n==1 and c[0]==1:
            print("YES")
        else:
            # c.append(c[0])
            # for i in range(n):
            # for i in range(n-1):
            #     if c[i+1]-c[i]<=1 and c[0]-c[-1]<=1:
            c.append(c[0])
            for i in range(n):
                if c[i+1]-c[i]<=1:
                    pass
                else:
                    print("NO")
                    break
            else:
                print("YES")
        