N = int(input())

data = []
for _ in range(N):
    s = input()
    if s == "TRUTH":
        data.append(1)
    else:
        data.append(-1)


if data[-1] == 1:
    pass
else:
    data[-2] *= -1
for i in range(N-2, 0, -1):
    if data[i] == 1:
        pass
    else:
        data[i-1] *= -1

if data[0] == 1:
    print("TRUTH")
else:
    print("LIE")
