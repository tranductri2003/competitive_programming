t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    temp = []
    for num in s:
        temp.append(num)
    temp.sort()
    maxx = temp[-1]
    secondMax = temp[-2]
    for num in s:
        if num == maxx:
            print(num-secondMax, end=" ")
        else:
            print(num-maxx, end=" ")
    print()
