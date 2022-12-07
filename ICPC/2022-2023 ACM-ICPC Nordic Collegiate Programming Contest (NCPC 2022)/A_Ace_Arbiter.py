tong = ["Alice"]*23
for i in (1, 2, 5, 6, 9, 10, 13, 14, 17, 18, 21, 22):
    tong[i] = "Bob"

stop = False
Alice = [0]
Bob = [0]
n = int(input())
thdb = False
X = 0
Y = 0
for i in range(1, n+1):
    x, y = list(map(int, input().split("-")))
    if x == 11 and y == 11 and stop == False:
        print("error", i)
        stop = True

    if tong[x+y] == "Alice":
        Alice.append(x)
        Bob.append(y)
    else:
        Bob.append(x)
        Alice.append(y)

    if (Alice[i] < Alice[i-1] or Bob[i] < Bob[i-1]) and stop == False:
        print("error", i)
        stop = True
    elif thdb == True and (X != x or Y != y) and stop == False:
        print("error", i)
        stop = True
    if x == 11 or y == 11:
        thdb = True
        X = x
        Y = y
if stop == False:
    print("ok")
