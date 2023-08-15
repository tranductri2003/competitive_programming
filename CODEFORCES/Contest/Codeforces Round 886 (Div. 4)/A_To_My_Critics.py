t = int(input())
for _ in range(t):
    a, b, c = list(map(int, input().split()))
    check = False
    if a+b >= 10 or a+c >= 10 or b+c >= 10:
        check = True

    if check:
        print("YES")
    else:
        print("NO")
