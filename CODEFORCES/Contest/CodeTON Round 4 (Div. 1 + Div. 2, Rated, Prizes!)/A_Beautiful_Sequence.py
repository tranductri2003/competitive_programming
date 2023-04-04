t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    stop = True
    for i in range(n):
        if i+1 >= a[i]:
            stop = False
    if stop == False:
        print("YES")
    else:
        print("NO")
