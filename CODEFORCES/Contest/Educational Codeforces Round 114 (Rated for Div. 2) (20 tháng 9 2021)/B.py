testcase=int(input())

for i in range(0,testcase):
    a,b,c,m=list(map(int,input().split()))
    maxlienke=a-1+b-1+c-1
    if m>maxlienke:
        print("NO")
    else:
        if max(a,b,c)==a:
            khoang=b+c-1
        if max(a,b,c)==b:
            khoang=a+c-1
        if max(a,b,c)==c:
            khoang=b+a-1
        minlienke=max(a,b,c)-(khoang+2)
        if minlienke<=m<=maxlienke:
            print("YES")
        else:
            print("NO")