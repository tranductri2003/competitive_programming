t = int(input())
for _ in range(t):
    n, h = list(map(int, input().split()))
    temph = h
    a = list(map(int, input().split()))
    green = 2
    blue = 1
    res = 0
    a.sort()
    for i in range(n):
        if h > a[i]:
            h += a[i]//2
            res += 1
        else:
            if h*2 > a[i]:
                if green:
                    h *= 2
                    h += a[i]//2
                    green -= 1
                    res += 1
                elif blue:
                    h *= 3
                    h += a[i]//2
                    blue -= 1
                    res += 1
                else:
                    break
            elif h*3 > a[i]:
                if blue:
                    h *= 3
                    h += a[i]//2
                    blue -= 1
                    res += 1
                elif green == 2:
                    h *= 4
                    h += a[i]//2
                    green -= 2
                    res += 1
                else:
                    break
            elif h*4 > a[i]:
                if green == 2:
                    h *= 4
                    h += a[i]//2
                    green -= 2
                    res += 1
                elif green == 1 and blue == 1:
                    h *= 6
                    h += a[i]//2
                    green -= 1
                    blue -= 1
                    res += 1
                else:
                    break
            elif h*6 > a[i]:
                if green and blue:
                    h *= 6
                    h += a[i]//2
                    green -= 1
                    blue -= 1
                    res += 1
                else:
                    break
            elif h*12 > a[i]:
                if green == 2 and blue:
                    h *= 12
                    h += a[i]//2
                    green -= 2
                    blue -= 1
                    res += 1
                else:
                    break
            else:
                break

    res2 = 0
    blue = 1
    green = 2
    h = temph
    for i in range(n):
        if h > a[i]:
            h += a[i]//2
            res2 += 1
        else:
            if blue:
                h *= 3
                blue -= 1
            if h > a[i]:
                h += a[i]//2
                res2 += 1
            elif h*2 > a[i]:
                if green:
                    h *= 2
                    h += a[i]//2
                    green -= 1
                    res2 += 1
                elif blue:
                    h *= 3
                    h += a[i]//2
                    blue -= 1
                    res2 += 1
                else:
                    break
            elif h*3 > a[i]:
                if blue:
                    h *= 3
                    h += a[i]//2
                    blue -= 1
                    res2 += 1
                elif green == 2:
                    h *= 4
                    h += a[i]//2
                    green -= 2
                    res2 += 1
                else:
                    break
            elif h*4 > a[i]:
                if green == 2:
                    h *= 4
                    h += a[i]//2
                    green -= 2
                    res2 += 1
                elif green == 1 and blue == 1:
                    h *= 6
                    h += a[i]//2
                    green -= 1
                    blue -= 1
                    res2 += 1
                else:
                    break
            elif h*6 > a[i]:
                if green and blue:
                    h *= 6
                    h += a[i]//2
                    green -= 1
                    blue -= 1
                    res2 += 1
                else:
                    break
            elif h*12 > a[i]:
                if green == 2 and blue:
                    h *= 12
                    h += a[i]//2
                    green -= 2
                    blue -= 1
                    res2 += 1
                else:
                    break
            else:
                break

    res3 = 0
    blue = 1
    green = 2
    h = temph
    for i in range(n):
        if h > a[i]:
            h += a[i]//2
            res3 += 1
        else:
            if green == 2:
                h *= 4
                green -= 2
            if h > a[i]:
                h += a[i]//2
                res3 += 1
            elif h*2 > a[i]:
                if green:
                    h *= 2
                    h += a[i]//2
                    green -= 1
                    res3 += 1
                elif blue:
                    h *= 3
                    h += a[i]//2
                    blue -= 1
                    res3 += 1
                else:
                    break
            elif h*3 > a[i]:
                if blue:
                    h *= 3
                    h += a[i]//2
                    blue -= 1
                    res3 += 1
                elif green == 2:
                    h *= 4
                    h += a[i]//2
                    green -= 2
                    res3 += 1
                else:
                    break
            elif h*4 > a[i]:
                if green == 2:
                    h *= 4
                    h += a[i]//2
                    green -= 2
                    res3 += 1
                elif green == 1 and blue == 1:
                    h *= 6
                    h += a[i]//2
                    green -= 1
                    blue -= 1
                    res3 += 1
                else:
                    break
            elif h*6 > a[i]:
                if green and blue:
                    h *= 6
                    h += a[i]//2
                    green -= 1
                    blue -= 1
                    res3 += 1
                else:
                    break
            elif h*12 > a[i]:
                if green == 2 and blue:
                    h *= 12
                    h += a[i]//2
                    green -= 2
                    blue -= 1
                    res3 += 1
                else:
                    break
            else:
                break
    print(max(res, res2, res3))
