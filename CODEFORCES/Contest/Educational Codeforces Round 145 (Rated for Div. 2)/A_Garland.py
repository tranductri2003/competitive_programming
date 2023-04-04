t = int(input())
for _ in range(t):
    a = input()
    s1 = int(a[0])
    s2 = int(a[1])
    s3 = int(a[2])
    s4 = int(a[3])
    data = [s1, s2, s3, s4]
    if len(set(data)) == 1:
        print(-1)
    elif len(set(data)) == 4 or len(set(data)) == 3:
        print(4)
    elif len(set(data)) == 2:
        data.sort()
        if data[0] == data[1] == data[2] or data[1] == data[2] == data[3]:
            print(6)
        else:
            print(4)
