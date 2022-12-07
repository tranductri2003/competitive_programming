n, t = list(map(int, input().split()))
if t == 1:
    print(1)
else:
    temp = bin(n)[2:]
    print(temp)
