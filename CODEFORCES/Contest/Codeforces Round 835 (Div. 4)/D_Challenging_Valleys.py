t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    minValue = min(a)
    pos = a.index(minValue)

    left = True
    right = True
    for i in range(pos, 0, -1):
        if a[i-1] < a[i]:
            left = False

    for i in range(pos, n-1):
        if a[i] > a[i+1]:
            right = False

    # print(left, right)
    if left and right:
        print("YES")
    else:
        print("NO")
