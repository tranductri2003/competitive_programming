testcase=int(input())
for test in range(testcase):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    res=max(max(a),max(b))
    sonhonhat=-10**9
    for i in range(0,n):
        sonhonhat=max(sonhonhat,min(a[i],b[i]))
    res=max(max(a),max(b))*sonhonhat
    print(res)
    