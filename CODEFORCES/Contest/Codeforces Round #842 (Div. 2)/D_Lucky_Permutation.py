
def minSwaps(arr, n):
    arrpos = [*enumerate(arr)]

    arrpos.sort(key=lambda it: it[1])

    vis = {k: False for k in range(n)}

    ans = 0
    for i in range(n):

        if vis[i] or arrpos[i][0] == i:
            continue

        cycle_size = 0
        j = i

        while not vis[j]:

            vis[j] = True

            j = arrpos[j][0]
            cycle_size += 1

        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # day1 = []
    # for num in a:
    #     if num == 1:
    #         day1.append(2)
    #     elif num == 2:
    #         day1.append(1)
    #     else:
    #         day1.append(num)

    # day2 = []
    # for num in a:
    #     if num == n:
    #         day2.append(n-1)
    #     elif num == n-1:
    #         day2.append(n)
    #     else:
    #         day2.append(num)
    # print(min(minSwaps(day1, n), minSwaps(day2, n)))
    veLaiBinhThuong = minSwaps(a, n)
    if a == sorted(a):
        print(veLaiBinhThuong+1)
    else:
        exist = False
        for i in range(n):
            if a[i] == i+2:
                exist = True

        if a[n-1] == n-1 and a[0] == n:
            exist = True
        if a[-1] == 1 and a[0] == 2:
            exist = True
        if exist:
            print(veLaiBinhThuong-1)
        else:
            print(veLaiBinhThuong+1)
