for _ in range(int(input())):
    b, r, d, s = list(map(int, input().split()))

    if r == 0:
        if d > 0:
            print("gua!")
        else:
            print("ok")
    else:
        nghi = 1/r*60
        numkhoangcach = s/nghi
        # print(numkhoangcach)
        if numkhoangcach % 1 == 0:
            maxInFact = numkhoangcach+1
        else:
            maxInFact = numkhoangcach//1+1
        maxDamgeInFact = maxInFact*b
        if d > maxDamgeInFact:
            print("gua!")
        else:
            print('ok')
    # dan = r*s//60
    # if r != 0:
    #     dan += 1
    # if dan*b < d:
    #     print("gua!")
    # else:
    #     print("ok")
