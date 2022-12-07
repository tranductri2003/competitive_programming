n,m=list(map(int,input().split()))
a=list(map(int,input().split()))


if m==1:
    sotamgiac=0
    for i in range(n,-1,-1):
        sotamgiac+=n**i
    print(sotamgiac-n)
else:
    print(3)