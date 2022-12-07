import math
t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    if a == b:
        print("YES")
    else:
        for temp in range(b//a, 1, -1):
            if (b-temp*a) % (temp-1) == 0:
                print("YES")
                break
        else:
            print("NO")
