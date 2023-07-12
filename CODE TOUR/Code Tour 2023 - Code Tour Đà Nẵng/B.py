import math
t = int(input())

for _ in range(t):
    n, m, x = map(int, input().split())

    if n > m:
        n, m = m, n

    # TH1
    kichThuocGach = x*math.sqrt(3)
    soNgang = 0
    soDoc = 0
    ngang = 0
    doc = 0

    if n % kichThuocGach == 0:
        soNgang = n//kichThuocGach
    else:
        soNgang = n//kichThuocGach + 1

    while doc < m:
        if soDoc % 2 == 0:
            doc += x
        else:
            doc += 2*x
        soDoc += 1
    if soDoc % 2 == 0:
        res1 = soNgang*soDoc//2 + (soNgang+1)*soDoc//2
    else:
        res1 = soNgang*(soDoc//2+1) + (soNgang+1)*(soDoc//2)

    # TH2
    res2 = 0
    n, m = m, n
    kichThuocGach = x*math.sqrt(3)
    soNgang = 0
    soDoc = 0
    ngang = 0
    doc = 0

    if n % kichThuocGach == 0:
        soNgang = n//kichThuocGach
    else:
        soNgang = n//kichThuocGach + 1

    while doc < m:
        if soDoc % 2 == 0:
            doc += x
        else:
            doc += 2*x
        soDoc += 1

    if soDoc % 2 == 0:
        res2 = soNgang*soDoc//2 + (soNgang+1)*soDoc//2
    else:
        res2 = soNgang*(soDoc//2+1) + (soNgang+1)*(soDoc//2)

    res = min(res1, res2)
    if "." in str(res):
        print(str(res)[:-2])
    else:
        print(res)
