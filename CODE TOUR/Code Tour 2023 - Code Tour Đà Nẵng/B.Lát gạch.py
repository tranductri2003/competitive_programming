
from collections import defaultdict


def hexadecimal_to_decimal(hexadecimal):
    decimal = 0
    power = len(hexadecimal) - 1

    for digit in hexadecimal:
        if digit.isdigit():
            decimal += int(digit) * (16 ** power)
        else:
            decimal += (ord(digit.upper()) - 55) * (16 ** power)
        power -= 1

    return decimal


n = int(input())
anh1 = [0]*n
anh2 = [0]*n
res = [0]*n
for i in range(n):
    temp = input()[1:]
    R = temp[0:2]
    G = temp[2:4]
    B = temp[4:6]
    anh1[i] = (hexadecimal_to_decimal(
        R), hexadecimal_to_decimal(G), hexadecimal_to_decimal(B))


for i in range(n):
    temp = input()[1:]
    R = temp[0:2]
    G = temp[2:4]
    B = temp[4:6]
    anh2[i] = (hexadecimal_to_decimal(
        R), hexadecimal_to_decimal(G), hexadecimal_to_decimal(B))


for i in range(n):
    if anh2[i][0] >= anh1[i][0]:
        R = anh2[i][0]-anh1[i][0]
    else:
        R = anh2[i][0]+256-anh1[i][0]

    if anh2[i][1] >= anh1[i][1]:
        G = anh2[i][1]-anh1[i][1]
    else:
        G = anh2[i][1]+256-anh1[i][1]

    if anh2[i][2] >= anh1[i][2]:
        B = anh2[i][2]-anh1[i][2]
    else:
        B = anh2[i][2]+256-anh1[i][2]

    res[i] = (R, G, B)

print(res)

check = defaultdict(lambda: 0)
for i in range(n):
    check[res[i]] += 1


proportion = format(max(check.values())/n*100, ".2f")+"%"
print(proportion)
