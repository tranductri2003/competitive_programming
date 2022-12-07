
t = int(input())
for _ in range(t):
    s = input()

    temp = sorted(s)
    keep = []
    deleted = []
    point = 0
    last = -1

    for i in range(len(s)):
        if s[i] == temp[point]:
            point += 1
            last = i

    point = 0
    for i in range(len(s)):
        if s[i] == temp[point]:
            keep.append(s[i])
            point += 1
        else:
            if i <= last:
                deleted.append(min(int(s[i])+1, 9))
            else:
                deleted.append(int(s[i]))

    deleted.sort()
    res = keep+deleted
    for i in range(len(res)):
        res[i] = str(res[i])
    res = "".join(res)
    print(res)
