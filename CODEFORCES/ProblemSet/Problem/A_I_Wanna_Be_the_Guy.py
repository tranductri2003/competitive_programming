n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=a[1:]+b[1:]

for i in range(1,n+1):
    if i in res:
        pass
    else:
        print("Oh, my keyboard!")
        break
else:
    print("I become the guy.")
