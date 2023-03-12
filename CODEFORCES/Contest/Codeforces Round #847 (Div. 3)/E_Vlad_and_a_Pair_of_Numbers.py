t = int(input())
for _ in range(t):
    x = int(input())
    if x % 2 == 1:
        print(-1)
    else:
        down = x//2
        up = down*3
        if down ^ up == x:
            print(down, up)
        else:
            print(-1)
