def intersect(a, b):
    if a[1] < b[0] or b[1] < a[0]:
        return (-1, -1)
    return (max(a[0], b[0]), min(a[1], b[1]))


n, l, r, k = list(map(int, input().split()))
a = list(map(int, input().split()))

dif = [0]*(n+5)
for i in range(1, n):
    if a[i-1] == a[i]:
        dif[i-1] = 0
    else:
        if a[i-1] < a[i]:
            dif[i-1] = 1
        else:
            dif[i-1] = -1

stop = False
bound = [(0, 0)]*(n+5)
bound[n-1] = (l, r)
for i in range(n-2, -1, -1):
    if dif[i] == 0:
        bound[i] = bound[i+1]
    elif dif[i] == -1:
        if bound[i+1][0]+1 > r:
            print(-1)
            stop = True
            break
        low = bound[i+1][0]+1
        high = min(bound[i+1][1]+k, r)
        bound[i] = (low, high)
    else:
        if bound[i+1][1]-1 < l:
            print(-1)
            stop = True
            break
        low = max(bound[i+1][0]-k, l)
        high = bound[i+1][1]-1
        bound[i] = (low, high)

if stop == False:
    tmp = bound[0][0]
    print(tmp, end=" ")
    for i in range(0, n-1):
        if dif[i] == -1:
            ints = intersect((tmp-k, tmp-1), bound[i+1])
            tmp = ints[0]
        elif dif[i] == 1:
            ints = intersect((tmp+1, tmp+k), bound[i+1])
            tmp = ints[0]
        print(tmp, end=" ")
