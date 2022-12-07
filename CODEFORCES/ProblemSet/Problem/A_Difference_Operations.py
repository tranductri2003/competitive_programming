for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    data = []
    for i in range(1, n):
        data.append(a[i]-a[i-1])

    if len(list(set(data))) == 1:
        print("YES")
    else:
        print("NO")
