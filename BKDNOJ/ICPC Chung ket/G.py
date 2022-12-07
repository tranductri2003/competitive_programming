import random

for _ in range(10):
    # n = int(input())
    n = random.randint(1, 10)

    thamkhao = []
    check = []
    data = []
    for i in range(1, n+1):
        t = random.randint(0, 1)
        thamkhao.append(t)
        if check == []:
            check.append(t)
        else:
            if i % 2 == 1:
                check.append(t)
            else:
                if t != check[-1]:
                    for j in range(len(check)-1, -1, -1):
                        if check[j] != t:
                            check[j] = t
                        else:
                            break
                    check.append(t)
                else:
                    check.append(t)

        if i % 2 == 1:
            if data == []:
                data.append((1, t))
            elif data[-1][1] == t:
                temp = data[-1][0]
                data.pop()
                data.append((temp+1, t))
            else:
                data.append((1, t))
        else:
            if data == []:
                data.append((1, t))
            else:
                temp = data[-1][0]
                data.pop()
                data.append((temp+1, t))

    res = 0
    for num in data:
        if num[1] == 0:
            res += num[0]

    res1 = 0
    for num in check:
        if num == 0:
            res1 += 1

    if res != res1:
        print("as")
        print(thamkhao)
        break
