n=int(input())

if n%2==0:
    print(round(n/2))
    for i in range(0,round(n/2)):
        print("2",end=" ")
else:
    print(round((n-3)/2)+1)
    for i in range(0,round((n-3)/2)):
        print("2",end=" ")
    print("3")