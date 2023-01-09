from collections import defaultdict
t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    subM = m
    a = list(map(int, input().split()))
    a.sort()
    new = list(set(a))
    new.sort()

    numNguoi = defaultdict(lambda: 0)
    for num in a:
        numNguoi[num] += 1

    nguoiWin = defaultdict(lambda: 0)
    nguoiWin[new[0]] = 0
    for i in range(1, len(new)):
        nguoiWin[new[i]] = nguoiWin[new[i-1]]+numNguoi[new[i-1]]

    # print(nguoiWin)

    soNguoiGietMax = 0
    for i in range(0, n):
        if m >= a[i]:
            soNguoiGietMax += 1
            m -= a[i]
        else:
            break
    prePos = -1
    nguoiMaMinhHon = []
    for i in range(0, soNguoiGietMax-1):
        nguoiMaMinhHon.append(a[i])
        subM -= a[i]
        prePos = i
    # if soNguoiGietMax == 0:
    #     print("Khong hon ai ca")
    #     pass

    if soNguoiGietMax != 0:
        i = 0
        pos = -1
        while i < n:
            if a[i] <= subM:
                i += 1
            else:
                pos = i-1  # vi tri cuoi cung ma minh hon
                nguoiMaMinhHon.append(a[i-1])
                break
                i += 1
        if i == n:
            pos = n-1
            nguoiMaMinhHon.append(a[-1])
    # print(nguoiMaMinhHon)
    checkNguoiMaMinhHon = defaultdict(lambda: False)
    for num in nguoiMaMinhHon:
        checkNguoiMaMinhHon[num] = True

    diemMinh = len(nguoiMaMinhHon)
    # print(nguoiWin)

    tongKetDiemNguoiKhac = [0]*n
    for i in range(n):
        tongKetDiemNguoiKhac[i] = nguoiWin[a[i]]

    if soNguoiGietMax == 0:
        pos = -1
    for i in range(prePos+1, pos):
        tongKetDiemNguoiKhac[i] += 1
    for i in range(pos+1, n):
        tongKetDiemNguoiKhac[i] += 1

    # print(a)
    # print(tongKetDiemNguoiKhac)
    # print(diemMinh)
    # print()
    res = 0
    for i in range(n):
        if tongKetDiemNguoiKhac[i] > diemMinh:
            res += 1
    print(res+1)
