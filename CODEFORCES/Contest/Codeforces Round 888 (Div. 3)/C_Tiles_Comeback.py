t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    c = list(map(int, input().split()))

    soBatDau = c[0]
    soCuoiCung = c[-1]
    if c.count(soBatDau) < k or c.count(soCuoiCung) < k:
        print("NO")
    else:
        if soCuoiCung == soBatDau:
            print("YES")
        else:
            leftToRight = []
            numBatDau = 0
            rightToLeft = []
            numCuoiCung = 0
            for i in range(n):
                if numBatDau == k:
                    break
                if c[i] == soBatDau:
                    leftToRight.append(i)
                    numBatDau += 1

            for i in range(n-1, -1, -1):
                if numCuoiCung == k:
                    break
                if c[i] == soCuoiCung:
                    rightToLeft.append(i)
                    numCuoiCung += 1

            data = leftToRight+rightToLeft[::-1]
            if data == sorted(data):
                print("YES")
            else:
                print("NO")
