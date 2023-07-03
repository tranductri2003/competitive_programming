s1 = input()
s2 = input()
dang1s1 = []
dang2s1 = []

dang1s2 = []
dang2s2 = []
for i in range(len(s1)):
    if ord(s1[i]) % 2 == 1:
        dang1s1.append(s1[i])
    else:
        dang2s1.append(s1[i])

for i in range(len(s2)):
    if ord(s2[i]) % 2 == 1:
        dang1s2.append(s2[i])
    else:
        dang2s2.append(s2[i])

# print(dang1s1, dang1s2, dang2s1, dang2s2)
if dang1s1 == dang1s2 and dang2s1 == dang2s2:
    print("Yes")
else:
    print("No")
