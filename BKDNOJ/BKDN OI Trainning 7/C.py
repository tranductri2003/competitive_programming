n = int(input())
bach = []
khoa = []
for i in range(n):
    bach.append(int(input()))

for i in range(1, 2*n+1):
    if i not in bach:
        khoa.append(i)

bach.sort()
khoa.sort()

previous = bach.pop(0)
luotbach = False
luotkhoa = True

# print(bach)
# print(khoa)
while len(bach) > 0 and len(khoa) > 0:
    if len(bach) == 0 or len(khoa) == 0:
        break
    if luotkhoa == True:
        for i in range(len(khoa)):
            if khoa[i] > previous:
                previous = khoa.pop(i)
                luotbach = True
                luotkhoa = False
                break
        else:
            luotkhoa = True
            luotbach = False
            previous = bach.pop(0)
    elif luotbach == True:
        for i in range(len(bach)):
            if bach[i] > previous:
                previous = bach.pop(i)
                luotbach = False
                luotkhoa = True
                break
        else:
            luotkhoa = False
            luotbach = True
            previous = khoa.pop(0)

    if len(bach) == 0 or len(khoa) == 0:
        break
    # print(bach)
    # print(khoa)
    # print()


# print(bach)
# print(khoa)
print(len(khoa))
print(len(bach))
