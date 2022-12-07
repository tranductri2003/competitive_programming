t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if len(set(a))==1:
        print("NO")
    else:
        print("YES")
        exist=[]
        for i in range(1,n):
            if a[i]!=a[0]:
                print(1,i+1)
            else:
                exist.append(i+1)
        for i in range(1,n):
            if a[i]!=a[0]:
                pos=i
                break
        for num in exist:
            print(num,pos+1)