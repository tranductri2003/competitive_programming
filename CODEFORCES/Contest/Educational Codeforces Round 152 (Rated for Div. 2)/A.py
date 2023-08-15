t = int(input())
for _ in range(t):
    b, c, h = list(map(int, input().split()))
    temp = c+h
    if b >= temp+1:
        print(temp*2+1)
    else:
        print(b+b-1)
