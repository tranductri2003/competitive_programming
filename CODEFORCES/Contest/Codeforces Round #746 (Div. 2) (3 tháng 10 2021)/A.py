testcase=int(input())

for test in range(0,testcase):
    n,H=list(map(int,input().split()))
    a=list(map(int,input().split()))
    
    a.sort(reverse=True)
    max=a[0]
    secondmax=a[1]

    b=H//(max+secondmax)

    c=H-b*(max+secondmax)
    if c==0:
        print(b*2)
    elif c>max:
        print(b*2+2)
    else:
        print(b*2+1)
