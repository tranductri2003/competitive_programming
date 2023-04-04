t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    chan = 0
    le = 0
    for num in a:
        if num % 2 == 0:
            chan += num
        else:
            le += num

    if chan > le:
        print("YES")
    else:
        print("NO")
