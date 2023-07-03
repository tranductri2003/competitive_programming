t = int(input())
for _ in range(t):
    tm, sm, ty, sy = list(map(int, input().split()))

    if 100/(tm+sm) <= 10/sm:
        t1 = 100/(tm+sm)
    else:
        t1 = 90/tm
    if 100/(ty+sy) <= 10/sy:
        t2 = 100/(ty+sy)
    else:
        t2 = 90/ty

    # print(t1, t2)
    if t1 == t2:
        print("Draw")
    elif t1 > t2:
        print("Yunyun")
    else:
        print("Megumin")
