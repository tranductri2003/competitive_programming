t=int(input())
for _ in range(t):
    a,b,c = list(map(int,input().split()))
    thang1 = a+c//2
    if c%2==1:
        thang1+=1
    thang2 = b+c//2
    if thang2>=thang1:
        print("Second")
    else:
        print("First")