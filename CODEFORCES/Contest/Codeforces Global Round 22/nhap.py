
check = False
n = -1


for i in range(2, 27):
    print("?", 1, i, flush=True)
    t1 = int(input())
    if t1 == -1:
        n = i-1
        check = True
        break

    print("?", i, 1, flush=True)
    t2 = int(input())
    if t2 == -1:
        n = i-1
        check = True
        break

    if t1 != t2:
        break

if check == True:
    print("!", n)
else:
    print("!", t1+t2)
