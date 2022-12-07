l = int(input())
r = int(input())
temp = 0
for i in range(l, r+1):
    temp = str(i)
    for j in range(len(temp)):
        c *= int(temp[j])
    print(i, c)
