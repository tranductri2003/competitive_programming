from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print("N")
else:
    check = defaultdict(lambda: 0)
    a.sort()
    for i in range(0, n):
        temp = a[i]
        while check[temp] != 0:
            check[temp] -= 1
            temp += 1
        check[temp] = 1

    temp = 0
    data = check.values()
    temp = 0
    for num in data:
        if num != 0:
            temp += 1
    if temp == 2 or temp == 1:
        print("Y")
    else:
        print("N")
