import math
n = int(input())
if math.sqrt(n) == int(math.sqrt(n)):
    temp = math.sqrt(n)
    temp = str(temp)[:-2]
    print(0, 0)
    print(temp, 0)
    print(0, temp)
    print(temp, temp)
else:
    stop = False
    for i in range(1, 1000):
        for j in range(1, 1000):
            if i**2+j**2 == n:
                print(i, 0)
                print(0, j)
                print(j, i+j)
                print(i+j, i)
                quit()

    print("Impossible")
